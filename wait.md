# `oc wait`

> 1 つ以上のリソースが特定の条件を満たすまで待機する

[`oc`](oc.md) / `wait`

## Usage

```
oc wait ([-f FILENAME] | resource.group/resource.name | resource.group [(-l label | --all)]) [--for=create|--for=delete|--for condition=available|--for=jsonpath='{}'[=value]] [options]
```

このコマンドは複数のリソースを受け取り、指定した条件がそれぞれのリソースの Status フィールドに現れるまで待機します。

また、--for フラグの値として "create" または "delete" キーワードを指定することで、指定したリソース群が作成される / 削除されるまで待つこともできます。

指定した条件が満たされると、成功メッセージが標準出力に出力されます。-o オプションで出力先を変更できます。

## Examples

```bash
# Pod "busybox1" のステータス条件に "Ready" タイプが含まれるまで待つ
oc wait --for=condition=Ready pod/busybox1

# status 条件のデフォルト値は true です。等号の後に別の値を書くと、その値になるまで待機できます（比較には Unicode の simple case folding、より一般的な大文字小文字の同一視が適用されます）
oc wait --for=condition=Ready=false pod/busybox1

# Pod "busybox1" のステータス phase が "Running" になるまで待つ
oc wait --for=jsonpath='{.status.phase}'=Running pod/busybox1

# Pod "busybox1" が Ready になるまで待つ
oc wait --for='jsonpath={.status.conditions[?(@.type=="Ready")].status}=True' pod/busybox1

# Service "loadbalancer" が ingress を持つまで待つ
oc wait --for=jsonpath='{.status.loadBalancer.ingress}' service/loadbalancer

# シークレット "busybox1" が作成されるまで、タイムアウト 30 秒で待つ
oc create secret generic busybox1
oc wait --for=create secret/busybox1 --timeout=30s

# "delete" コマンドの実行後、Pod "busybox1" が削除されるまで、タイムアウト 60 秒で待つ
oc delete pod/busybox1
oc wait --for=delete pod/busybox1 --timeout=60s
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  リソースを特定する。

- `--for=''`
  待機する条件: [create|delete|condition=condition-name[=condition-value]|jsonpath='{JSONPath expression}'=[JSONPath value]]。condition-value のデフォルトは true です。条件値は Unicode の simple case folding（より一般的な大文字小文字の同一視）を適用してから比較されます。

- `--local=false`
  true の場合、annotation は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=true`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!=' をサポートします（例: -l key1=value1,key2=value2）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--timeout=30s`
  諦めるまでの待ち時間。0 は 1 回だけ確認して待たないこと、負の値は 1 週間待つことを意味します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc wait --help` / `gen-oc-help.py` で生成</sub>
