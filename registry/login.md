# `oc registry login`

> 統合レジストリにログインする

[`oc`](../oc.md) / [`oc registry`](../registry.md) / `login`

## Usage

```
oc registry login  [flags] [options]
```

OpenShift の統合レジストリにログインします。

これにより、（管理者が設定していれば）外部レジストリ名を使って、ローカルの Docker クライアントを OpenShift の統合レジストリにログインさせます。クライアント証明書でサーバーにログインしている場合、コンテナレジストリは通常クライアント証明書を受け付けないため、このコマンドはエラーを報告します。

高度なオプションとして、--auth-basic に USER:PASSWORD を指定して、ログインに使う認証情報を指定できます。

--to を使うと、ホームディレクトリの .docker/config.json ではなく、別のファイルに認証情報を書き出せます。

レジストリのホスト名を検出するため、クライアントは現在の namespace または openshift namespace からイメージストリームを探し、レジストリのホスト名を示すステータスフィールドを使用します。イメージストリームが見つからない場合や、イメージストリームを参照する権限がない場合は、--registry フラグで目的のホスト名を指定する必要があります。

--registry フラグを指定して、カスタムの DNS 名で統合レジストリにログインしたり、外部レジストリにログインしたりすることもできます。なお --auth-basic=USER:PASSWORD を指定しない場合、接続中の kubeconfig ファイルの認証トークンが、指定したレジストリ値に対する認証エントリとして認証情報ファイル（デフォルトは Docker の config.json）に記録されます。

## Examples

```bash
# 統合レジストリにログインする
oc registry login

# BASIC 認証の資格情報を使って別のレジストリにログインする
oc registry login --registry quay.io/myregistry --auth-basic=USER:PASS
```

## Options

- `--auth-basic=''`
  認証用の資格情報を 'user:password' の形式で指定します（上級者向け）

- `--insecure=false`
  レジストリへのログインを確認する際に、HTTPS の証明書検証をスキップします。

- `--registry=''`
  レジストリに使用する代替のドメイン名とポート。デフォルトはクラスタに設定された外部ホスト名です。

- `-a, --registry-config=''`
  資格情報を保存するファイルの場所。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json または /run/containers/${UID}/auth.json です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するようデフォルトを変更できます。

- `--skip-check=false`
  レジストリに対する資格情報の確認をスキップします。

- `--to=''`
  資格情報を保存するファイルの場所。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json または /run/containers/${UID}/auth.json です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するようデフォルトを変更できます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc registry login --help` / `gen-oc-help.py` で生成</sub>
