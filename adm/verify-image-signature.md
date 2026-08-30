# `oc adm verify-image-signature`

> イメージ署名に含まれるイメージの identity を検証する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `verify-image-signature`

## Usage

```
oc adm verify-image-signature IMAGE --expected-identity=EXPECTED_IDENTITY [--save] [flags] [options]
```

ローカルの公開 GPG 鍵を使って、内部レジストリにインポートされたイメージのイメージ署名を検証します。

このコマンドは、公開 GPG 鍵で署名そのものを検証し、指定された expected identity と対象イメージの identity (pull spec) を照合することで、イメージ署名に含まれるイメージの identity が信頼できるかどうかを検証します。デフォルトでは、"$GNUPGHOME/.gnupg/pubring.gpg" にある公開 GPG キーリングを使用します

デフォルトでは、このコマンドは検証結果をイメージオブジェクトに保存しません。保存するには "--save" フラグを指定する必要があります。なお、イメージ署名の検証ステータスを変更するには、イメージオブジェクトを編集する権限（通常は "image-auditor" ロール）が必要です。

既に検証済みのイメージに対して、無効な GPG 鍵や無効な expected identity とともに "--save" フラグを使うと、保存されていた検証ステータスが削除され、そのイメージは "unverified" になります。

このコマンドをクラスタ外で実行する場合は、"--registry-url" パラメータでイメージレジストリのパブリック URL を指定する必要があります。

すべての検証結果を削除するには "--remove-all" フラグを使用します。

## Examples

```bash
# ローカルの GPG キーチェーンを使って、イメージ署名と identity を検証する
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 \
--expected-identity=registry.local:5000/foo/bar:v1

# ローカルの GPG キーチェーンを使ってイメージ署名と identity を検証し、その結果を保存する
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 \
--expected-identity=registry.local:5000/foo/bar:v1 --save

# 公開されたレジストリのルート経由で、イメージ署名と identity を検証する
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 \
--expected-identity=registry.local:5000/foo/bar:v1 \
--registry-url=docker-registry.foo.com

# イメージからすべての署名検証結果を削除する
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 --remove-all
```

## Options

- `--expected-identity=''`
  検証対象として期待されるイメージの docker 参照（必須）。

- `--insecure=false`
  設定した場合、レジストリとの通信に非セキュアなプロトコルを使用します。

- `--public-key='pubring.gpg'`
  検証に使用する公開 GPG 鍵のパス（デフォルトは "pubring.gpg"）

- `--registry-url=''`
  レジストリへの接続時に、クラスタ内部アドレスの代わりに使用するアドレス。内部レジストリのアドレスを名前解決できない、または到達できない場合に便利です。

- `--remove-all=false`
  設定した場合、指定したイメージからすべての署名検証結果を削除します。

- `--save=false`
  true の場合、検証結果をイメージオブジェクトに保存します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm verify-image-signature --help` / `gen-oc-help.py` で生成</sub>
