# `oc adm cordon`

> ノードをスケジュール不可にする

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `cordon`

## Usage

```
oc adm cordon NODE [options]
```

## Examples

```bash
# ノード "foo" をスケジュール不可にする
oc adm cordon foo
```

## Options

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm cordon --help` / `gen-oc-help.py` で生成</sub>
