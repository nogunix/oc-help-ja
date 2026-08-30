# `oc set resources`

> Pod テンプレートを持つオブジェクトのリソース requests / limits を更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `resources`

## Usage

```
oc set resources (-f FILENAME | TYPE NAME)  ([--limits=LIMITS & --requests=REQUESTS] [options]
```

Pod テンプレートを定義する任意のリソースについて、コンピュートリソースの要件 (cpu、memory) を指定します。Pod のスケジュールに成功した場合、要求した量のリソースは保証され、指定した limits までバーストできます。

各コンピュートリソースについて、limit を指定して request を省略した場合、request のデフォルトは limit と同じ値になります。

指定できるリソース（大文字小文字を区別しません）: "ReplicationController"、"Deployment"、"DaemonSet"、"Job"、"ReplicaSet"、"DeploymentConfigs"

## Examples

```bash
# デプロイメントの nginx コンテナの CPU limits を 200m、メモリを 512Mi に設定する
oc set resources deployment nginx -c=nginx --limits=cpu=200m,memory=512Mi

# nginx のすべてのコンテナについて、リソースの requests と limits を設定する
oc set resources deployment nginx --limits=cpu=200m,memory=512Mi --requests=cpu=100m,memory=256Mi

# nginx のコンテナから、リソースの requests を削除する
oc set resources deployment nginx --limits=cpu=0,memory=0 --requests=cpu=0,memory=0

# nginx コンテナの limits をローカルで更新した結果を、サーバーに接続せずに YAML 形式で表示する
oc set resources -f path/to/file.yaml --limits=cpu=200m,memory=512Mi --local -o yaml
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-c, --containers='*'`
  変更対象とする、選択した Pod テンプレート内のコンテナ名。デフォルトではすべてのコンテナが対象です。ワイルドカードを使用できます

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--limits=''`
  このコンテナのリソース requests。例: 'cpu=100m,memory=256Mi'。なお、limit range などサーバーの設定によっては、サーバー側のコンポーネントが requests を割り当てることがあります。

- `--local=false`
  true の場合、set resources は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--requests=''`
  このコンテナのリソース requests。例: 'cpu=100m,memory=256Mi'。なお、limit range などサーバーの設定によっては、サーバー側のコンポーネントが requests を割り当てることがあります。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set resources --help` / `gen-oc-help.py` で生成</sub>
