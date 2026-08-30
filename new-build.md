# `oc new-build`

> 新しいビルド設定を作成する

[`oc`](oc.md) / `new-build`

## Usage

```
oc new-build (IMAGE | IMAGESTREAM | PATH | URL ...) [flags] [options]
```

ソースコードを指定して新しいビルドを作成します。

このコマンドは、イメージと公開リポジトリを持つコードを使って、アプリケーションのビルド設定を作成しようとします。イメージは、ローカルのコンテナストレージ（利用可能な場合）、コンテナイメージレジストリ、またはイメージストリームから検索されます。

ソースコードの URL を指定すると、そのソースコードを Pod 内で実行できるイメージに変換するビルドが設定されます。ローカルのソースは、サーバーから参照できるリモートリポジトリを持つ git リポジトリ内にある必要があります。

ビルド設定を作成すると、新しいビルドが自動的にトリガーされます。進捗は '%[1]s status' で確認できます。

## Examples

```bash
# 現在の git リポジトリのソースコードを基にビルド設定を作成する（パブリックな
# リモート）とコンテナイメージ
oc new-build . --image=repo/langimage

# 指定された [image]~[source code] の組み合わせを基に、NodeJS のビルド設定を作成する
oc new-build centos/nodejs-8-centos7~https://github.com/sclorg/nodejs-ex.git

# リモートリポジトリの beta2 ブランチを使ってビルド設定を作成する
oc new-build https://github.com/openshift/ruby-hello-world#beta2

# 引数として指定した Dockerfile を使ってビルド設定を作成する
oc new-build -D $'FROM centos:7\nRUN yum install -y httpd'

# リモートリポジトリからビルド設定を作成し、カスタム環境変数を追加する
oc new-build https://github.com/openshift/ruby-hello-world -e RACK_ENV=development

# リモートのプライベートリポジトリからビルド設定を作成し、使用する既存のシークレットを指定する
oc new-build https://github.com/youruser/yourgitrepo --source-secret=yoursecret

# 完全なマニフェストリストを持つイメージを使ってビルド設定を作成し、アプリケーションを作成して、アプリケーション成果物の名前を上書きする
oc new-build --image=myregistry.com/mycompany/image --name=private --import-mode=PreserveOriginal

# リモートリポジトリからビルド設定を作成し、ビルドに npmrc を注入する
oc new-build https://github.com/openshift/ruby-hello-world --build-secret npmrc:.npmrc

# リモートリポジトリからビルド設定を作成し、ビルドに環境データを注入する
oc new-build https://github.com/openshift/ruby-hello-world --build-config-map env:config

# リモートリポジトリと別のコンテナイメージから入力を取得するビルド設定を作成する
oc new-build https://github.com/openshift/ruby-hello-world --source-image=openshift/jenkins-1-centos7 --source-image-path=/var/lib/jenkins:tmp
```

## Options

- `--allow-missing-images=false`
  true の場合、ローカルにもレジストリにも見つからない参照先コンテナイメージであっても使用することを示します。

- `--allow-missing-imagestream-tags=false`
  true の場合、存在しないイメージストリームタグであっても使用することを示します。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--binary=false`
  ソース URL を前提とする代わりに、ビルドがバイナリの内容を受け取るように設定します。トリガーは無効になります。

- `--build-arg=[]`
  ビルド時に Docker へ渡すキーと値のペアを指定します。

- `--build-config-map=[]`
  ビルドの入力として使用する ConfigMap と配置先。

- `--build-secret=[]`
  ビルドの入力として使用するシークレットと配置先。

- `--code=[]`
  ビルド設定内のソースコード。

- `--context-dir=''`
  ビルドで使用するコンテキストディレクトリ。

- `-D, --dockerfile=''`
  直接ビルドする Dockerfile の内容を指定します。--strategy=docker が指定されたものとして扱われます。'-' を渡すと標準入力から読み込みます。

- `--dry-run=false`
  true の場合、操作を実行せずに結果だけを表示します。

- `-e, --env=[]`
  生成されるイメージに設定する環境変数を、キーと値のペアで指定します。

- `--env-file=[]`
  各コンテナに設定する環境変数を、キーと値のペアとして記述したファイル。

- `--image=[]`
  ビルダーとして使用するコンテナイメージの名前。

- `-i, --image-stream=[]`
  ビルダーとして使用するイメージストリームの名前。

- `--import-mode=''`
  'PreserveOriginal' を指定した場合、タグの完全なマニフェストリストをインポートします。デフォルトは 'Legacy' です。

- `--insecure-registry=false`
  true の場合、参照先のコンテナイメージが非セキュアなレジストリ上にあり、証明書チェックを回避すべきであることを示します

- `-l, --labels=''`
  生成されるすべてのリソースに設定するラベル。

- `--name=''`
  生成されるビルド成果物に使用する名前を設定します。

- `--no-output=false`
  true の場合、ビルドの出力をどこにも push しません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--output-version=''`
  出力オブジェクトの優先 API バージョン

- `--push-secret=''`
  出力イメージの push に使用する、既存のシークレットの名前。

- `-a, --show-all=false`
  出力時に、すべてのリソースを表示します（デフォルトは終了済みの Pod を非表示）

- `--show-labels=false`
  出力時に、すべてのラベルを最後の列として表示します（デフォルトはラベル列を非表示）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--source-image=''`
  ビルドのソースとして使用するイメージを指定します。--source-image-path も併せて指定する必要があります。

- `--source-image-path=''`
  ソースイメージからコピーするファイルまたはディレクトリと、ビルドディレクトリ内のコピー先を指定します。形式: [source]:[destination-dir]。

- `--source-secret=''`
  プライベートな git リポジトリのクローンに使用する、既存のシークレットの名前。

- `--strategy=`
  自動判定させたくない場合に、使用するビルドストラテジー (docker|pipeline|source) を指定します。注意: pipeline ストラテジーは非推奨です。Jenkins 上で Jenkinsfile を直接使うか、OpenShift Pipelines の利用を検討してください。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--to=''`
  ビルドしたイメージをこのイメージストリームタグに push します（--to-docker を指定した場合はコンテナイメージリポジトリに push します）。

- `--to-docker=false`
  true の場合、ビルドの出力を Docker リポジトリに push します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc new-build --help` / `gen-oc-help.py` で生成</sub>
