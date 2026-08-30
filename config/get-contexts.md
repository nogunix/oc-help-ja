# `oc config get-contexts`

> 1 つまたは複数のコンテキストの詳細を表示する

[`oc`](../oc.md) / [`oc config`](../config.md) / `get-contexts`

## Usage

```
oc config get-contexts [(-o|--output=)name)] [options]
```

kubeconfig ファイルから 1 つまたは複数のコンテキストを表示します。

## Examples

```bash
# kubeconfig ファイル内のすべてのコンテキストを一覧する
oc config get-contexts

# kubeconfig ファイル内の 1 つのコンテキストの詳細を表示する
oc config get-contexts my-context
```

## Options

- `--no-headers=false`
  デフォルトまたは custom-column の出力形式を使う場合に、ヘッダーを表示しません（デフォルトは表示）。

- `-o, --output=''`
  出力形式。(name) のみ指定できます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config get-contexts --help` / `gen-oc-help.py` で生成</sub>
