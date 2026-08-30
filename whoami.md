# `oc whoami`

> 現在のセッションの情報を返します。

[`oc`](oc.md) / `whoami`

## Usage

```
oc whoami [flags] [options]
```

現在のセッションの情報を表示する

このコマンドのデフォルトのオプションでは、現在認証されているユーザー名、または空文字列が返されます。他のフラグを使うと、現在使用中のトークンやユーザーコンテキストを返せます。

## Examples

```bash
# 現在認証されているユーザーを表示する
oc whoami
```

## Options

- `--show-console=false`
  true の場合、現在のサーバーの Web コンソールの URL を表示します

- `-c, --show-context=false`
  現在のユーザーコンテキスト名を表示する

- `--show-server=false`
  true の場合、現在のサーバーの REST API の URL を表示します

- `-t, --show-token=false`
  現在のセッションが使用しているトークンを表示します。別の認証方式を使用している場合はエラーになります。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc whoami --help` / `gen-oc-help.py` で生成</sub>
