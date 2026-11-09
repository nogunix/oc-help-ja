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

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-console=false`
  true の場合、現在のサーバーの Web コンソールの URL を表示します

- `-c, --show-context=false`
  現在のユーザーコンテキスト名を表示する

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--show-server=false`
  true の場合、現在のサーバーの REST API の URL を表示します

- `-t, --show-token=false`
  現在のセッションが使用しているトークンを表示します。別の認証方式を使用している場合はエラーになります。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc whoami --help` / `gen-oc-help.py` で生成</sub>
