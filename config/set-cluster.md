# `oc config set-cluster`

> kubeconfig にクラスタエントリを設定する

[`oc`](../oc.md) / [`oc config`](../config.md) / `set-cluster`

## Usage

```
oc config set-cluster NAME [--server=server] [--certificate-authority=path/to/certificate/authority] [--insecure-skip-tls-verify=true] [--tls-server-name=example.com] [options]
```

既に存在する名前を指定した場合、そのフィールドの既存の値の上に新しいフィールドがマージされます。

## Examples

```bash
# 他の値には触れず、e2e クラスタエントリの server フィールドだけを設定する
oc config set-cluster e2e --server=https://1.2.3.4

# e2e クラスタエントリに認証局データを埋め込む
oc config set-cluster e2e --embed-certs --certificate-authority=~/.kube/e2e/kubernetes.ca.crt

# e2e クラスタエントリの証明書チェックを無効にする
oc config set-cluster e2e --insecure-skip-tls-verify=true

# e2e クラスタエントリの検証に使用する、カスタムの TLS サーバー名を設定する
oc config set-cluster e2e --tls-server-name=my-cluster-name

# e2e クラスタエントリのプロキシ URL を設定する
oc config set-cluster e2e --proxy-url=https://1.2.3.4
```

## Options

- `--certificate-authority=''`
  kubeconfig 内のクラスタエントリ用の認証局ファイルのパス

- `--embed-certs=false`
  kubeconfig 内のクラスタエントリの embed-certs

- `--insecure-skip-tls-verify=false`
  kubeconfig 内のクラスタエントリの insecure-skip-tls-verify

- `--proxy-url=''`
  kubeconfig 内のクラスタエントリの proxy-url

- `--server=''`
  kubeconfig 内のクラスタエントリの server

- `--tls-server-name=''`
  kubeconfig 内のクラスタエントリの tls-server-name

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config set-cluster --help` / `gen-oc-help.py` で生成</sub>
