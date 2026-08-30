# `oc adm policy scc-review`

> どのサービスアカウントが Pod を作成できるかを確認する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `scc-review`

## Usage

```
oc adm policy scc-review [flags] [options]
```

どのサービスアカウントが Pod を作成できるかを確認します。Pod は、指定したリソース内の Pod テンプレート spec から推測されます。サービスアカウントを指定しなかった場合は podTemplateSpec.spec.serviceAccountName の値が使われ、それが空の場合は "default" が使われます。サービスアカウントを指定した場合、podTemplateSpec.spec.serviceAccountName は無視されます。

## Examples

```bash
# サービスアカウント sa1 と sa2 が、my_resource.yaml で指定した Pod テンプレート spec を持つ Pod を許可できるかどうかを確認する
# myresource.yaml ファイルで指定されたサービスアカウントは無視される
oc adm policy scc-review -z sa1,sa2 -f my_resource.yaml

# サービスアカウント system:serviceaccount:bob:default が、my_resource.yaml で指定した Pod テンプレート spec を持つ Pod を許可できるかどうかを確認する
oc adm policy scc-review -z system:serviceaccount:bob:default -f my_resource.yaml

# my_resource_with_sa.yaml で指定されたサービスアカウントが、その Pod を許可できるかどうかを確認する
oc adm policy scc-review -f my_resource_with_sa.yaml

# デフォルトのサービスアカウントがその Pod を許可できるかどうかを確認する。myresource_with_no_sa.yaml にサービスアカウントの定義がないため default が使われる
oc adm policy scc-review -f myresource_with_no_sa.yaml
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--no-headers=false`
  デフォルトの出力形式を使う場合に、ヘッダーを表示しません（デフォルトは表示）。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-z, --serviceaccount=[]`
  ユーザーとして使用する、現在の namespace 内のサービスアカウント

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm policy scc-review --help` / `gen-oc-help.py` で生成</sub>
