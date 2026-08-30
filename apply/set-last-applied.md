# `oc apply set-last-applied`

> 稼働中のオブジェクトの last-applied-configuration アノテーションを、ファイルの内容に合わせて設定する

[`oc`](../oc.md) / [`oc apply`](../apply.md) / `set-last-applied`

## Usage

```
oc apply set-last-applied -f FILENAME [options]
```

最新の last-applied-configuration アノテーションを、ファイルの内容に合わせて設定します。これにより、オブジェクトの他の部分は更新せずに、'oc apply -f`<file>` ' を実行したときと同じように last-applied-configuration だけが更新されます。

## Examples

```bash
# リソースの last-applied-configuration を、ファイルの内容に合わせて設定する
oc apply set-last-applied -f deploy.yaml

# ディレクトリ内の各設定ファイルに対して set-last-applied を実行する
oc apply set-last-applied -f path/

# リソースの last-applied-configuration を、ファイルの内容に合わせて設定する。アノテーションが存在しない場合は作成する
oc apply set-last-applied -f deploy.yaml --create-annotation=true
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--create-annotation=false`
  現在のオブジェクトが 'last-applied-configuration' アノテーションを持っていない場合は作成します

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-f, --filename=[]`
  last-applied-configuration アノテーションを含むファイル名、ディレクトリ、または URL

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc apply set-last-applied --help` / `gen-oc-help.py` で生成</sub>
