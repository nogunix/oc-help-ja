# `oc adm groups add-users`

> グループにユーザーを追加する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm groups`](../groups.md) / `add-users`

## Usage

```
oc adm groups add-users GROUP USER [USER ...] [flags] [options]
```

このコマンドは、グループのメンバー一覧に、重複しないようユーザーを追加します。

## Examples

```bash
# my-group に user1 と user2 を追加する
oc adm groups add-users my-group user1 user2
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm groups add-users --help` / `gen-oc-help.py` で生成</sub>
