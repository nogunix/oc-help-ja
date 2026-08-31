# `oc adm inspect`

> 指定したリソースのデバッグ用データを収集する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `inspect`

## Usage

```
oc adm inspect (TYPE[.VERSION][.GROUP] [NAME] | TYPE[.VERSION][.GROUP]/NAME ...) [flags] [options]
```

指定したリソースのデバッグ用データを収集します。

このコマンドは、デバッグ情報を収集する目的で、指定したリソースと関連するリソースをダウンロードします。

## Examples

```bash
# "openshift-apiserver" clusteroperator のデバッグ用データを収集する
oc adm inspect clusteroperator/openshift-apiserver

# "openshift-apiserver" と "kube-apiserver" の clusteroperator のデバッグ用データを収集する
oc adm inspect clusteroperator/openshift-apiserver clusteroperator/kube-apiserver

# すべての clusteroperator のデバッグ用データを収集する
oc adm inspect clusteroperator

# すべての clusteroperator と clusterversion のデバッグ用データを収集する
oc adm inspect clusteroperators,clusterversions
```

## Options

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--as=''`
  この操作で偽装するユーザー名。通常のユーザーのほか、namespace 内のサービスアカウントも指定できます。

- `--as-group=[]`
  この操作で偽装するグループ。複数のグループを指定するには、このフラグを繰り返し指定します。

- `--as-uid=''`
  この操作で偽装する UID。

- `--as-user-extra=[]`
  この操作で偽装するユーザーの extra 情報。同じキーに複数の値を指定するには、このフラグを繰り返し指定します。

- `--cache-dir='/Users/mnoguchi/.kube/cache'`
  デフォルトのキャッシュディレクトリ

- `--certificate-authority=''`
  認証局の証明書ファイルのパス

- `--client-certificate=''`
  TLS 用クライアント証明書ファイルのパス

- `--client-key=''`
  TLS 用クライアント鍵ファイルのパス

- `--cluster=''`
  使用する kubeconfig のクラスタ名

- `--context=''`
  使用する kubeconfig のコンテキスト名

- `--dest-dir=''`
  収集したクラスタオペレータのデータをすべて保存するルートディレクトリ。デフォルトは $(PWD)/inspect.local.`<rand>` です

- `--disable-compression=false`
  true の場合、サーバーへのすべてのリクエストでレスポンス圧縮を使用しません

- `--events-file=''`
  HTML ページの生成元とする events.json ファイルのパス

- `--insecure-skip-tls-verify=false`
  true の場合、サーバー証明書の有効性を検証しません。HTTPS 接続が安全でなくなります

- `--kubeconfig=''`
  CLI リクエストで使用する kubeconfig ファイルのパス。

- `-n, --namespace=''`
  指定した場合、この CLI リクエストで使用する namespace スコープ

- `--request-timeout='0'`
  サーバーへの 1 リクエストを諦めるまでの待ち時間。0 以外の値には対応する時間の単位を付けてください（例: 1s、2m、3h）。0 はリクエストをタイムアウトさせないことを意味します。

- `-s, --server=''`
  Kubernetes API サーバーのアドレスとポート

- `--since=0s`
  5s、2m、3h のような相対時間より新しいログのみを返します。デフォルトはすべてのログです。since-time と since は同時に指定できません。

- `--since-time=''`
  指定した日時 (RFC3339) 以降のログのみを返します。デフォルトはすべてのログです。since-time と since は同時に指定できません。

- `--tls-server-name=''`
  サーバー証明書の検証に使用するサーバー名。指定しない場合は、サーバーへの接続に使用したホスト名が使われます

- `--token=''`
  API サーバーへの認証に使用する Bearer トークン

- `--user=''`
  使用する kubeconfig のユーザー名

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm inspect --help` / `gen-oc-help.py` で生成</sub>
