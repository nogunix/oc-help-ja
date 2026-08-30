# `oc proxy`

> Kubernetes API サーバーへのプロキシを実行する

[`oc`](oc.md) / `proxy`

## Usage

```
oc proxy [--port=PORT] [--www=static-dir] [--www-prefix=prefix] [--api-prefix=prefix] [options]
```

localhost と Kubernetes API サーバーの間に、プロキシサーバーまたはアプリケーションレベルのゲートウェイを作成します。指定した HTTP パスで静的コンテンツを配信することもできます。受信データはすべて 1 つのポートから入り、静的コンテンツのパスに一致する場合を除き、リモートの Kubernetes API サーバーのポートへ転送されます。

## Examples

```bash
# Kubernetes API のみをプロキシする
oc proxy --api-prefix=/

# Kubernetes API の一部と、いくつかの静的ファイルをプロキシする
# Pod の情報は 'curl localhost:8001/api/v1/pods' で取得できます
oc proxy --www=/my/files --www-prefix=/static/ --api-prefix=/api/

# Kubernetes API 全体を別のルートパスでプロキシする
# Pod の情報は 'curl localhost:8001/custom/api/v1/pods' で取得できます
oc proxy --api-prefix=/custom/

# ポート 8011 で Kubernetes API サーバーへのプロキシを実行し、./local/www/ から静的コンテンツを配信する
oc proxy --port=8011 --www=./local/www/

# 任意のローカルポートで Kubernetes API サーバーへのプロキシを実行する
# サーバーが選択したポートは標準出力に表示されます
oc proxy --port=0

# API のプレフィックスを k8s-api に変更して、Kubernetes API サーバーへのプロキシを実行する
# これにより、たとえば Pod の API が localhost:8001/k8s-api/v1/pods/ で利用できるようになります
oc proxy --api-prefix=/k8s-api
```

## Options

- `--accept-hosts='^localhost$,^127\.0\.0\.1$,^\[::1\]$'`
  プロキシが受け付けるべきホストの正規表現。

- `--accept-paths='^.*'`
  プロキシが受け付けるべきパスの正規表現。

- `--address='127.0.0.1'`
  待ち受ける IP アドレス。

- `--api-prefix='/'`
  プロキシした API を配信するパスのプレフィックス。

- `--append-server-path=false`
  true の場合、各リクエストに kube コンテキストのサーバーパスを自動的に付加します。

- `--disable-filter=false`
  true の場合、プロキシのリクエストフィルタリングを無効にします。これは危険であり、外部からアクセス可能なポートで使用すると XSRF 攻撃に対して脆弱になります。

- `--keepalive=0s`
  keepalive は、アクティブなネットワーク接続の keep-alive 間隔を指定します。0 に設定すると keepalive を無効にします。

- `-p, --port=8001`
  プロキシを実行するポート。0 を指定するとランダムなポートが選ばれます。

- `--reject-methods='^$'`
  プロキシが拒否すべき HTTP メソッドの正規表現（例: --reject-methods='POST,PUT,PATCH'）。

- `--reject-paths='^/api/.*/pods/.*/exec,^/api/.*/pods/.*/attach'`
  プロキシが拒否すべきパスの正規表現。ここで指定したパスは、--accept-paths で許可されていても拒否されます。

- `-u, --unix-socket=''`
  プロキシを実行する Unix ソケット。

- `-w, --www=''`
  指定したプレフィックスの下で、指定ディレクトリの静的ファイルも配信します。

- `-P, --www-prefix='/static/'`
  静的ファイルのディレクトリを指定した場合に、それを配信するパスのプレフィックス。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc proxy --help` / `gen-oc-help.py` で生成</sub>
