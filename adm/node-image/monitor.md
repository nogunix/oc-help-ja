# `oc adm node-image monitor`

> OpenShift クラスタに追加中の新しいノードを監視する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm node-image`](../node-image.md) / `monitor`

## Usage

```
oc adm node-image monitor [flags] [options]
```

"oc adm node-image create" コマンドで生成したイメージを使って、クラスタに追加中のノードを監視します。

ノードイメージ ISO をホスト上で起動した後、monitor コマンドは、そのホストのクラスタ追加を妨げる可能性のある事前検証の失敗を報告します。検証に成功すると、ノードのインストールが開始されます。

ノードがクラスタに参加して完全に機能するようになるには、2 つの証明書署名要求 (CSR) を承認する必要があります。monitor コマンドは、承認待ちの CSR を表示します。

このコマンドは、ノードがクラスタへの参加に成功した時点で終了します。

このコマンドは、ノードを監視するために、対象クラスタ上の一時的な namespace に Pod を作成します。

このコマンドには、対象クラスタへの接続と、対象クラスタのリリースから必要な情報を取得するための有効なレジストリ認証情報も必要です。

## Examples

```bash
# クラスタに追加中の単一ノードを監視する
oc adm node-image monitor --ip-addresses 192.168.111.83

# クラスタに追加中の複数ノードを、それぞれ区切って監視する
# IP アドレスをカンマ区切りで
oc adm node-image monitor --ip-addresses 192.168.111.83,192.168.111.84
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--ip-addresses=''`
  監視対象ノードの IP アドレス。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm node-image monitor --help` / `gen-oc-help.py` で生成</sub>
