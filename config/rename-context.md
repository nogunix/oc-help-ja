# `oc config rename-context`

> kubeconfig ファイルのコンテキスト名を変更する

[`oc`](../oc.md) / [`oc config`](../config.md) / `rename-context`

## Usage

```
oc config rename-context CONTEXT_NAME NEW_NAME [options]
```

kubeconfig ファイルのコンテキスト名を変更します。

CONTEXT_NAME は変更したいコンテキストの名前です。

NEW_NAME は設定したい新しい名前です。

注: 名前を変更するコンテキストが 'current-context' の場合、そのフィールドも更新されます。

## Examples

```bash
# kubeconfig ファイル内のコンテキスト 'old-name' を 'new-name' に変更する
oc config rename-context old-name new-name
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config rename-context --help` / `gen-oc-help.py` で生成</sub>
