# `oc get-token`

> 実験的機能: credentials exec プラグインとして、外部 OIDC 発行者からトークンを取得する

[`oc`](oc.md) / `get-token`

## Usage

```
oc get-token --oidc-client-id=CLIENT_ID --oidc-issuer-url=ISSUER_URL [flags] [options]
```

実験的機能: このコマンドは開発中であり、予告なく変更される可能性があります。oc に組み込みの Credential Exec プラグインです。

リフレッシュトークンに加えて、Auth Code および Auth Code + PKCE をサポートします。get-token は認可コードフローの完了後に ID トークンとリフレッシュトークンをキャッシュし、ID トークンの期限が切れると、リフレッシュトークンフローで新しいトークンの取得を試みます。任意ですが、コンフィデンシャルクライアントとして動作するためのクライアントシークレットの指定にも対応しています。

## Examples

```bash
# クライアント ID と指定した追加スコープを使って、issuer URL への認可コードフローを開始する
oc get-token --client-id=client-id --issuer-url=test.issuer.url --extra-scopes=email,profile

# 別のコールバックアドレスを指定して、issuer URL への認可コードフローを開始する
oc get-token --client-id=client-id --issuer-url=test.issuer.url --callback-address=127.0.0.1:8343
```

## Options

- `--auto-open-browser=false`
  ブラウザを自動的に開くかどうかを指定します。

- `--callback-address='127.0.0.1:0'`
  フロー完了後に外部 OIDC 発行者がリダイレクトするコールバックアドレス。デフォルトは 127.0.0.1:0 で、ランダムなポートが選ばれます。

- `--client-id=''`
  外部 OIDC プロバイダが管理するユーザーのクライアント ID

- `--client-secret=''`
  外部 OIDC プロバイダが管理するユーザーのクライアントシークレット（省略可）。

- `--extra-scopes=[]`
  外部 OIDC プロバイダへの認証リクエストに付与する追加のスコープ（省略可）。

- `--issuer-url=''`
  外部 OIDC プロバイダの issuer URL

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc get-token --help` / `gen-oc-help.py` で生成</sub>
