# `oc adm release new`

> 新しい OpenShift リリースを作成する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm release`](../release.md) / `new`

## Usage

```
oc adm release new [SRC=DST ...] [flags] [options]
```

クラスタを更新するための新しい OpenShift リリースイメージをビルドします。

OpenShift では、"オペレータ" と呼ばれる長時間稼働する能動的な管理プロセスによって、クラスタを稼働させ、コンポーネントのライフサイクルを管理します。このコマンドは、オペレータの定義を含む一連のイメージを、クラスタのインストールや更新に使える 1 つの更新ペイロードにまとめます。

オペレータは、クラスタへのインストールに必要な設定を、自身のイメージ内の '/manifests' ディレクトリに置くことが想定されています。このコマンドは一連のオペレータイメージを順に処理し、それらのマニフェストを、順序付けられた 1 つの Kubernetes オブジェクトのリストとして取り出します。このリストは、更新時に cluster version operator がクラスタ上で順次適用します。マニフェストファイルはデフォルトで '0000 70`<image_name>`_`<filename>` ' にリネームされます。全体の順序を制御したい（他のオペレータより前後に置きたい）オペレータの作成者は、ファイル名の先頭に '0000 NN`<component>`_' を付けてください。これにより、リリースビルダーはコンポーネントのプレフィックスを付与しなくなります。マニフェストが読み込まれるのは、入力のうちイメージラベル 'io.openshift.release.operator=true' を持つイメージだけです。

入力に含まれていても、オペレータの image-references ファイルから参照されていないイメージは、--include=NAME を指定しない限り最終的なリリースイメージに含まれません。

SRC=DST の位置引数でマッピングを指定すると、特定のオペレータを特定のイメージで上書きできます。例:

cluster-version-operator=registry.example.com/openshift/cluster-version-operator:test-123

デフォルトの cluster-version-operator イメージを、registry.example.com から取得したイメージで上書きします。

## Examples

```bash
# 最新の origin イメージからリリースを作成し、DockerHub リポジトリに push する
oc adm release new --from-image-stream=4.11 -n origin --to-image docker.io/mycompany/myrepo:latest

# 以前のリリースを基に、メタデータを更新した新しいリリースを作成する
oc adm release new --from-release registry.ci.openshift.org/origin/release:v4.11 --name 4.11.1 \
--previous 4.11.0 --metadata ... --to-image docker.io/mycompany/myrepo:latest

# 新しいリリースを作成し、イメージを 1 つだけ上書きする
oc adm release new --from-release registry.ci.openshift.org/origin/release:v4.11 \
cli=docker.io/mycompany/cli:latest --to-image docker.io/mycompany/myrepo:latest

# そのリリースを再現できることを確認するため、検証パスを実行する
oc adm release new --from-release registry.ci.openshift.org/origin/release:v4.11
```

## Options

- `--allow-missing-images=false`
  オペレータが、含まれていないリリースイメージを参照している場合に、そのエラーを無視します。

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--component-versions=''`
  リリースに追加のバージョン文字列を key=value[,key=value] の形式で指定します。

- `--component-versions-display-names=''`
  リリースに追加のバージョン表示名を key=value[,key=value] の形式で指定します。

- `--dir=''`
  リリースの内容を書き出すディレクトリ。デフォルトは一時ディレクトリです。

- `--dry-run=false`
  ミラーリングや push による外部レジストリへの変更をスキップします。

- `--exclude=[]`
  除外するイメージ名またはタグのリスト。すべての入力を処理した後に適用されます。カンマ区切り、または個別の引数として指定します。

- `--from-dir=''`
  このディレクトリを、リリースペイロードのソースとして使用します。

- `--from-image-stream=''`
  指定したイメージストリーム内のすべてのタグを調べ、それらからリリースペイロードをビルドします。

- `-f, --from-image-stream-file=''`
  ディスク上の指定したイメージストリームを使って、そこからリリースペイロードをビルドします。

- `--from-release=''`
  既存のリリースイメージを入力として使用します。

- `--include=[]`
  prune の対象外とするイメージタグのリスト。除外指定が優先されます。カンマ区切り、または個別の引数として指定します。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--keep-manifest-list=false`
  イメージがマニフェストリストの一部である場合、イメージが 1 つしか見つからなくても常にリストをミラーします。

- `--mapping-file=[]`
  リリースのビルドに使用する入力イメージのマッピングを定義したファイル

- `--max-per-registry=4`
  1 つのレジストリに対して許可する同時リクエスト数。

- `--metadata=''`
  リリースマニフェストのメタデータとして添付する JSON オブジェクト。

- `--mirror=''`
  リリースの内容をこのリポジトリにミラーします。

- `--name=''`
  リリースの名前。デフォルトは現在時刻です。

- `--next=[]`
  リリースマニフェスト上で、このバージョンより後に位置すべきセマンティックバージョンのリスト。--next は、そのリリースがまだ存在しないためにリグレッションを引き起こす可能性があります。注意して使用してください。

- `-o, --output=''`
  マッピング定義をこの形式で出力します。

- `--previous=[]`
  リリースマニフェスト上で、このバージョンより前に位置すべきセマンティックバージョンのリスト。

- `--reference-mode=''`
  デフォルトでは、イメージストリームのイメージ参照は、そのストリームのパブリックレジストリとイメージダイジェストを指します。'source' を指定すると、元イメージへの参照を組み立てます。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--release-manifest=false`
  true の場合、--name をセマンティックバージョンとして使い、リリースマニフェストを作成します。

- `--skip-manifest-check=false`
  オペレータが解析できない yaml/yml/json ファイルを含んでいる場合に、そのエラーを無視します。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

- `--to-dir=''`
  イメージを作成する代わりに、リリースマニフェストをディレクトリに出力します。

- `--to-file=''`
  イメージを作成する代わりに、リリースを tar ファイルに出力します。

- `--to-image=''`
  リリースイメージのアップロード先。

- `--to-image-base=''`
  指定した場合、リリースレイヤーを上に重ねる対象のイメージ。

- `--to-image-base-tag='cluster-version-operator'`
  指定した場合、リリースレイヤーを上に重ねる入力側のイメージタグ。デフォルトは cluster-version-operator です。

- `--to-signature=''`
  指定した場合、このリリースを説明する署名可能なメッセージを出力します。--to-image が必要です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm release new --help` / `gen-oc-help.py` で生成</sub>
