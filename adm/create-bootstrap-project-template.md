# `oc adm create-bootstrap-project-template`

> bootstrap プロジェクトテンプレートを作成する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-bootstrap-project-template`

## Usage

```
oc adm create-bootstrap-project-template [flags] [options]
```

## Examples

```bash
# bootstrap プロジェクトテンプレートを YAML 形式で標準出力に出力する
oc adm create-bootstrap-project-template -o yaml
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--name='project-request'`
  出力するテンプレートの名前。

- `-o, --output='json'`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm create-bootstrap-project-template --help` / `gen-oc-help.py` で生成</sub>
