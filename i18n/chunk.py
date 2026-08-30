#!/usr/bin/env python3
"""ja.json の msgid を索引付きチャンクに割る / 訳文を索引で流し込む。"""
import json, os, sys

D = os.path.dirname(os.path.abspath(__file__))
CAT = os.path.join(D, 'ja.json')
KEYS = os.path.join(D, 'keys.json')

def keys():
    if os.path.exists(KEYS):
        return json.load(open(KEYS))
    ks = sorted(json.load(open(CAT)))
    json.dump(ks, open(KEYS, 'w'), ensure_ascii=False, indent=0)
    return ks

def cmd_split(budget=20000):
    ks, chunks, cur, n = keys(), [], [], 0
    for i, k in enumerate(ks):
        cur.append(i); n += len(k)
        if n >= budget:
            chunks.append(cur); cur, n = [], 0
    if cur: chunks.append(cur)
    for c, idxs in enumerate(chunks):
        with open(os.path.join(D, 'parts', 'chunk-%02d.txt' % c), 'w') as f:
            for i in idxs:
                f.write('%d\t%s\n' % (i, ks[i].replace('\n', ' ')))
    print('%d chunks, %d msgids' % (len(chunks), len(ks)))

def cmd_apply():
    ks, cat = keys(), json.load(open(CAT))
    applied = 0
    for fn in sorted(os.listdir(os.path.join(D, 'parts'))):
        if not fn.endswith('.json'): continue
        for i, v in json.load(open(os.path.join(D, 'parts', fn))).items():
            if v and v.strip():
                cat[ks[int(i)]] = v.strip(); applied += 1
    json.dump(cat, open(CAT, 'w'), ensure_ascii=False, indent=1, sort_keys=True)
    done = sum(1 for v in cat.values() if v)
    print('applied %d, translated %d/%d (%.1f%%)' % (applied, done, len(cat), 100.0*done/len(cat)))

def cmd_todo():
    ks, cat = keys(), json.load(open(CAT))
    miss = [i for i, k in enumerate(ks) if not cat.get(k)]
    print('untranslated: %d' % len(miss))
    print(' '.join(map(str, miss[:40])))

if __name__ == '__main__':
    {'split': cmd_split, 'apply': cmd_apply, 'todo': cmd_todo}[sys.argv[1]](*[int(a) for a in sys.argv[2:]])
