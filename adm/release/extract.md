# `oc adm release extract`

> 更新ペイロードの内容をディスクに取り出す

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm release`](../release.md) / `extract`

## Usage

```
oc adm release extract [flags] [options]
```

リリースイメージの内容をディスクに取り出します。

検査やデバッグのために、OpenShift リリースイメージの内容をディスクに取り出します。更新イメージには、そのバージョンでクラスタにインストールする必要があるオペレータのマニフェストとメタデータが含まれています。

--tools と --command フラグを使うと、お使いの OS 向けのクライアントバイナリをディスクに取り出せます。--tools は、現在の OS 向けツール（--command-os に '*' を指定した場合はすべての OS 向け）を含むアーカイブファイルを作成します。--command に 'oc' または 'openshift-install' を指定すると、バイナリを直接取り出します。--signing-key で PGP 秘密鍵ファイルを渡すと、取り出した内容を記述し、その鍵で署名した ASCII armor 形式の sha256sum.txt.asc ファイルが作成されます。より高度な署名を行うには、生成された sha256sum.txt と gpg などの外部ツールを使用してください。

--credentials-requests フラグは、取り出すマニフェストをクラウドの credential request のみに絞り込みます。--cloud フラグは、さらに特定のクラウド向けの credential request に絞り込みます。--cloud に指定できる値は alibabacloud、aws、azure、gcp、ibmcloud、nutanix、openstack、ovirt、powervs、vsphere です。

--included フラグは、取り出すマニフェストを、そのクラスタに含まれると想定されるものに絞り込みます。フィルタは累積的に適用されるため、'--credentials-requests --included' はクラスタに含まれると想定されるクラウドの credential request のみを対象にします。--install-config を指定した場合はそれを使って想定されるクラスタ構成を判断し、指定しない場合は現在のクラスタに問い合わせて構成を判断します。このコマンドは、取り出しに使うクライアントのバージョンが対象クラスタのバージョンと一致しているときに最も正確です。

マニフェストを取り出す代わりに、--git=DIR を指定して、そのリリースを構成するソースコードを Git でチェックアウトできます。コンポーネントがソースコードに紐づいていない場合は警告が表示されます。このコマンドは、'git checkout' の実行（現在のブランチが変わる可能性があります）を除き、破壊的な操作を行いません。PATH 上に 'git' が必要です。

指定したイメージが複数のオペレーティングシステムに対応している場合、現在の OS に一致するイメージが選択されます。それ以外の場合は、--filter-by-os で目的のイメージを選択する必要があります。

## Examples

```bash
# git を使って、現在のクラスタリリースのソースコードを DIR にチェックアウトする
oc adm release extract --git=DIR

# AWS 向けのクラウド credential request を取り出す
oc adm release extract --credentials-requests --cloud=aws

# git を使って、linux/s390x イメージから現在のクラスタリリースのソースコードを DIR にチェックアウトする
# 注: ワイルドカードによる絞り込みはサポートされません。取り出す os/arch を 1 つ指定してください
oc adm release extract --git=DIR quay.io/openshift-release-dev/ocp-release:4.11.2 --filter-by-os=linux/s390x
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--cloud=''`
  指定したクラウドプロバイダに関係しない credential request を除外します。--credentials-requests と併用した場合のみ有効です。

- `--command=''`
  お使いの OS 向けのクライアントを取り出すには 'oc' または 'openshift-install' を指定します。

- `--command-os=''`
  取り出すコマンドの対象 OS (mac, windows, linux) を上書きします。アーキテクチャ付き (linux/arm64, mac/amd64) で指定することもできます。'*' を指定すると、すべてのツールアーカイブを取り出します。

- `--credentials-requests=false`
  credential request ではないマニフェストを除外します。

- `--dir=''`
  file:// のイメージのコピー先となる、ディスク上のディレクトリ。

- `--file=''`
  ペイロードから 1 つのファイルを標準出力に取り出します。

- `--filter-by-os=''`
  複数のバリアントが存在する場合に、どのイメージを対象とするかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。

- `--from=''`
  リリースペイロードを含むイメージ。

- `--git=''`
  このリリースを作成したソースを、指定したディレクトリにチェックアウトします。リポジトリは `<dir>`/`<host>`/`<path>` に作成されます。PATH 上に 'git' が必要です。

- `--idms-file=''`
  ImageDigestMirrorSet ファイルのパス。指定した場合、このファイルの情報を使ってイメージの代替の場所を探します。

- `--included=false`
  クラスタに含まれることが想定されていないマニフェストを除外します。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--install-config=''`
  openshift-install コマンドが読み込む install-config ファイルのパス。--included と併用した場合のみ有効です。

- `--max-per-registry=0`
  1 つのレジストリに対して許可する同時リクエスト数。

- `-o, --output=''`
  出力形式。'--git' と併用する場合は 'commit' をサポートします。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--signing-key=''`
  --tools で生成される sha256sum.txt を、この GPG 鍵で署名します。この鍵で署名された sha256sum.txt.asc ファイルが作成されます。鍵は暗号化されているものとして扱われます。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

- `--to='.'`
  リリースの内容を書き出すディレクトリ。デフォルトはカレントディレクトリです。

- `--tools=false`
  リリースイメージからツールのアーカイブを取り出します。--command=* を指定したものとして扱われます

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm release extract --help` / `gen-oc-help.py` で生成</sub>
