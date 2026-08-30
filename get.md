# `oc get`

> 1 つまたは複数のリソースを表示する

[`oc`](oc.md) / `get`

## Usage

```
oc get [(-o|--output=)json|yaml|kyaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file|custom-columns|custom-columns-file|wide] (TYPE[.VERSION][.GROUP] [NAME | -l label] | TYPE[.VERSION][.GROUP]/NAME ...) [flags] [options]
```

指定したリソースに関する重要な情報を表形式で表示します。--selector フラグでラベルセレクターを指定して一覧を絞り込めます。対象のリソースタイプが namespace スコープの場合、namespace を指定しなければ現在の namespace の結果のみが表示されます。

出力に 'template' を指定し、--template フラグの値として Go テンプレートを渡すと、取得したリソースの属性を絞り込めます。

サポートされているリソースの完全な一覧は "oc api-resources" で確認できます。

## Examples

```bash
# すべての Pod を ps 形式で一覧する
oc get pods

# すべての Pod を、より多くの情報（ノード名など）付きで ps 形式で一覧する
oc get pods -o wide

# 指定した NAME のレプリケーションコントローラー 1 つを ps 形式で一覧する
oc get replicationcontroller web

# "apps" API グループの "v1" バージョンで、デプロイメントを JSON 形式で一覧する
oc get deployments.v1.apps -o json

# 単一の Pod を JSON 形式で一覧する
oc get -o json pod web-pod-13je7

# "pod.yaml" で指定された type と name の Pod を JSON 形式で一覧する
oc get -f pod.yaml -o json

# kustomization.yaml を含むディレクトリからリソースを一覧する（例: dir/kustomization.yaml）
oc get -k dir/

# 指定した Pod の phase の値だけを返す
oc get -o template pod/web-pod-13je7 --template={{.status.phase}}

# リソース情報をカスタム列で一覧する
oc get pod test-pod -o custom-columns=CONTAINER:.spec.containers[0].name,IMAGE:.spec.containers[0].image

# すべてのレプリケーションコントローラーと Service をまとめて ps 形式で一覧する
oc get rc,services

# type と名前を指定して 1 つ以上のリソースを一覧する
oc get rc/web service/frontend pods/web-pod-13je7

# 単一の Pod の 'status' サブリソースを一覧する
oc get pod web-pod-13je7 --subresource status

# namespace 'backend' 内のすべてのデプロイメントを一覧する
oc get deployments.apps --namespace backend

# 全 namespace に存在するすべての Pod を一覧する
oc get pods --all-namespaces
```

## Options

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--chunk-size=500`
  大きなリストを一度に返さず、チャンクに分けて返します。0 を指定すると無効になります。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `--ignore-not-found=false`
  true に設定した場合、存在しない特定のオブジェクトについて NotFound エラーを抑制します。リソースのコレクションを問い合わせるコマンドでこのフラグを使っても、リソースが見つからない場合には効果はありません。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-L, --label-columns=[]`
  列として表示するラベルをカンマ区切りのリストで受け取ります。名前は大文字小文字を区別します。-L label1 -L label2... のようにフラグを複数回指定することもできます。

- `--no-headers=false`
  デフォルトまたは custom-column の出力形式を使う場合に、ヘッダーを表示しません（デフォルトは表示）。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file, custom-columns, custom-columns-file, wide)。カスタム列 [https://kubernetes.io/docs/reference/kubectl/#custom-columns]、golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview]、jsonpath テンプレート [https://kubernetes.io/docs/reference/kubectl/jsonpath/] を参照してください。

- `--output-watch-events=false`
  --watch または --watch-only を使用した場合に、watch イベントのオブジェクトを出力します。既存のオブジェクトは、最初の ADDED イベントとして出力されます。

- `--raw=''`
  サーバーにリクエストする生の URI。kubeconfig ファイルで指定されたトランスポートを使用します。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--server-print=true`
  true の場合、サーバーに適切なテーブル形式の出力を返させます。拡張 API と CRD をサポートします。

- `--show-kind=false`
  指定した場合、要求されたオブジェクトのリソースタイプを表示します。

- `--show-labels=false`
  出力時に、すべてのラベルを最後の列として表示します（デフォルトはラベル列を非表示）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--sort-by=''`
  空でない場合、指定したフィールド指定で一覧をソートします。フィールド指定は JSONPath 式で記述します（例: '{.metadata.name}'）。この JSONPath 式が指す API リソースのフィールドは、整数または文字列である必要があります。

- `--subresource=''`
  指定した場合、対象オブジェクトのサブリソースを取得します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `-w, --watch=false`
  指定したオブジェクトを一覧 / 取得した後、変更を監視し続けます。

- `--watch-only=false`
  最初の一覧 / 取得を行わずに、対象オブジェクトの変更を監視します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc get --help` / `gen-oc-help.py` で生成</sub>
