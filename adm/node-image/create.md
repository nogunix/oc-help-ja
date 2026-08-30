# `oc adm node-image create`

> 対象クラスタに追加するノードを起動するための ISO イメージを作成する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm node-image`](../node-image.md) / `create`

## Usage

```
oc adm node-image create [flags] [options]
```

指定したノード群の初期設定から ISO イメージを作成し、既存のオンプレミスクラスタに追加します。

このコマンドは、カスタマイズした ISO イメージの作成に必要な情報を取得するため、対象クラスタ上の一時的な namespace に Pod を作成します。ダウンロードした ISO イメージを使えば、あらかじめ選んだノード群を起動し、完全に自動化された形で対象クラスタに追加できます。

このコマンドには、対象クラスタへの接続と、対象クラスタのリリースから必要な情報を取得するための有効なレジストリ認証情報も必要です。

選択したノードに必要な初期設定を与えるため、nodes-config.yaml 設定ファイルを作成する必要があります。単一ノードを追加するだけの簡単な構成であれば、フラグの組み合わせでホストを設定することもできます。その場合、必須のフラグは '--mac-address' のみで、他はすべて省略可能です（注: 設定ファイルが存在していても無視されます）。

コマンドが失敗した場合、エラーの詳細と追加のトラブルシューティング情報を含む report.json ファイルが自動的に作成されます。

## Examples

```bash
# ISO イメージを作成し、カレントフォルダにダウンロードする
oc adm node-image create

# 別のアセットフォルダを使う
oc adm node-image create --dir=/tmp/assets

# カスタムのイメージ名を指定する
oc adm node-image create -o=my-node.iso

# ISO の代わりに、PXE ブートに使用できるファイルを作成します
oc adm node-image create --pxe

# 設定ファイルを使わずに単一ノードを追加する ISO を作成する
oc adm node-image create --mac-address=00:d8:e7:c7:4b:bb

# root デバイスヒントを指定し、設定ファイルを使わずに単一ノードを追加する ISO を作成する
# 設定ファイルを使って
oc adm node-image create --mac-address=00:d8:e7:c7:4b:bb --root-device-hint=deviceName:/dev/sda
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `-c, --cpu-architecture=''`
  単一ノード用のフラグ。ノードのインストールに使用する CPU アーキテクチャ。`mac-address` を指定した場合にのみ有効です。

- `--dir=''`
  設定ファイルを含むパス。生成された成果物の保存先にもなります。

- `--hostname=''`
  単一ノード用のフラグ。ノードに設定するホスト名。`mac-address` を指定した場合にのみ有効です。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `-m, --mac-address=''`
  単一ノード用のフラグ。設定を適用するホストを識別するための MAC アドレス。指定した場合、nodes-config.yaml 設定ファイルは使用されません。

- `--network-config-path=''`
  単一ノード用のフラグ。ノードに適用する NMState 設定を記述した YAML ファイル。`mac-address` を指定した場合にのみ有効です。

- `-o, --output-name=''`
  出力イメージの名前。

- `-p, --pxe=false`
  ISO の代わりに、PXE ブートに使用できるファイルを作成する

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `-r, --report=false`
  指定した場合、report.json を常にアセットフォルダに生成します

- `--root-device-hint=''`
  単一ノード用のフラグ。イメージのルートファイルシステムを配置するストレージの場所を示すヒント。形式は `<hint name>`:`<value>` です。`mac-address` を指定した場合にのみ有効です。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

- `-k, --ssh-key-path=''`
  単一ノード用のフラグ。ノードへのアクセスに使用する SSH 鍵のパス。`mac-address` を指定した場合にのみ有効です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm node-image create --help` / `gen-oc-help.py` で生成</sub>
