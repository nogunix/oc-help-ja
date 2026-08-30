#!/usr/bin/env python3
"""oc の --help を再帰的に展開して、エディタで読める Markdown ツリーに落とす。

  help/oc.md               ... `oc --help`
  help/adm.md              ... `oc adm --help`
  help/adm/policy.md       ... `oc adm policy --help`
  help/adm/policy/*.md     ... さらにその下
  all.txt                  ... 生ヘルプ全部を 1 ファイルに連結（grep 用）
  README.md                ... 目次（相対リンク付き）

使い方: python3 gen-oc-help.py [--oc /path/to/oc] [--out DIR] [--max-depth N]
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

# "Available Commands:" / "Basic Commands:" / "Advanced Commands:" など
SECTION_RE = re.compile(r'^([A-Z][A-Za-z/ ]*Commands|Available Commands):\s*$')
# セクション終端になる見出し
STOP_RE = re.compile(r'^(Usage|Options|Examples|Flags|Global Flags|Use ")')
# "  get               Display one or many resources"
ENTRY_RE = re.compile(r'^  ([a-z][a-z0-9][a-z0-9._-]*)\s{2,}(\S.*)$')
# "    -A, --all-namespaces=false:"
OPT_RE = re.compile(r'^\s{2,}(-.*?):\s*$')
BULLET_RE = re.compile(r'^\s*\*\s+(\S.*)$')
# 山括弧トークン（<name> など）は素の Markdown だと HTML タグとして食われる
ANGLE_RE = re.compile(r'(?<!`)(<[A-Za-z][A-Za-z0-9._| -]*>)(?!`)')


def run_help(oc, path):
    p = subprocess.run([oc] + path + ['--help'], capture_output=True, text=True)
    out = p.stdout if p.stdout.strip() else p.stderr
    return out.rstrip('\n') + '\n'


def parse_children(text):
    """help 本文から (サブコマンド名, 1行説明) を順序どおりに抜き出す。"""
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
    """生ヘルプを [(kind, title, lines)] に分解する。"""
    sections, kind, title, buf = [], 'prose', '', []

    def flush():
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
            kind, title = line.rstrip(':').strip().lower(), line.rstrip(':').strip()
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
    """Markdown で壊れやすい記法を最小限だけ守る。"""
    return ANGLE_RE.sub(r'`\1`', text.rstrip())


def dedent(lines):
    pad = min((len(l) - len(l.lstrip(' ')) for l in lines if l.strip()), default=0)
    return [l[pad:] if l.strip() else '' for l in lines]


def render_prose(lines, out, skip_first=None):
    body = dedent(lines)
    norm = lambda t: t.strip().rstrip('.').lower()
    if skip_first and body and norm(body[0]) == norm(skip_first):
        body = body[1:]
        while body and not body[0].strip():
            body = body[1:]
    for line in body:
        indent = len(line) - len(line.lstrip(' '))
        if indent >= 4:
            # 深いインデントはヘルプ中の埋め込み例。Markdown のコードブロックに任せる
            out.append(line.rstrip())
            continue
        m = BULLET_RE.match(line)
        out.append('- ' + inline(m.group(1)) if m else inline(line.lstrip(' ')))
    out.append('')


def render_code(lines, out, lang=''):
    out.append('```' + lang)
    out.extend(l.rstrip() for l in dedent(lines))
    out.append('```')
    out.append('')


def render_commands(lines, title, out, here_dir, path, out_dir):
    if title and title != 'Available Commands':
        out.append('### ' + title)
        out.append('')
    for line in lines:
        m = ENTRY_RE.match(line)
        if not m:
            continue
        name, desc = m.group(1), m.group(2).strip()
        target = os.path.join(out_dir, 'help', *path, name + '.md')
        out.append('- [`%s`](%s) — %s' % (
            name, os.path.relpath(target, here_dir), inline(desc)))
    out.append('')


def render_options(lines, out):
    cur = None
    for line in lines:
        m = OPT_RE.match(line)
        if m:
            cur = m.group(1).strip()
            out.append('- `%s`' % cur)
        elif line.strip() and cur:
            out.append('  %s' % inline(line.strip()))
            out.append('')
    if out and out[-1] != '':
        out.append('')


def render_md(path, desc, text, out_dir):
    """1 コマンド分の Markdown を組み立てる。"""
    full = 'oc ' + ' '.join(path) if path else 'oc'
    here_dir = os.path.dirname(md_path(out_dir, path))
    out = ['# `%s`' % full, '']
    if desc:
        out += ['> ' + inline(desc), '']

    # パンくず（親コマンドへのリンク）
    if path:
        crumbs = []
        for i in range(len(path)):
            parent = path[:i]
            label = 'oc ' + ' '.join(parent) if parent else 'oc'
            crumbs.append('[`%s`](%s)' % (
                label, os.path.relpath(md_path(out_dir, parent), here_dir)))
        out += [' / '.join(crumbs) + ' / `%s`' % path[-1], '']

    order = {'usage': 0, 'prose': 1, 'commands': 2, 'examples': 3,
             'options': 4, 'flags': 4, 'global flags': 4, 'note': 5}
    sections = sorted(split_sections(text),
                      key=lambda s: (order.get(s[0], 6),))
    seen_head = set()
    for kind, title, lines in sections:
        if not lines:
            continue
        if kind == 'usage':
            out += ['## Usage', '']
            render_code(lines, out)
        elif kind == 'prose':
            render_prose(lines, out, skip_first=desc if 'prose' not in seen_head else None)
            seen_head.add('prose')
        elif kind == 'commands':
            if 'commands' not in seen_head:
                out += ['## Subcommands', '']
                seen_head.add('commands')
            render_commands(lines, title, out, here_dir, path, out_dir)
        elif kind == 'examples':
            out += ['## Examples', '']
            render_code(lines, out, 'bash')
        elif kind in ('options', 'flags', 'global flags'):
            if 'options' not in seen_head:
                out += ['## Options', '']
                seen_head.add('options')
            render_options(lines, out)
        elif kind == 'note':
            for line in lines:
                out.append('> ' + inline(line))
            out.append('')

    out += ['---', '',
            '<sub>`$ %s --help` / `gen-oc-help.py` で生成</sub>' % full, '']
    # 空行の連続をつぶす
    body, prev_blank = [], False
    for line in out:
        blank = not line.strip()
        if blank and prev_blank:
            continue
        body.append(line)
        prev_blank = blank
    return '\n'.join(body).rstrip() + '\n'


def md_path(out_dir, path):
    name = path[-1] if path else 'oc'
    return os.path.join(out_dir, 'help', *path[:-1], name + '.md')


def walk(oc, out_dir, path, desc, depth, max_depth, nodes):
    text = run_help(oc, path)
    dest = md_path(out_dir, path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, 'w') as f:
        f.write(render_md(path, desc, text, out_dir))
    nodes.append((path, desc, os.path.relpath(dest, out_dir), text))
    print('  ' * depth + ('oc ' + ' '.join(path) if path else 'oc'),
          file=sys.stderr)
    if depth >= max_depth:
        return
    for child, cdesc in parse_children(text):
        walk(oc, out_dir, path + [child], cdesc, depth + 1, max_depth, nodes)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--oc', default=shutil.which('oc') or 'oc')
    ap.add_argument('--out', default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument('--max-depth', type=int, default=6)
    args = ap.parse_args()

    ver = subprocess.run([args.oc, 'version', '--client', '-o', 'json'],
                         capture_output=True, text=True).stdout
    m = re.search(r'"gitVersion":\s*"([^"]+)"', ver)
    version = m.group(1) if m else 'unknown'

    help_dir = os.path.join(args.out, 'help')
    if os.path.isdir(help_dir):
        shutil.rmtree(help_dir)

    nodes = []
    walk(args.oc, args.out, [], 'OpenShift Client', 0, args.max_depth, nodes)

    # all.txt: 生ヘルプを 1 ファイルに（grep 用）
    with open(os.path.join(args.out, 'all.txt'), 'w') as f:
        f.write('oc %s - all help texts\n' % version)
        for path, _desc, _rel, text in nodes:
            title = 'oc ' + ' '.join(path) if path else 'oc'
            f.write('\n\n' + '=' * 78 + '\n== %s\n' % title + '=' * 78 + '\n\n')
            f.write(text)

    # README.md: 目次
    with open(os.path.join(args.out, 'README.md'), 'w') as f:
        f.write('# oc help tree (`%s`)\n\n' % version)
        f.write('`gen-oc-help.py` で `oc ... --help` を再帰展開したもの。'
                '全 %d コマンド。\n\n' % len(nodes))
        f.write('- 読む: [`help/oc.md`](help/oc.md) から辿るか、下の目次から\n')
        f.write('- $EDITOR で開く: `./ochelp adm policy add-role-to-user`'
                '（引数なし + fzf で絞り込み）\n')
        f.write('- 全文検索: `./ochelp -g PATTERN` / `rg PATTERN help/`'
                '（`all.txt` に生ヘルプを連結してある）\n')
        f.write('- 再生成: `python3 gen-oc-help.py`\n\n')
        f.write('## 目次\n\n')
        for path, desc, rel, _text in nodes:
            label = 'oc ' + ' '.join(path) if path else 'oc'
            indent = '  ' * len(path)
            f.write('%s- [`%s`](%s) — %s\n' % (indent, label, rel, desc))

    print('\n%d commands -> %s' % (len(nodes), args.out), file=sys.stderr)


if __name__ == '__main__':
    main()
