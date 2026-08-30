# `oc config set-credentials`

> kubeconfig にユーザーエントリを設定する

[`oc`](../oc.md) / [`oc config`](../config.md) / `set-credentials`

## Usage

```
oc config set-credentials NAME [--client-certificate=path/to/certfile] [--client-key=path/to/keyfile] [--token=bearer_token] [--username=basic_user] [--password=basic_password] [--auth-provider=provider_name] [--auth-provider-arg=key=value] [--exec-command=exec_command] [--exec-api-version=exec_api_version] [--exec-arg=arg] [--exec-env=key=value] [options]
```

既に存在する名前を指定した場合、既存の値の上に新しいフィールドがマージされます。

        Client-certificate flags:
        --client-certificate=certfile --client-key=keyfile
        Bearer token flags:
        --token=bearer_token
        Basic auth flags:
        --username=basic_user --password=basic_password
Bearer トークンと Basic 認証は同時に指定できません。

## Examples

```bash
# "cluster-admin" の "client-key" フィールドだけを設定する
# エントリ。他の値には触れない
oc config set-credentials cluster-admin --client-key=~/.kube/admin.key

# "cluster-admin" エントリに Basic 認証を設定する
oc config set-credentials cluster-admin --username=admin --password=uXFGweU9l35qcif

# "cluster-admin" エントリにクライアント証明書データを埋め込む
oc config set-credentials cluster-admin --client-certificate=~/.kube/admin.crt --embed-certs=true

# "cluster-admin" エントリで Google Compute Platform の認証プロバイダを有効にする
oc config set-credentials cluster-admin --auth-provider=gcp

# "cluster-admin" エントリで OpenID Connect の認証プロバイダを、追加の引数付きで有効にする
oc config set-credentials cluster-admin --auth-provider=oidc --auth-provider-arg=client-id=foo --auth-provider-arg=client-secret=bar

# "cluster-admin" エントリの OpenID Connect 認証プロバイダから、設定値 "client-secret" を削除する
oc config set-credentials cluster-admin --auth-provider=oidc --auth-provider-arg=client-secret-

# "cluster-admin" エントリの新しい exec 認証プラグインを有効にする
oc config set-credentials cluster-admin --exec-command=/path/to/the/executable --exec-api-version=client.authentication.k8s.io/v1beta1

# "cluster-admin" エントリの新しい exec 認証プラグインを、インタラクティブモードで有効にする
oc config set-credentials cluster-admin --exec-command=/path/to/the/executable --exec-api-version=client.authentication.k8s.io/v1beta1 --exec-interactive-mode=Never

# "cluster-admin" エントリの exec 認証プラグインの引数を新しく定義する
oc config set-credentials cluster-admin --exec-arg=arg1 --exec-arg=arg2

# "cluster-admin" エントリの exec 認証プラグインの環境変数を作成または更新する
oc config set-credentials cluster-admin --exec-env=key1=val1 --exec-env=key2=val2

# "cluster-admin" エントリの exec 認証プラグインの環境変数を削除する
oc config set-credentials cluster-admin --exec-env=var-to-remove-
```

## Options

- `--auth-provider=''`
  kubeconfig 内のユーザーエントリで使用する認証プロバイダ

- `--auth-provider-arg=[]`
  認証プロバイダに渡す 'key=value' 形式の引数

- `--client-certificate=''`
  kubeconfig 内のユーザーエントリ用のクライアント証明書ファイルのパス

- `--client-key=''`
  kubeconfig 内のユーザーエントリ用のクライアント鍵ファイルのパス

- `--embed-certs=false`
  kubeconfig 内のユーザーエントリに、クライアント証明書 / 鍵を埋め込みます

- `--exec-api-version=''`
  kubeconfig 内のユーザーエントリで使用する exec クレデンシャルプラグインの API バージョン

- `--exec-arg=[]`
  kubeconfig 内のユーザーエントリの exec クレデンシャルプラグインコマンドに渡す新しい引数

- `--exec-command=''`
  kubeconfig 内のユーザーエントリで使用する exec クレデンシャルプラグインのコマンド

- `--exec-env=[]`
  exec クレデンシャルプラグインに渡す 'key=value' 形式の環境変数

- `--exec-interactive-mode=''`
  kubeconfig 内のユーザーエントリで使用する exec クレデンシャルプラグインの InteractiveMode

- `--exec-provide-cluster-info=false`
  kubeconfig 内のユーザーエントリで使用する exec クレデンシャルプラグインの ProvideClusterInfo

- `--password=''`
  kubeconfig 内のユーザーエントリの password

- `--token=''`
  kubeconfig 内のユーザーエントリの token

- `--username=''`
  kubeconfig 内のユーザーエントリの username

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config set-credentials --help` / `gen-oc-help.py` で生成</sub>
