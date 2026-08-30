# `oc login`

> サーバーにログインする

[`oc`](oc.md) / `login`

## Usage

```
oc login [URL] [flags] [options]
```

サーバーにログインし、以降の利用のためにログイン情報を保存します。

クライアントを初めて使う場合は、このコマンドでサーバーに接続し、認証済みセッションを確立して、接続情報を設定ファイルに保存します。デフォルトの設定は、ホームディレクトリ配下の ".kube/config" に保存されます。

ログインに必要な情報（ユーザー名とパスワード、セッショントークン、サーバーの詳細など）はフラグで指定できます。指定しない場合、コマンドは必要に応じて入力を求めます。該当するフラグを指定すれば、Web ブラウザ経由でログインすることもできます。

## Examples

```bash
# 対話的にログインする
oc login --username=myuser

# 指定した認証局ファイルを使って、指定したサーバーにログインする
oc login localhost:8443 --certificate-authority=/path/to/cert.crt

# 指定した資格情報で、指定したサーバーにログインする（対話的な入力は求められない）
oc login localhost:8443 --username=myuser --password=mypass

# 指定したサーバーにブラウザ経由でログインする
oc login localhost:8443 --web --callback-port 8280

# ブラウザを自動で開かずに（URL を表示するだけで）、指定したサーバーにログインする
oc login localhost:8443 --web --auto-open-browser=false --callback-port 8280

# ポート 8080 で待ち受けるローカルサーバーを起動し、Auth Code + PKCE で外部 OIDC 発行者にログインする
oc login localhost:8443 --exec-plugin=oc-oidc --client-id=client-id --extra-scopes=email,profile --callback-port=8080
```

## Options

- `--auto-open-browser=false`
  実験的機能: ログイン時にブラウザを自動的に開きます。--web と併用した場合のデフォルトは true、外部 OIDC 用に --exec-plugin と併用した場合のデフォルトは false です。

- `-c, --callback-port=0`
  --web を使用する場合のコールバックサーバーのポート。デフォルトは空いているランダムなポートです

- `--client-id=''`
  実験的機能: 外部 OIDC 発行者のクライアント ID。Auth Code + PKCE のみサポートします。必須です。

- `--client-secret=''`
  実験的機能: 外部 OIDC 発行者のクライアントシークレット（省略可）。

- `--exec-plugin=''`
  実験的機能: 外部 OIDC 発行者の認証に使用する credentials exec プラグインの種類を指定します。現在サポートされているのは 'oc-oidc' のみです

- `--extra-scopes=[]`
  実験的機能: 外部 OIDC 発行者に対する追加のスコープ（省略可）。

- `--issuer-url=''`
  実験的機能: 外部発行者の issuer URL。必須です。

- `--oidc-certificate-authority=''`
  実験的機能: 外部 OIDC 発行者との通信に使用する認証局バンドルのパス。

- `-p, --password=''`
  サーバー用のパスワード

- `-u, --username=''`
  サーバー用のユーザー名

- `-w, --web=false`
  Web ブラウザでログインします。OAuth2 の認可コードグラントフローを実行するため、ローカルの HTTP コールバックサーバーを起動します。そのサーバーのポートはすべてのユーザーに開かれるため、マルチユーザー環境では注意して使用してください。

- `--certificate-authority=''`
  認証局の証明書ファイルのパス

- `--insecure-skip-tls-verify=false`
  true の場合、サーバー証明書の有効性を検証しません。HTTPS 接続が安全でなくなります

- `--token=''`
  API サーバーへの認証に使用する Bearer トークン

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc login --help` / `gen-oc-help.py` で生成</sub>
