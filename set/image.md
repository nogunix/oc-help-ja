# `oc set image`

> Pod テンプレートのイメージを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `image`

## Usage

```
oc set image (-f FILENAME | TYPE NAME) CONTAINER_NAME_1=CONTAINER_IMAGE_1 ... CONTAINER_NAME_N=CONTAINER_IMAGE_N [options]
```

リソースの既存のコンテナイメージを更新します。

## Examples

```bash
# デプロイメント設定の nginx コンテナのイメージを 'nginx:1.9.1' に、busybox コンテナのイメージを 'busybox' に設定する
oc set image dc/nginx busybox=busybox nginx=nginx:1.9.1

# デプロイメント設定の app コンテナのイメージを、imagestream タグ 'openshift/ruby:2.3' が参照するイメージに設定する
oc set image dc/myapp app=openshift/ruby:2.3 --source=imagestreamtag

# すべてのデプロイメントと rc の nginx コンテナのイメージを 'nginx:1.9.1' に更新する
oc set image deployments,rc nginx=nginx:1.9.1 --all

# デーモンセット abc のすべてのコンテナのイメージを 'nginx:1.9.1' に更新する
oc set image daemonset abc *=nginx:1.9.1

# ローカルファイルから nginx コンテナのイメージを更新した結果を、サーバーに接続せずに YAML 形式で表示する
oc set image -f path/to/file.yaml nginx=nginx:1.9.1 --local -o yaml
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--source='docker'`
  イメージのソースタイプ。有効な値は 'imagestreamtag'、'istag'、'imagestreamimage'、'isimage'、'docker' です

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set image --help` / `gen-oc-help.py` で生成</sub>
