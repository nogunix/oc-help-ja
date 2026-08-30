# `oc policy scc-subject-review`

> ユーザーまたはサービスアカウントが Pod を作成できるかどうかを確認する

[`oc`](../oc.md) / [`oc policy`](../policy.md) / `scc-subject-review`

## Usage

```
oc policy scc-subject-review [flags] [options]
```

ユーザー、サービスアカウント、またはグループが Pod を作成できるかどうかを確認します。そのリソースを許可する security context constraint のリストが返されます。user のみ指定して groups を指定しなかった場合は、「そのユーザーがどのグループにも属していないとしたら」という意味に解釈されます。user と groups の両方が空の場合は、現在のユーザーで確認します。

## Examples

```bash
# ユーザー bob が myresource.yaml で指定された Pod を作成できるかどうかを確認する
oc policy scc-subject-review -u bob -f myresource.yaml

# projectAdmin グループに属するユーザー bob が、myresource.yaml で指定された Pod を作成できるかどうかを確認する
oc policy scc-subject-review -u bob -g projectAdmin -f myresource.yaml

# myresourcewithsa.yaml の Pod テンプレート spec で指定されたサービスアカウントが、その Pod を作成できるかどうかを確認する
oc policy scc-subject-review -f myresourcewithsa.yaml
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-g, --groups=[]`
  グループのカンマ区切りリスト。レビューはこれらのグループの権限で実行されます

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--no-headers=false`
  デフォルトの出力形式を使う場合に、ヘッダーを表示しません（デフォルトは表示）。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-z, --serviceaccount=''`
  ユーザーとして使用する、現在の namespace 内のサービスアカウント

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `-u, --user=''`
  レビューはこのユーザーの権限で実行されます

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc policy scc-subject-review --help` / `gen-oc-help.py` で生成</sub>
