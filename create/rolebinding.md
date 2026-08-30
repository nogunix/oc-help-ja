# `oc create rolebinding`

> 特定のロールまたはクラスタロールに対するロールバインディングを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `rolebinding`

## Usage

```
oc create rolebinding NAME --clusterrole=NAME|--role=NAME [--user=username] [--group=groupname] [--serviceaccount=namespace:serviceaccountname] [--dry-run=server|client|none] [options]
```

## Examples

```bash
# admin クラスタロールを使って、user1、user2、group1 に対するロールバインディングを作成する
oc create rolebinding admin --clusterrole=admin --user=user1 --user=user2 --group=group1

# admin ロールを使って、サービスアカウント monitoring:sa-dev に対するロールバインディングを作成する
oc create rolebinding admin-binding --role=admin --serviceaccount=monitoring:sa-dev
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--clusterrole=''`
  この RoleBinding が参照する ClusterRole

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--group=[]`
  ロールにバインドするグループ。複数のグループを追加するには、このフラグを繰り返し指定します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--role=''`
  この RoleBinding が参照する Role

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--serviceaccount=[]`
  ロールにバインドするサービスアカウント。`<namespace>`:`<name>` の形式で指定します。複数のサービスアカウントを追加するには、このフラグを繰り返し指定します。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--user=[]`
  ロールにバインドするユーザー名。複数のユーザーを追加するには、このフラグを繰り返し指定します。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create rolebinding --help` / `gen-oc-help.py` で生成</sub>
