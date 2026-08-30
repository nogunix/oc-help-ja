# `oc new-app`

> 新しいアプリケーションを作成する

[`oc`](oc.md) / `new-app`

## Usage

```
oc new-app (IMAGE | IMAGESTREAM | TEMPLATE | PATH | URL ...) [flags] [options]
```

ソースコード、テンプレート、イメージなどを指定して新しいアプリケーションを作成します。

このコマンドは、イメージ、テンプレート、または公開リポジトリを持つコードを使って、アプリケーションのコンポーネントを組み立てようとします。イメージは、ローカルのコンテナストレージ（利用可能な場合）、コンテナイメージレジストリ、統合イメージストリーム、保存済みテンプレートから検索されます。

ソースコードの URL を指定すると、そのソースコードを Pod 内で実行できるイメージに変換するビルドが設定されます。ローカルのソースは、サーバーから参照できるリモートリポジトリを持つ git リポジトリ内にある必要があります。イメージはデプロイメントまたはデプロイメント設定を通じてデプロイされ、アプリケーションの最初の公開ポートに Service が接続されます。各種フラグでコンポーネントを明示的に指定することも、指定した内容からどのようなコンポーネントかを oc new-app に自動判定させることもできます。

ソースコードを指定した場合、新しいビルドが自動的にトリガーされます。進捗は 'oc status' で確認できます。

## Examples

```bash
# アプリの作成に使えるローカルのテンプレートとイメージストリームをすべて一覧する
oc new-app --list

# 現在の git リポジトリ（パブリックなリモートを持つ）のソースコードとコンテナイメージを基にアプリケーションを作成する
oc new-app . --image=registry/repo/langimage

# バイナリ入力を前提とした Docker ビルドストラテジーで、myapp というアプリケーションを作成する
oc new-app  --strategy=docker --binary --name myapp

# 指定された [image]~[source code] の組み合わせを基に、Ruby アプリケーションを作成する
oc new-app centos/ruby-25-centos7~https://github.com/sclorg/ruby-ex.git

# パブリックなコンテナレジストリの MySQL イメージを使ってアプリを作成する。生成される成果物には db=mysql のラベルが付く
oc new-app mysql MYSQL_USER=user MYSQL_PASSWORD=pass MYSQL_DATABASE=testdb -l db=mysql

# プライベートレジストリの MySQL イメージを使ってアプリを作成し、アプリケーション成果物の名前を上書きする
oc new-app --image=myregistry.com/mycompany/mysql --name=private

# 完全なマニフェストリストを持つイメージを使ってアプリを作成し、アプリケーション成果物の名前を上書きする
oc new-app --image=myregistry.com/mycompany/image --name=private --import-mode=PreserveOriginal

# リモートリポジトリの beta4 ブランチを使ってアプリケーションを作成する
oc new-app https://github.com/openshift/ruby-hello-world#beta4

# 保存されたテンプレートを基に、パラメータ値を明示的に指定してアプリケーションを作成する
oc new-app --template=ruby-helloworld-sample --param=MYSQL_USER=admin

# リモートリポジトリからアプリケーションを作成し、コンテキストディレクトリを指定する
oc new-app https://github.com/youruser/yourgitrepo --context-dir=src/build

# リモートのプライベートリポジトリからアプリケーションを作成し、使用する既存のシークレットを指定する
oc new-app https://github.com/youruser/yourgitrepo --source-secret=yoursecret

# テンプレートファイルを基に、パラメータ値を明示的に指定してアプリケーションを作成する
oc new-app --file=./example/myapp/template.json --param=MYSQL_USER=admin

# すべてのテンプレート、イメージストリーム、コンテナイメージから "ruby" に一致するものを検索する
oc new-app --search ruby

# "ruby" を検索するが、保存済みテンプレートのみを対象にする（--template、--image-stream、--image
# を使って検索結果を絞り込める）
oc new-app --search --template=ruby

# 保存済みテンプレートから "ruby" を検索し、結果を YAML で出力する
oc new-app --search --template=ruby --output=yaml
```

## Options

- `--allow-missing-images=false`
  true の場合、ローカルにもレジストリにも見つからない参照先コンテナイメージであっても使用することを示します。

- `--allow-missing-imagestream-tags=false`
  true の場合、存在しないイメージストリームタグであっても使用することを示します。

- `--allow-missing-template-keys=false`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--as-deployment-config=false`
  true の場合、このアプリケーションをデプロイメント設定として作成します。これによりフックやカスタムストラテジーを利用できます。

- `--as-test=false`
  true の場合、このアプリケーションをテストデプロイとして作成します。デプロイが成功することを検証した後、スケールダウンします。

- `--binary=false`
  ソース URL を前提とする代わりに、ビルドがバイナリの内容を受け取るように設定します。トリガーは無効になります。

- `--build-env=[]`
  各ビルドイメージに設定する環境変数を、キーと値のペアで指定します。

- `--build-env-file=[]`
  各ビルドイメージに設定する環境変数を、キーと値のペアとして記述したファイル。

- `--code=[]`
  このアプリケーションのビルドに使用するソースコード。

- `--context-dir=''`
  ビルドで使用するコンテキストディレクトリ。

- `--dry-run=false`
  true の場合、操作を実行せずに結果だけを表示します。

- `-e, --env=[]`
  各コンテナに設定する環境変数を、キーと値のペアで指定します。

- `--env-file=[]`
  各コンテナに設定する環境変数を、キーと値のペアとして記述したファイル。

- `-f, --file=[]`
  アプリで使用するテンプレートファイルのパス。

- `--grant-install-rights=false`
  true の場合、アカウントへのアクセスを必要とするコンポーネントが、あなたのトークンを使ってプロジェクトにソフトウェアをインストールできます。信頼できるイメージにのみ、自分のトークンで実行する権限を与えてください。

- `--group=[]`
  まとめて 1 つのグループとして扱うコンポーネントを `<comp1>`+`<comp2>` の形式で指定します。

- `--ignore-unknown-parameters=false`
  true の場合、指定したパラメータがテンプレートに存在しなくても処理を中断しません。

- `--image=[]`
  アプリに含めるコンテナイメージの名前。注: レジストリやリポジトリを指定しない場合、クライアントのイメージ pull に適用されるデフォルト設定が使われます。

- `-i, --image-stream=[]`
  アプリのデプロイに使用する既存のイメージストリームの名前。

- `--import-mode=''`
  'PreserveOriginal' を指定した場合、タグの完全なマニフェストリストをインポートします。デフォルトは 'Legacy' です。

- `--insecure-registry=false`
  true の場合、参照先のコンテナイメージが非セキュアなレジストリ上にあり、証明書チェックを回避すべきであることを示します

- `-l, --labels=''`
  このアプリケーションのすべてのリソースに設定するラベル。

- `-L, --list=false`
  作成に使えるローカルのテンプレートとイメージストリームをすべて一覧表示します。

- `--name=''`
  生成されるアプリケーション成果物に使用する名前を設定します

- `--no-install=false`
  インストール可能と自称するイメージは実行しない

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--output-version=''`
  出力オブジェクトの優先 API バージョン

- `-p, --param=[]`
  テンプレート内のパラメータ値を設定 / 上書きするキーと値のペアを指定します（例: -p FOO=BAR）。

- `--param-file=[]`
  テンプレート内で設定 / 上書きするパラメータ値を記述したファイル。

- `-S, --search=false`
  指定した引数に一致するテンプレート、イメージストリーム、コンテナイメージをすべて検索します。注: コンテナイメージの検索は、ImageStreamImport API を通じて OpenShift クラスタ上で実行されます。

- `-a, --show-all=false`
  出力時に、すべてのリソースを表示します（デフォルトは終了済みの Pod を非表示）

- `--show-labels=false`
  出力時に、すべてのラベルを最後の列として表示します（デフォルトはラベル列を非表示）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--sort-by=''`
  空でない場合、指定したフィールド指定で一覧をソートします。フィールド指定は JSONPath 式で記述します（例: '{.metadata.name}'）。この JSONPath 式が指す API リソースのフィールドは、整数または文字列である必要があります。

- `--source-secret=''`
  プライベートな git リポジトリのクローンに使用する、既存のシークレットの名前。

- `--strategy=`
  自動判定させたくない場合に、使用するビルドストラテジー (docker|pipeline|source) を指定します。注意: pipeline ストラテジーは非推奨です。Jenkins 上で Jenkinsfile を直接使うか、OpenShift Pipelines の利用を検討してください。

- `--template=[]`
  アプリで使用する、保存済みテンプレートの名前。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc new-app --help` / `gen-oc-help.py` で生成</sub>
