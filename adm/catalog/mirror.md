# `oc adm catalog mirror`

> operator-registry のカタログをミラーする

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm catalog`](../catalog.md) / `mirror`

## Usage

```
oc adm catalog mirror SRC DEST [flags] [options]
```

カタログの内容をレジストリにミラーします。

このコマンドは、カタログを含むイメージを pull してディスクに展開し、マニフェストで使われているすべてのイメージを問い合わせたうえで、それらを対象のレジストリにミラーします。

デフォルトではカタログファイルは一時ディレクトリに展開されますが、フラグを指定してローカルに保存することもできます。

イメージコンテンツソースポリシーがファイルに書き出され、対象レジストリにアクセスできるクラスタに追加できます。これにより、オペレータマニフェストに記載された場所ではなくミラーから pull するようクラスタが設定されます。

"oc image mirror" と互換性のある mapping.txt ファイルも作成されます。ミラーリング設定をさらにカスタマイズする用途に使えますが、通常は必要ありません。

        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        !! DEPRECATION NOTICE:
        !!   Sqlite-based catalogs are deprecated. Support for them will be removed in a
        !!   future release. Please migrate your catalog workflows to the new file-based
        !!   catalog format.
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## Examples

```bash
# operator-registry のイメージとその内容をレジストリにミラーする
oc adm catalog mirror quay.io/my/image:latest myregistry.com

# operator-registry のイメージとその内容を、レジストリ内の特定の namespace にミラーする
oc adm catalog mirror quay.io/my/image:latest myregistry.com/my-namespace

# まずファイルにミラーしてから、エアギャップ環境のレジストリにミラーする
oc adm catalog mirror quay.io/my/image:latest file:///local/index
oc adm catalog mirror file:///local/index/my/image:latest my-airgapped-registry.com

# ミラーレジストリを使用するようクラスタを設定する
oc apply -f manifests/imageDigestMirrorSet.yaml

# ミラーリングのマッピングを編集し、"oc image mirror" で手動でミラーする
oc adm catalog mirror --manifests-only quay.io/my/image:latest myregistry.com
oc image mirror -f manifests/mapping.txt

# oc adm catalog mirror が生成したすべての ImageDigestMirrorSet を削除する
oc delete imagedigestmirrorset -l operators.openshift.org/catalog=true
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--continue-on-error=true`
  ミラーリング中にエラーが発生しても処理を続行し、できる限り多くをミラーします。

- `--dir=''`
  file:// のイメージのコピー先となる、ディスク上のディレクトリ。

- `--dry-run=false`
  実行される予定の操作を表示し、書き込み先に何も書き込まずに終了します。

- `--from-dir=''`
  file:// のイメージの読み込み元となる、ディスク上のディレクトリ。--dir より優先されます

- `--idms-scope='repository'`
  imagedigestmirrorset ファイル内のレジストリミラーのスコープ。指定できる値: repository、registry。デフォルト: repository

- `--index-filter-by-os=''`
  複数のバリアントが存在する場合に、どのインデックスイメージを選択するかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。インデックスから参照されるイメージには適用されません。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--manifests-only=false`
  ミラーリングに必要なマニフェストを計算しますが、実際のイメージコンテンツのミラーは行いません。

- `--max-components=2`
  宛先のマッピングで許可されるパス要素の最大数。例: `quay.io/org/repo` のパス要素は 2 つです。

- `--max-idms-size=250000`
  生成される IDMS yaml の最大バイト数。デフォルトは 250000 です

- `--max-per-registry=4`
  1 つのレジストリに対して許可する同時リクエスト数。

- `--path=''`
  インデックスファイルについて、コンテナ内のパスとローカルパスの対応を指定します。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

- `--to-manifests=''`
  マニフェストを保存するローカルパス。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm catalog mirror --help` / `gen-oc-help.py` で生成</sub>
