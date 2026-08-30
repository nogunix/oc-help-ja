# `oc expose`

> 複製されたアプリケーションを Service または Route として公開する

[`oc`](oc.md) / `expose`

## Usage

```
oc expose (-f FILENAME | TYPE NAME) [--port=port] [--protocol=TCP|UDP|SCTP] [--target-port=number-or-name] [--name=name] [--external-ip=external-ip-of-service] [--type=type] [flags] [options]
```

コンテナを Service として内部に、または Route を通じて外部に公開します。

デプロイメント設定、レプリケーションコントローラー、Service、Pod を、指定したポートで新しい Service として公開することもできます。ラベルを指定しない場合、新しいオブジェクトは公開元のオブジェクトのラベルを再利用します。

## Examples

```bash
# nginx サービスを基にルートを作成する。新しいルートは nginx のラベルを再利用する
oc expose service nginx

# 独自のラベルとルート名を指定してルートを作成する
oc expose service nginx -l name=myroute --name=fromdowntown

# ホスト名を指定してルートを作成する
oc expose service nginx --hostname=www.example.com

# ワイルドカード付きのルートを作成する
oc expose service nginx --hostname=x.example.com --wildcard-policy=Subdomain
# これは *.example.com と同等になります。注: ワイルドカードが一致するのはホストのみで、サブドメインは含まれません

# デプロイメント設定を Service として公開し、指定したポートを使用する
oc expose dc ruby-hello-world --port=8080

# 指定したパスで Service を Route として公開する
oc expose service nginx --path=/nginx
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--cluster-ip=''`
  Service に割り当てる ClusterIP。空にすると自動割り当て、'None' にすると headless Service を作成します。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--external-ip=''`
  Service で受け付ける追加の外部 IP アドレス（Kubernetes の管理対象外）。この IP がノードにルーティングされていれば、自動生成された Service IP に加えて、この IP でも Service にアクセスできます。

- `--field-manager='kubectl-expose'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  Service として公開するリソースを特定するファイル名、ディレクトリ、または URL

- `--hostname=''`
  新しいルートにホスト名を設定する

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-l, --labels=''`
  この呼び出しで作成される Service に適用するラベル。

- `--load-balancer-ip=''`
  LoadBalancer に割り当てる IP。空の場合は一時的な IP が作成されて使用されます（クラウドプロバイダ依存）。

- `--name=''`
  新しく作成するオブジェクトの名前。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--override-type='merge'`
  生成されたオブジェクトの上書きに使用する方式: json、merge、strategic のいずれか。

- `--overrides=''`
  生成されるオブジェクトを上書きするインライン JSON。空でない場合、生成されたオブジェクトの内容を上書きします。オブジェクトが有効な apiVersion フィールドを持つ必要があります。

- `--path=''`
  新しいルートにパスを設定する

- `--port=''`
  Service が提供するポート。指定しない場合は、公開対象のリソースからコピーされます

- `--protocol=''`
  作成する Service のネットワークプロトコル。デフォルトは 'TCP' です。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--selector=''`
  この Service に使用するラベルセレクター。等価ベースのセレクター要件のみサポートされます。空（デフォルト）の場合、公開対象のリソースからセレクターを推測します。

- `--session-affinity=''`
  空でない場合、Service のセッションアフィニティをこの値に設定します。指定できる値: 'None'、'ClientIP'

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--target-port=''`
  Service がトラフィックを転送する先の、コンテナ上のポートの名前または番号。省略可能です。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--type=''`
  この Service のタイプ: ClusterIP、NodePort、LoadBalancer、ExternalName のいずれか。デフォルトは 'ClusterIP' です。

- `--wildcard-policy=''`
  ホスト名の WildcardPolicy を設定します。デフォルトは "None" です。有効な値は "None" と "Subdomain" です

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc expose --help` / `gen-oc-help.py` で生成</sub>
