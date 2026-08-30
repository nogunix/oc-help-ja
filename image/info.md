# `oc image info`

> イメージの情報を表示する

[`oc`](../oc.md) / [`oc image`](../image.md) / `info`

## Usage

```
oc image info IMAGE [...] [flags] [options]
```

リモートのイメージレジストリにあるイメージの情報を表示します。

このコマンドは、リモートのイメージレジストリにあるコンテナイメージのメタデータを取得します。イメージはタグまたはダイジェストで指定でき、一度に複数指定することもできます。

マニフェストリスト形式のイメージは、現在のオペレーティングシステム向けのものが表示されます。特定の OS 向けのイメージを見るには --filter-by-os=OS/ARCH フラグを使用します。マニフェストリスト形式でないイメージに --filter-by-os を指定した場合、このフラグは無視されます。

## Examples

```bash
# イメージの情報を表示する
oc image info quay.io/openshift/cli:latest

# ワイルドカードに一致するイメージの情報を表示する
oc image info quay.io/openshift/cli:4.*

# DIR 配下のディスクにミラーされたファイルの情報を表示する
oc image info --dir=DIR file://library/busybox:latest

# マルチ OS イメージのうち、どのイメージを表示するかを選択します
oc image info library/busybox:latest --filter-by-os=linux/arm64
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--dir=''`
  file:// のイメージの読み込み元となる、ディスク上のディレクトリ。

- `--filter-by-os=''`
  複数のバリアントが存在する場合に、どのイメージを対象とするかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。

- `--icsp-file=''`
  ImageContentSourcePolicy ファイルのパス。指定した場合、このファイルの情報を使ってイメージの代替の場所を探します。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `-o, --output=''`
  イメージを別の形式で表示します: json

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--show-multiarch=false`
  マルチアーキテクチャイメージであっても情報を表示します。指定しない場合、マルチアーキテクチャイメージではエラーになります。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc image info --help` / `gen-oc-help.py` で生成</sub>
