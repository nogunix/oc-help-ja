# `oc create clusterrole`

> クラスタロールを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `clusterrole`

## Usage

```
oc create clusterrole NAME --verb=verb --resource=resource.group [--resource-name=resourcename] [--dry-run=server|client|none] [options]
```

## Examples

```bash
# Pod に対する "get"、"watch"、"list" を許可する "pod-reader" という名前のクラスタロールを作成する
oc create clusterrole pod-reader --verb=get,list,watch --resource=pods

# ResourceName を指定して "pod-reader" という名前のクラスタロールを作成する
oc create clusterrole pod-reader --verb=get --resource=pods --resource-name=readablepod --resource-name=anotherpod

# API Group を指定して "foo" という名前のクラスタロールを作成する
oc create clusterrole foo --verb=get,list,watch --resource=rs.apps

# SubResource を指定して "foo" という名前のクラスタロールを作成する
oc create clusterrole foo --verb=get,list,watch --resource=pods,pods/status

# NonResourceURL を指定して "foo" という名前のクラスタロールを作成する
oc create clusterrole "foo" --verb=get --non-resource-url=/logs/*

# AggregationRule を指定して "monitoring" という名前のクラスタロールを作成する
oc create clusterrole monitoring --aggregation-rule="rbac.example.com/aggregate-to-monitoring=true"
```

## Options

- `--aggregation-rule=`
  ClusterRole を組み合わせるための集約ラベルセレクター。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--non-resource-url=[]`
  ユーザーがアクセスできるべき部分 URL。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--resource=[]`
  このルールを適用するリソース

- `--resource-name=[]`
  このルールを適用する、許可リスト内のリソース。複数指定するには、このフラグを繰り返し指定します

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--verb=[]`
  このルール内のリソースに適用する verb

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create clusterrole --help` / `gen-oc-help.py` で生成</sub>
