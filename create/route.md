# `oc create route`

> セキュアな Route を通じてコンテナを外部に公開する

[`oc`](../oc.md) / [`oc create`](../create.md) / `route`

## Usage

```
oc create route [flags] [options]
```

セキュアなルートは edge、passthrough、reencrypt の 3 種類がサポートされています。セキュアでないルートを作成したい場合は "oc expose -h" を参照してください。

## Subcommands

- [`edge`](route/edge.md) — edge TLS 終端を使うルートを作成する
- [`passthrough`](route/passthrough.md) — passthrough TLS 終端を使うルートを作成する
- [`reencrypt`](route/reencrypt.md) — reencrypt TLS 終端を使うルートを作成する

> 各コマンドの詳細については "oc create route `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create route --help` / `gen-oc-help.py` で生成</sub>
