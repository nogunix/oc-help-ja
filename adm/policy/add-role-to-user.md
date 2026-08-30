# `oc adm policy add-role-to-user`

> 現在のプロジェクトを対象に、ユーザーまたはサービスアカウントにロールを付与する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-role-to-user`

## Usage

```
oc adm policy add-role-to-user ROLE (USER | -z SERVICEACCOUNT) [USER ...] [flags] [options]
```

プロジェクトを対象に、ユーザーまたはサービスアカウントにロールを付与します。

このコマンドを使うと、ユーザーをロールに割り当てることで、現在のプロジェクト内の特定のリソースと操作へのアクセス権を付与できます。指定したロールを参照するロールバインディングを作成または変更し、対象のユーザーやサービスアカウントをサブジェクトの一覧に追加します。このコマンドは、対応するロールやユーザー / サービスアカウントのリソースが存在することを必須とせず、それらが存在しない場合や、ユーザーにそれらを参照する権限がない場合でも、バインディングの作成に成功します。

--rolebinding-name 引数を指定した場合、その名前の既存ロールバインディングを探します。一致したロールバインディングのロールは、コマンドに指定したロール名と一致している必要があります。ロールバインディング名を指定しない場合は、デフォルトの名前が使用されます。--role-namespace 引数に空でない値を指定した場合、それは現在の namespace と一致している必要があります。role-namespace を指定した場合、ロールバインディングは namespace スコープのロールを参照します。指定しない場合は、クラスタロールのリソースを参照します。

詳しくは RBAC とポリシーに関する情報を参照するか、次のリソースに対して 'get' および 'describe' コマンドを使用してください: 'clusterroles'、'clusterrolebindings'、'roles'、'rolebindings'、'users'、'groups'、'serviceaccounts'。

## Examples

```bash
# 現在のプロジェクトを対象に、user1 に 'view' ロールを付与する
oc adm policy add-role-to-user view user1

# 現在のプロジェクトを対象に、serviceaccount1 に 'edit' ロールを付与する
oc adm policy add-role-to-user edit -z serviceaccount1
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--role-namespace=''`
  ロールが定義されている namespace。空の場合は、クラスタポリシーで定義されたロールを意味します

- `--rolebinding-name=''`
  変更または作成するロールバインディングの名前。空のままにすると、デフォルトの名前で新しいロールバインディングを作成します

- `-z, --serviceaccount=[]`
  ユーザーとして使用する、現在の namespace 内のサービスアカウント

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm policy add-role-to-user --help` / `gen-oc-help.py` で生成</sub>
