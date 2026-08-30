# `oc set deployment-hook`

> デプロイメント設定のデプロイメントフックを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `deployment-hook`

## Usage

```
oc set deployment-hook DEPLOYMENTCONFIG --pre|--post|--mid -- CMD [flags] [options]
```

デプロイメント設定のデプロイメントフックを設定または削除します。

デプロイメント設定では、デプロイメントストラテジーに応じて、デプロイのライフサイクルの各時点でフックを実行できます。

Recreate ストラテジーのデプロイでは、Pre・Mid・Post のフックを指定できます。Pre フックはデプロイ開始前に実行されます。Mid フックは、以前のデプロイが 0 までスケールダウンされた後、新しいデプロイが立ち上がる前に実行されます。Post フックはデプロイ完了後に実行されます。

Rolling ストラテジーのデプロイでは、Pre と Post のフックを指定できます。Pre フックはデプロイ開始前に、Post フックはデプロイ完了後に実行されます。

各フックでは、デプロイメントの Pod テンプレートに含まれるコンテナのいずれかを使い、指定したコマンドを実行する新しい Pod が起動されます。フック用の追加の環境変数や、Pod テンプレートのどのボリュームをフック用 Pod にマウントするかも指定できます。

各フックは独自のキャンセルポリシーを持てます。abort、retry、ignore のいずれかです。すべてのフックですべてのキャンセルポリシーを設定できるわけではありません。たとえば rolling ストラテジーの Post フックでは、その時点で既にデプロイが完了しているため abort ポリシーはサポートされません。

## Examples

```bash
# デプロイメント設定の pre / post フックを削除する
oc set deployment-hook dc/myapp --remove --pre --post

# アプリケーションの DB マイグレーションコマンドを実行する pre デプロイメントフックを設定する
# アプリケーションのデータボリュームを使って
oc set deployment-hook dc/myapp --pre --volumes=data -- /var/lib/migrate-db.sh

# 追加の環境変数とともに mid デプロイメントフックを設定する
oc set deployment-hook dc/myapp --mid --volumes=data -e VAR1=value1 -e VAR2=value2 -- /var/lib/prepare-deploy.sh
```

## Options

- `--all=false`
  true の場合、namespace 内のすべてのデプロイメント設定を選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-c, --container=''`
  デプロイメントフックに使用する、選択したデプロイメント設定内のコンテナ名

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-e, --environment=[]`
  デプロイメントフックの Pod で使用する環境変数

- `--failure-policy='ignore'`
  デプロイメントフックの失敗時ポリシー。有効な値: abort、retry、ignore

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set deployment hook は API サーバーに接続せずローカルで実行します。

- `--mid=false`
  mid デプロイメントフックを設定または削除する

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--post=false`
  post デプロイメントフックを設定または削除する

- `--pre=false`
  pre デプロイメントフックを設定または削除する

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove=false`
  true の場合、指定したデプロイメントフックを削除します。

- `-l, --selector=''`
  デプロイメント設定を絞り込むためのセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--volumes=[]`
  デプロイメントフックの Pod で使用する、Pod テンプレート由来のボリューム

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set deployment-hook --help` / `gen-oc-help.py` で生成</sub>
