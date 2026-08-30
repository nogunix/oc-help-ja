# `oc config unset`

> kubeconfig ファイル内の個々の値を解除する

[`oc`](../oc.md) / [`oc config`](../config.md) / `unset`

## Usage

```
oc config unset PROPERTY_NAME [options]
```

PROPERTY_NAME はドット区切りの名前で、各要素は属性名またはマップのキーを表します。マップのキーにドットを含めることはできません。

## Examples

```bash
# current-context を解除する
oc config unset current-context

# foo コンテキストの namespace を解除する
oc config unset contexts.foo.namespace
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config unset --help` / `gen-oc-help.py` で生成</sub>
