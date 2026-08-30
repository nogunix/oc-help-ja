#!/usr/bin/env python3
"""oc の --help を再帰展開して、エディタで読める Markdown ツリーに落とす。

  *.md / **/*.md ... 日本語訳（i18n/ja.json の対訳カタログを当てて生成）
  all.txt        ... 生ヘルプの連結（grep 用）
  README.md      ... 目次

  python3 gen-oc-help.py                 # 日本語 Markdown と all.txt と README.md を生成
  python3 gen-oc-help.py --extract       # 翻訳対象の文字列を i18n/ja.json に抽出
  python3 gen-oc-help.py --stats         # 翻訳の進捗を出す

翻訳しないもの: コマンド名、フラグ名、Usage 行、実行例のコマンド本体。
翻訳するもの:   説明文（段落単位）、箇条書き、サブコマンドの 1 行説明、
                オプションの説明、実行例の `#` コメント、末尾の注記。
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

SECTION_RE = re.compile(r'^([A-Z][A-Za-z/ ]*Commands|Available Commands):\s*$')
STOP_RE = re.compile(r'^(Usage|Options|Examples|Flags|Global Flags|Use ")')
ENTRY_RE = re.compile(r'^  ([a-z][a-z0-9][a-z0-9._-]*)\s{2,}(\S.*)$')
OPT_RE = re.compile(r'^\s{2,}(-.*?):\s*$')
BULLET_RE = re.compile(r'^\s*\*\s+(\S.*)$')
ANGLE_RE = re.compile(r'(?<!`)(<[A-Za-z][A-Za-z0-9._| -]*>)(?!`)')

CATALOG = {}     # msgid -> msgstr
COLLECT = None   # --extract のとき msgid を集める dict


def tr(s):
    """カタログ経由で訳文を返す。未訳なら原文のまま。"""
    key = ' '.join(s.split())
    if not key:
        return s
    if COLLECT is not None:
        COLLECT.setdefault(key, '')
    return CATALOG.get(key) or s


def run_help(oc, path):
    p = subprocess.run([oc] + path + ['--help'], capture_output=True, text=True)
    out = p.stdout if p.stdout.strip() else p.stderr
    return out.rstrip('\n') + '\n'


def parse_children(text):
    children, seen, in_section = [], set(), False
    for line in text.splitlines():
        if SECTION_RE.match(line):
            in_section = True
            continue
        if not in_section:
            continue
        if not line.strip():
            continue
        if STOP_RE.match(line) or not line.startswith('  '):
            in_section = False
            continue
        m = ENTRY_RE.match(line)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            children.append((m.group(1), m.group(2).strip()))
    return children


def split_sections(text):
    sections, kind, title, buf = [], 'prose', '', []

    def flush():
        nonlocal kind, title
        while buf and not buf[-1].strip():
            buf.pop()
        if buf or kind != 'prose':
            sections.append((kind, title, list(buf)))
        buf.clear()

    for line in text.splitlines():
        m = SECTION_RE.match(line)
        if m:
            flush()
            kind, title = 'commands', m.group(1)
            continue
        if re.match(r'^(Examples|Options|Usage|Flags|Global Flags):\s*$', line):
            flush()
            kind = title = line.rstrip(':').strip()
            kind = kind.lower()
            continue
        if line.startswith('Use "'):
            flush()
            kind, title = 'note', ''
            buf.append(line)
            flush()
            kind, title = 'prose', ''
            continue
        buf.append(line)
    flush()
    return sections


def inline(text):
    """素の Markdown で壊れる記法を最小限だけ守る。"""
    return ANGLE_RE.sub(r'`\1`', text.rstrip())


def dedent(lines):
    pad = min((len(l) - len(l.lstrip(' ')) for l in lines if l.strip()), default=0)
    return [l[pad:] if l.strip() else '' for l in lines]


def render_prose(lines, out, skip_first=None):
    body = dedent(lines)
    norm = lambda t: ' '.join(t.split()).rstrip('.').lower()
    if skip_first and body and norm(body[0]) == norm(skip_first):
        body = body[1:]
        while body and not body[0].strip():
            body = body[1:]
    para = []

    def flush_para():
        if para:
            out.append(inline(tr(' '.join(para))))
            out.append('')
            para.clear()

    for line in body:
        indent = len(line) - len(line.lstrip(' '))
        m = BULLET_RE.match(line)
        if not line.strip():
            flush_para()
        elif indent >= 4:
            # ヘルプ本文に埋め込まれた実行例。Markdown のコードブロックに任せる
            flush_para()
            out.append(line.rstrip())
        elif m:
            flush_para()
            out.append('- ' + inline(tr(m.group(1))))
        else:
            para.append(line.strip())
    flush_para()
    if out and out[-1] != '':
        out.append('')


def render_code(lines, out, lang='', comments=False):
    out.append('```' + lang)
    for line in dedent(lines):
        m = re.match(r'^(\s*)#\s+(\S.*)$', line) if comments else None
        out.append('%s# %s' % (m.group(1), tr(m.group(2))) if m else line.rstrip())
    out.append('```')
    out.append('')


def render_commands(lines, title, out, here_dir, path, root):
    if title and title != 'Available Commands':
        out += ['### ' + tr(title), '']
    for line in lines:
        m = ENTRY_RE.match(line)
        if not m:
            continue
        target = os.path.join(root, *path, m.group(1) + '.md')
        out.append('- [`%s`](%s) — %s' % (
            m.group(1), os.path.relpath(target, here_dir), inline(tr(m.group(2)))))
    out.append('')


def render_options(lines, out):
    cur = None
    for line in lines:
        m = OPT_RE.match(line)
        if m:
            cur = m.group(1).strip()
            out.append('- `%s`' % cur)
        elif line.strip() and cur:
            out += ['  %s' % inline(tr(line.strip())), '']
    if out and out[-1] != '':
        out.append('')


def md_path(root, path):
    name = path[-1] if path else 'oc'
    return os.path.join(root, *path[:-1], name + '.md')


def render_md(path, desc, text, root):
    full = 'oc ' + ' '.join(path) if path else 'oc'
    here_dir = os.path.dirname(md_path(root, path))
    out = ['# `%s`' % full, '']
    if desc:
        out += ['> ' + inline(tr(desc)), '']

    if path:
        crumbs = []
        for i in range(len(path)):
            parent = path[:i]
            label = 'oc ' + ' '.join(parent) if parent else 'oc'
            crumbs.append('[`%s`](%s)' % (
                label, os.path.relpath(md_path(root, parent), here_dir)))
        out += [' / '.join(crumbs) + ' / `%s`' % path[-1], '']

    order = {'usage': 0, 'prose': 1, 'commands': 2, 'examples': 3,
             'options': 4, 'flags': 4, 'global flags': 4, 'note': 5}
    seen = set()
    for kind, title, lines in sorted(split_sections(text),
                                     key=lambda s: order.get(s[0], 6)):
        if not lines:
            continue
        if kind == 'usage':
            out += ['## Usage', '']
            render_code(lines, out)
        elif kind == 'prose':
            render_prose(lines, out, skip_first=desc if 'prose' not in seen else None)
            seen.add('prose')
        elif kind == 'commands':
            if 'commands' not in seen:
                out += ['## Subcommands', '']
                seen.add('commands')
            render_commands(lines, title, out, here_dir, path, root)
        elif kind == 'examples':
            out += ['## Examples', '']
            render_code(lines, out, 'bash', comments=True)
        elif kind in ('options', 'flags', 'global flags'):
            if 'options' not in seen:
                out += ['## Options', '']
                seen.add('options')
            render_options(lines, out)
        elif kind == 'note':
            out += ['> ' + inline(tr(l)) for l in lines] + ['']

    out += ['---', '']
    out += ['<sub>`$ %s --help` / `gen-oc-help.py` で生成</sub>' % full, '']

    body, prev_blank = [], False
    for line in out:
        blank = not line.strip()
        if blank and prev_blank:
            continue
        body.append(line)
        prev_blank = blank
    return '\n'.join(body).rstrip() + '\n'


def walk(oc, path, desc, depth, max_depth, nodes):
    text = run_help(oc, path)
    nodes.append((path, desc, text))
    print('  ' * depth + ('oc ' + ' '.join(path) if path else 'oc'), file=sys.stderr)
    if depth >= max_depth:
        return
    for child, cdesc in parse_children(text):
        walk(oc, path + [child], cdesc, depth + 1, max_depth, nodes)


def client_version(oc):
    ver = subprocess.run([oc, 'version', '--client', '-o', 'json'],
                         capture_output=True, text=True).stdout
    m = re.search(r'"gitVersion":\s*"([^"]+)"', ver)
    return m.group(1) if m else 'unknown'


def write_readme(out, nodes, version, root):
    path = os.path.join(out, 'README.md')
    with open(path, 'w') as f:
        f.write('# oc help tree（日本語） (`%s`)\n\n' % version)
        f.write('> **非公式の翻訳です。**\n')
        f.write('> 本リポジトリは [openshift/oc](https://github.com/openshift/oc)'
                '（Copyright 2014 Red Hat, Inc.、Apache License 2.0）の '
                '`--help` 出力を日本語に翻訳した派生著作物です。\n')
        f.write('> Red Hat, Inc. および OpenShift プロジェクトが'
                '本翻訳を承認・保証するものではありません。\n')
        f.write('> "OpenShift" は Red Hat, Inc. の登録商標です。\n\n')
        f.write('`gen-oc-help.py` で `oc ... --help` を再帰展開したもの。'
                '全 %d コマンド。\n\n' % len(nodes))
        f.write('- 読む: [`oc.md`](oc.md) から辿るか、下の目次から\n')
        f.write('- $EDITOR で開く: `./ochelp adm policy add-role-to-user`'
                '（引数なし + fzf で絞り込み）\n')
        f.write('- 全文検索: `./ochelp -g PATTERN`（`all.txt` の生ヘルプを検索）\n')
        f.write('- 再生成: `python3 gen-oc-help.py`\n\n')
        f.write('## ライセンス\n\n')
        f.write('原著作物（`oc` コマンドのヘルプテキスト）は Apache License 2.0 '
                'に基づいて提供されています。\n')
        f.write('本リポジトリの日本語訳も同ライセンスの下で配布します。'
                '詳細は [LICENSE](LICENSE) を参照してください。\n\n')
        f.write('## 目次\n\n')
        base = os.path.dirname(path)
        for p, desc, _ in nodes:
            label = 'oc ' + ' '.join(p) if p else 'oc'
            f.write('%s- [`%s`](%s) — %s\n' % (
                '  ' * len(p), label,
                os.path.relpath(md_path(root, p), base), tr(desc)))


def main():
    global CATALOG, COLLECT
    ap = argparse.ArgumentParser()
    ap.add_argument('--oc', default=shutil.which('oc') or 'oc')
    ap.add_argument('--out', default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument('--max-depth', type=int, default=6)
    ap.add_argument('--extract', action='store_true')
    ap.add_argument('--stats', action='store_true')
    args = ap.parse_args()

    cat_path = os.path.join(args.out, 'i18n', 'ja.json')
    if os.path.exists(cat_path):
        CATALOG = json.load(open(cat_path))

    if args.stats:
        done = sum(1 for v in CATALOG.values() if v)
        print('%d / %d translated (%.1f%%)' % (
            done, len(CATALOG), 100.0 * done / max(len(CATALOG), 1)))
        return

    if args.extract:
        COLLECT = {}

    version = client_version(args.oc)
    nodes = []
    walk(args.oc, [], 'OpenShift Client', 0, args.max_depth, nodes)

    root = args.out
    md_dirs = set()
    for p, _, _ in nodes:
        d = os.path.dirname(md_path(root, p))
        if d != root:
            md_dirs.add(d)

    if not args.extract:
        for p, desc, text in nodes:
            dest = md_path(root, p)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'w') as f:
                f.write(render_md(p, desc, text, root))
        write_readme(args.out, nodes, version, root)

        with open(os.path.join(args.out, 'all.txt'), 'w') as f:
            f.write('oc %s - all help texts\n' % version)
            for p, _desc, text in nodes:
                title = 'oc ' + ' '.join(p) if p else 'oc'
                f.write('\n\n' + '=' * 78 + '\n== %s\n' % title + '=' * 78 + '\n\n')
                f.write(text)
    else:
        for p, desc, text in nodes:
            render_md(p, desc, text, root)

    if args.extract:
        merged = dict(COLLECT)
        merged.update({k: v for k, v in CATALOG.items() if k in COLLECT and v})
        os.makedirs(os.path.dirname(cat_path), exist_ok=True)
        with open(cat_path, 'w') as f:
            json.dump(merged, f, ensure_ascii=False, indent=1, sort_keys=True)
        stale = len(CATALOG) - sum(1 for k in CATALOG if k in COLLECT)
        print('\n%d msgids -> %s (%d translated, %d stale dropped)' % (
            len(merged), cat_path,
            sum(1 for v in merged.values() if v), stale), file=sys.stderr)
    else:
        print('\n%d commands -> %s' % (len(nodes), root), file=sys.stderr)


if __name__ == '__main__':
    main()
