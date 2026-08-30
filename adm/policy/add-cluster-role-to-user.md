# `oc adm policy add-cluster-role-to-user`

> クラスタ内のすべてのプロジェクトを対象に、ユーザーにロールを付与する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-cluster-role-to-user`

## Usage

```
oc adm policy add-cluster-role-to-user ROLE (USER | -z serviceaccount) [user]... [flags] [options]
```

すべてのプロジェクトを対象に、ユーザーまたはサービスアカウントにロールを付与する

このコマンドを使うと、ユーザーをロールに割り当てることで、クラスタ内の特定のリソースと操作へのアクセス権を付与できます。指定したクラスタロールを参照するクラスタロールバインディングを作成または変更し、対象のユーザーやサービスアカウントをサブジェクトの一覧に追加します。このコマンドは、対応するクラスタロールやユーザー / サービスアカウントのリソースが存在することを必須とせず、それらが存在しない場合や、ユーザーにそれらを参照する権限がない場合でも、バインディングの作成に成功します。

--rolebinding-name 引数を指定した場合、その名前の既存クラスタロールバインディングを探します。一致したクラスタロールバインディングのロールは、コマンドに指定したロール名と一致している必要があります。ロールバインディング名を指定しない場合は、デフォルトの名前が使用されます。

詳しくは RBAC とポリシーに関する情報を参照するか、次のリソースに対して 'get' および 'describe' コマンドを使用してください: 'clusterroles'、'clusterrolebindings'、'roles'、'rolebindings'、'users'、'groups'、'serviceaccounts'。

## Examples

```bash
# 'devuser' ユーザーに 'system:build-strategy-docker' クラスタロールを付与する
oc adm policy add-cluster-role-to-user system:build-strategy-docker devuser
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

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

<sub>`$ oc adm policy add-cluster-role-to-user --help` / `gen-oc-help.py` で生成</sub>
