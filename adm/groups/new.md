# `oc adm groups new`

> 新しいグループを作成する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm groups`](../groups.md) / `new`

## Usage

```
oc adm groups new GROUP [USER ...] [flags] [options]
```

このコマンドは、任意でユーザーの一覧を指定して、新しいグループを作成します。

## Examples

```bash
# ユーザーを含まないグループを追加する
oc adm groups new my-group

# ユーザーを 2 人含むグループを追加する
oc adm groups new my-group user1 user2

# ユーザーを 1 人含むグループを追加し、出力を簡潔にする
oc adm groups new my-group user1 -o name
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

<sub>`$ oc adm groups new --help` / `gen-oc-help.py` で生成</sub>
