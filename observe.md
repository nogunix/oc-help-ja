# `oc observe`

> リソースの変更を監視して反応する（実験的機能）

[`oc`](oc.md) / `observe`

## Usage

```
oc observe RESOURCE [-- COMMAND ...] [flags] [options]
```

リソースの変更を監視し、それに応じた処理を実行します。

このコマンドは、Kubernetes や OpenShift のリソースに発生した変更に対する、スクリプトによる反応を組み立てるのを支援します。これは Kubernetes ではしばしば 'コントローラー' と呼ばれ、特定の条件が維持されるように働きます。起動時、observe は特定のタイプのリソースをすべて一覧し、それぞれに対して指定されたスクリプトを実行します。その後もサーバーの変更を監視し、更新のたびにスクリプトを再実行します。

observe は「すべてのリソース X について、Y が成り立つようにする」という形の問題に最も適しています。observe の使い方の例をいくつか挙げます:

- すべての namespace にクォータまたは limit range オブジェクトがあることを確認する
- DNS API を呼び出して、すべての Service が DNS に登録されていることを確認する
- ノードが 'NotReady' を報告するたびにメール通知を送る
- 'FailedScheduling' イベントを監視し、IRC にメッセージを書き込む
- 新しい PVC が作成されたときに永続ボリュームを動的にプロビジョニングする
- 一定時間が経過した、正常に完了済みの Pod を削除する
最も単純なパターンは、オブジェクトに対する不変条件の維持です。たとえば「すべての namespace は、その所有者を示すアノテーションを持つべきである」といったものです。オブジェクトが削除された場合、何もする必要はありません。このパターンの変形として、別のオブジェクトを作成するものもあります。「すべての namespace は、その所有者に許可されたリソースに基づくクォータオブジェクトを持つべきである」といった具合です。

        $ cat set_owner.sh
        #!/bin/sh
        if [[ "$(oc get namespace "$1" --template='{{ .metadata.annotations.owner }}')" == "" ]]; then
        oc annotate namespace "$1" owner=bob
        fi
        $ oc observe namespaces -- ./set_owner.sh
set_owner.sh スクリプトは、各 namespace に対して 1 つの引数（namespace 名）とともに呼び出されます。この簡単なスクリプトは、"owner" アノテーションを持たないユーザーにそれを設定しつつ、既存の値はそのまま保持します。

コントローラーパターンのもう 1 つのよくある形がプロビジョニングです。これは、Kubernetes リソースの状態に合わせて外部システムを変更するというものです。この種のスクリプトでは、observe コマンドが動いていない間に発生した削除も考慮する必要があります。既知のオブジェクトの一覧は --names コマンドで渡せます。このコマンドは、名前または namespace/name のペアを改行区切りで返す必要があります。指定したコマンドは、observe がサーバー上の最新状態を確認するたびに呼び出されます。--names が返したもののうち、サーバー上に存在しないリソースは --delete のコマンドに渡されます。

たとえば、Kubernetes に追加されたすべてのノードを、その IP とともにクラスタのインベントリに追加したい場合は次のようにします:

        $ cat add_to_inventory.sh
        #!/bin/sh
        echo "$1 $2" >> inventory
        sort -u inventory -o inventory
        $ cat remove_from_inventory.sh
        #!/bin/sh
        grep -vE "^$1 " inventory > /tmp/newinventory
        mv -f /tmp/newinventory inventory
        $ cat known_nodes.sh
        #!/bin/sh
        touch inventory
        cut -f 1-1 -d ' ' inventory
        $ oc observe nodes --template '{ .status.addresses[0].address }' \
        --names ./known_nodes.sh \
        --delete ./remove_from_inventory.sh \
        -- ./add_to_inventory.sh
observe コマンドを停止してからノードを削除した場合、次に observe を起動したときに inventory の内容とサーバー上のノード一覧が比較され、既に存在しない inventory 内のノードについては、そのノード名を引数として remove_from_inventory.sh が呼び出されます。

重要: 削除を処理する場合、そのオブジェクトの以前の状態は取得できないことがあり、--delete で指定したコマンドにはオブジェクトの名前 / namespace のみが引数として渡されます（カスタム引数はすべて省略されます）。

より複雑な連携も、上の 2 つの例を土台に組み立てられます。たとえば inventory スクリプトから IaaS 上のストレージを確保したり、ノード名を DNS に登録したり、複雑なファイアウォールを設定したりできます。連携が複雑になるほど、どちらか一方のリソースが削除されたことを判別できるだけのデータを、リモート側に十分記録しておくことが重要になります。

## Examples

```bash
# Service の変更を監視する
oc observe services

# clusterIP を含めて Service の変更を監視し、変更ごとにスクリプトを呼び出す
oc observe services --template '{ .spec.clusterIP }' -- register_dns.sh

# ラベルセレクターで絞り込んだ Service の変更を監視する
oc observe services -l regist-dns=true --template '{ .spec.clusterIP }' -- register_dns.sh
```

## Options

- `-A, --all-namespaces=false`
  true の場合、すべてのプロジェクトを対象に、要求されたオブジェクトを一覧します。現在のコンテキストのプロジェクトは無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-d, --delete=''`
  リソースが削除されたときに実行するコマンド。複数回指定すると引数を追加できます。

- `--exit-after=0s`
  指定した時間が経過したら終了コード 0 で終了します（省略可）。

- `--listen-addr=':11251'`
  メトリクスとヘルスチェックを公開するために待ち受けるインターフェースの名前。

- `--maximum-errors=20`
  この数だけエラーを検出したら終了します。-1 を指定すると上限なしになります。

- `--names=''`
  現在判明しているすべての名前を一覧するコマンド（省略可）。複数回指定すると引数を追加できます。オブジェクトが削除されたときに通知を受け取るために使用します。

- `--object-env-var=''`
  コマンド呼び出し時に、オブジェクトをシリアライズして格納する環境変数の名前（省略可）。

- `--once=false`
  true の場合、現在のオブジェクトをすべて処理し終えた時点で終了コード 0 で終了します。

- `-o, --output='jsonpath'`
  出力形式。次のいずれかを指定します: (go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--print-metrics-on-exit=false`
  true の場合、終了時にすべてのメトリクスを標準出力に書き出します。

- `-q, --quiet=false`
  true の場合、コマンド実行前に各イベントの情報を表示しません。

- `--resync-period=0s`
  0 以外を指定した場合、サーバー上のすべての項目を定期的に Sync イベントとして再処理します。外部システムを最新の状態に保つために使用します。

- `--retry-count=2`
  処理を続行する前に、失敗したコマンドを再試行する回数。

- `--retry-on-exit-code=0`
  いずれかのコマンドがこの終了コードを返した場合、--retry-count の回数まで再試行します。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!=' をサポートします（例: -l key1=value1,key2=value2）

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--type-env-var=''`
  受信したイベントの種類 ('Sync'、'Updated'、'Deleted'、'Added') を、リアクションコマンドまたは --delete に渡す環境変数の名前。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc observe --help` / `gen-oc-help.py` で生成</sub>
