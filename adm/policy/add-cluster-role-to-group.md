# `oc adm policy add-cluster-role-to-group`

> クラスタ内のすべてのプロジェクトを対象に、グループにロールを付与する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-cluster-role-to-group`

## Usage

```
oc adm policy add-cluster-role-to-group ROLE GROUP [GROUP...] [flags] [options]
```

プロジェクトを対象に、グループにロールを付与する

このコマンドは、指定した名前のクラスタロールを持つクラスタロールバインディングを作成または変更し、指定したグループをサブジェクトの一覧に追加します。このコマンドは、対応するロールやグループのリソースが存在することを必須とせず、それらが存在しない場合や、ユーザーにそれらを参照する権限がない場合でも、バインディングの作成に成功します。

--rolebinding-name 引数を指定した場合、その名前の既存クラスタロールバインディングを探します。一致したクラスタロールバインディングのロールは、コマンドに指定したロール名と一致している必要があります。rolebinding 名を指定しない場合は、デフォルトの名前が使用されます。

## Examples

```bash
# 'cluster-admins' グループに 'cluster-admin' クラスタロールを付与する
oc adm policy add-cluster-role-to-group cluster-admin cluster-admins
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

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm policy add-cluster-role-to-group --help` / `gen-oc-help.py` で生成</sub>
