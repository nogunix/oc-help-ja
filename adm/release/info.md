# `oc adm release info`

> リリースの情報を表示する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm release`](../release.md) / `info`

## Usage

```
oc adm release info IMAGE [--changes-from=IMAGE] [--verify|--commits|--pullspecs] [flags] [options]
```

OpenShift リリースの情報を表示します。

このコマンドは、OpenShift の更新内容を説明する情報を取得・検証・整形して表示します。更新はコンテナイメージとして配布され、そのメタデータには、コンポーネントイメージと、システムオペレータのインストールに必要な設定が記述されています。リリースイメージは通常コンテンツダイジェストで参照されるため、このコマンドと更新基盤は、更新が改ざんされていないことを検証できます。

引数を指定しない場合、現在接続しているクラスタのリリースが表示されます。1 つ以上のイメージを pull spec で指定すると、各リリースイメージの詳細を確認できます。セマンティックバージョン (4.11.2) を引数として渡すこともでき、クラスタバージョンオブジェクトがアップグレードチャネルでそのバージョンを認識していれば、そのバージョンのリリース情報を見つけます。

--commits フラグは、各コンポーネントイメージのソースについて Git のコミット ID とリポジトリ URL を表示します。--pullspecs フラグは、コンポーネントイメージの完全な pull spec を表示します。--size は各イメージとそのレイヤーの内訳、およびペイロード全体のサイズを表示します。--contents は、更新実行時にクラスタへ適用される設定を表示します。イメージを 2 つ指定した場合は、1 つ目と 2 つ目の差分が表示されます。-o name、-o digest、-o pullspec を使うと、リリースイメージが参照するイメージのタグ名、ダイジェスト、pull spec をそれぞれ出力できます。

--verify フラグは、入力された各リリースイメージについて 1 行のサマリを表示し、それぞれの完全性を検証します。リリースが改ざんされている場合、このコマンドはエラーを返します。イメージを検証する際は、タグではなくダイジェスト付きの pull spec（例: quay.io/openshift/release@sha256:a9bc...）を渡すことを推奨します。これにより、攻撃者に古い（脆弱性のある可能性がある）バージョンをインストールさせられるのを防げます。

--bugs と --changelog フラグは、git でそのリリースの履歴をクローンし、2 つのリリース引数の間で発生したコード変更を表示します。この操作は時間がかかり、すべてのリポジトリをクローンできるだけの十分なディスク容量が必要です。

さらに、--rpmdb-cache フラグを使うと、リリース内のイメージの rpmdb の内容をキャッシュできます。その上で --rpmdb フラグを使うとイメージの RPM の内容を表示でき、--rpmdb-diff フラグを使うと 2 つのリリース引数の間で発生した RPM の変更を表示できます。この処理に最適化されたイメージ（十分に新しい machine-os イメージなど）ではかなり高速かつ効率的ですが、そうでない場合は十分なディスク容量を必要とする低速な処理になります。デフォルトでは machine-os コンポーネントを含むイメージが RPM クエリの対象になります。--rpmdb-image で別のイメージを対象にできます。

指定したイメージが複数のオペレーティングシステムに対応している場合、現在の OS に一致するイメージが選択されます。それ以外の場合は、--filter-by-os で目的のイメージを選択する必要があります。

## Examples

```bash
# クラスタの現在のリリースの情報を表示する
oc adm release info

# リリースを構成するソースコードを表示する
oc adm release info 4.11.2 --commit-urls

# 2 つのリリース間のソースコードの差分を表示する
oc adm release info 4.11.0 4.11.2 --commits

# そのリリースが参照するイメージの所在を表示する
oc adm release info quay.io/openshift-release-dev/ocp-release:4.11.2 --pullspecs

# linux/s390x イメージの情報を表示する
# 注: ワイルドカードによる絞り込みはサポートされません。取り出す os/arch を 1 つ指定してください
oc adm release info quay.io/openshift-release-dev/ocp-release:4.11.2 --filter-by-os=linux/s390x
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--bugs=''`
  このパスに展開された git リポジトリの changelog から、バグ一覧を生成します。

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--changelog=''`
  このパスに展開された git ディレクトリから changelog 出力を生成します。

- `--changes-from=''`
  このイメージから指定したイメージへの変更点を表示します。

- `--commit-urls=false`
  可能であればソースコードへのリンクを表示します。

- `--commits=false`
  そのイメージの作成元となったソースの情報を表示します。

- `--contents=false`
  リリースの内容を表示します。

- `--dir=''`
  file:// のイメージのコピー先となる、ディスク上のディレクトリ。

- `--filter-by-os=''`
  複数のバリアントが存在する場合に、どのイメージを対象とするかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。

- `--idms-file=''`
  ImageDigestMirrorSet ファイルのパス。指定した場合、このファイルの情報を使ってイメージの代替の場所を探します。

- `--image-for=''`
  指定したイメージの pull spec を表示します。存在しない場合はエラーになります。

- `--include-images=false`
  リリースを JSON 形式で出力する際に、そのリリースが参照するイメージも出力します。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--max-per-registry=4`
  1 つのレジストリに対して許可する同時リクエスト数。

- `-o, --output=''`
  リリース情報を別の形式で表示します: digest|json|name|pullspec|template|jsonpath。

- `--pullspecs=false`
  ダイジェストの代わりに、各イメージの pull spec を表示します。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--rpmdb=false`
  イメージ内の RPM パッケージを一覧表示します。

- `--rpmdb-cache=''`
  rpmdb の内容をこのディレクトリにキャッシュします。

- `--rpmdb-diff=false`
  RPM パッケージの差分を生成します。

- `--rpmdb-image=''`
  RPM の照会に使用するイメージ。

- `--size=false`
  重複分を含めた各イメージのサイズを表示します。

- `--skip-bug-check=false`
  --output=name でバグ一覧を生成する際に、バグのステータスを確認しません

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--verify=false`
  このパスに展開された git リポジトリの changelog から、バグ一覧を生成します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm release info --help` / `gen-oc-help.py` で生成</sub>
