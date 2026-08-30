# `oc start-build`

> 新しいビルドを開始する

[`oc`](oc.md) / `start-build`

## Usage

```
oc start-build (BUILDCONFIG | --from-build=BUILD) [flags] [options]
```

ビルドを開始します。

このコマンドは、指定したビルド設定の新しいビルドを開始するか、--from-build=`<name>` で既存のビルドをコピーします。ビルドの出力を確認するには --follow フラグを指定してください。

さらに、--from-file、--from-dir、--from-repo フラグで、ファイル・ディレクトリ・ソースコードリポジトリを直接ビルドに渡せます。その内容はビルドにストリーミングされ、現在のビルドソース設定を上書きします。--from-repo を使う場合、--commit フラグでサーバーに送るブランチ・タグ・コミットを指定できます。--from-file を指定した場合、そのファイルは空のディレクトリのルートに同じファイル名で置かれます。--from-file と --from-archive には http または https の URL も指定できますが、認証はサポートされておらず、https の場合は証明書が有効で、システムに認識されている必要があります。

バイナリ入力からトリガーされたビルドは、サーバー上にソースを保持しません。そのため、ベースイメージの変更でトリガーされた再ビルドでは、ビルド設定に指定されたソースが使用されます。

## Examples

```bash
# ビルド設定 "hello-world" からビルドを開始する
oc start-build hello-world

# 以前のビルド "hello-world-1" を基にビルドを開始する
oc start-build --from-build=hello-world-1

# ディレクトリの内容をビルドの入力として使う
oc start-build hello-world --from-dir=src/

# Git リポジトリの内容を、タグ 'v2' の状態でサーバーに送る
oc start-build hello-world --from-repo=../hello-world --commit=v2

# ビルド設定 "hello-world" の新しいビルドを開始し、ビルドが完了するまでログを監視する
# 完了または失敗する
oc start-build hello-world --follow

# ビルド設定 "hello-world" の新しいビルドを開始し、完了するまで待つ。これは
# ビルドが失敗した場合は 0 以外の終了コードで終了する
oc start-build hello-world --wait
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--build-arg=[]`
  ビルド時に Docker へ渡すキーと値のペアを指定します。

- `--build-loglevel=''`
  ビルドログ出力のログレベルを指定します

- `--commit=''`
  ビルドが使用するソースコードのコミット識別子を指定します。Git リポジトリを基にしたビルドが必要です

- `-e, --env=[]`
  ビルドコンテナに設定する環境変数を、キーと値のペアで指定します。

- `--exclude='(^|/)\.git(/|$)'`
  --from-dir オプションを使う場合に、ソースツリーからビルド対象外とするファイルを選ぶための正規表現。デフォルトでは '.git' ディレクトリが除外されます（構文は https://golang.org/pkg/regexp を参照。ただし "" はすべてのファイルを許可し、何も除外しない意味に解釈される点に注意してください）

- `-F, --follow=false`
  ビルドを開始し、完了または失敗するまでログを監視する

- `--from-archive=''`
  ビルド前に展開し、バイナリ入力として使用するアーカイブ（tar、tar.gz、zip）。

- `--from-build=''`
  再実行するビルドの名前を指定します

- `--from-dir=''`
  アーカイブしてビルドのバイナリ入力として使用するディレクトリ。

- `--from-file=''`
  ビルドのバイナリ入力として使用するファイル（例: pom.xml や Dockerfile）。ビルドソースはこのファイルのみになります。

- `--from-repo=''`
  ビルドのバイナリ入力として使用する、ローカルのソースコードリポジトリのパス。

- `--from-webhook=''`
  既存のビルド設定をトリガーするための汎用 Webhook の URL を表示する

- `--git-post-receive=''`
  ビルドをトリガーする post-receive フックの内容

- `--git-repository=''`
  post-receive 用の git リポジトリのパス。デフォルトはカレントディレクトリです

- `--incremental=false`
  source ストラテジーのビルドにおける incremental 設定を上書きします。指定しない場合は無視されます

- `--list-webhooks=''`
  指定したビルド設定またはビルドの Webhook を一覧します。'all'、'generic'、'github' を指定できます

- `--no-cache=false`
  docker ストラテジーのビルドにおける noCache 設定を上書きします。指定しない場合は無視されます

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `-w, --wait=false`
  ビルドの完了を待ち、失敗した場合は 0 以外の終了コードで終了する

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc start-build --help` / `gen-oc-help.py` で生成</sub>
