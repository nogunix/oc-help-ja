# `oc policy who-can`

> あるリソースに対して指定した操作を実行できるのは誰かを一覧する

[`oc`](../oc.md) / [`oc policy`](../policy.md) / `who-can`

## Usage

```
oc policy who-can VERB RESOURCE [NAME] [flags] [options]
```

## Options

- `-A, --all-namespaces=false`
  true の場合、すべての namespace について、指定した操作を実行できるのは誰かを一覧します。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--subresource=''`
  log や scale などのサブリソース

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc policy who-can --help` / `gen-oc-help.py` で生成</sub>
