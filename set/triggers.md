# `oc set triggers`

> 1 つ以上のオブジェクトのトリガーを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `triggers`

## Usage

```
oc set triggers RESOURCE/NAME [--from-config|--from-image|--from-github|--from-webhook] [--auto|--manual] [flags] [options]
```

トリガーを設定または削除します。

ビルド設定、デプロイメント設定、および Kubernetes のほとんどのワークロードオブジェクトは、イメージが変更されたときに新しいデプロイやビルドを作成するトリガーを持てます。このコマンドでは、それらのトリガーを変更できます（自動 / 手動の切り替え、エントリの追加、既存エントリの変更など）。

デプロイメントは、イメージの変更と設定の変更をトリガーにできます。設定の変更とは Pod テンプレートへの任意の変更を指し、イメージの変更では、イメージストリームタグが更新されるたびにコンテナイメージの値が更新されます。Kubernetes のステートフルセット、デーモンセット、デプロイメント、cron job もイメージからトリガーできます。設定変更トリガーを無効にすることは、ほとんどのオブジェクトにとって一時停止と同じ意味になります。デプロイメント設定は、すべてのイメージ変更トリガーが登録されるまで最初のデプロイを実行しません。

ビルド設定は、イメージの変更、設定の変更、Webhook をトリガーにできます。ビルド設定の設定変更トリガーは、最初のビルドのみをトリガーします。

## Examples

```bash
# デプロイメント設定 'myapp' のトリガーを表示する
oc set triggers dc/myapp

# すべてのトリガーを手動に設定する
oc set triggers dc/myapp --manual

# すべての自動トリガーを有効にする
oc set triggers dc/myapp --auto

# ビルドの GitHub Webhook のシークレットを、新しく生成した値にリセットする
oc set triggers bc/webapp --from-github
oc set triggers bc/webapp --from-webhook

# すべてのトリガーを削除する
oc set triggers bc/webapp --remove-all

# 設定変更によるトリガーを停止する
oc set triggers dc/myapp --from-config --remove

# ビルド設定にイメージトリガーを追加する
oc set triggers bc/webapp --from-image=namespace1/image:latest

# ステートフルセットのメインコンテナにイメージトリガーを追加する
oc set triggers statefulset/db --from-image=namespace1/image:latest -c main
```

## Options

- `--all=false`
  true の場合、指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--auto=false`
  true の場合、すべてのトリガー、または指定したトリガーを有効にします

- `-c, --containers=''`
  デプロイメント上でこのトリガーを適用するコンテナ名のカンマ区切りリスト。デフォルトは、コンテナが 1 つだけの場合その名前

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `--from-bitbucket=false`
  true の場合、Bitbucket の Webhook を作成します。シークレット値は自動生成されます

- `--from-config=false`
  設定した場合、設定の変更によって変更がトリガーされます

- `--from-github=false`
  true の場合、GitHub の Webhook を作成します。シークレット値は自動生成されます

- `--from-gitlab=false`
  true の場合、GitLab の Webhook を作成します。シークレット値は自動生成されます

- `--from-image=''`
  トリガー元とするイメージストリームタグ

- `--from-webhook=false`
  true の場合、汎用 Webhook を作成します。シークレット値は自動生成されます

- `--from-webhook-allow-env=false`
  true の場合、環境変数を渡せる汎用 Webhook を作成します。シークレット値は自動生成されます

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `--manual=false`
  true の場合、すべてのトリガー、または指定したトリガーを手動に設定します

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove=false`
  true の場合、指定したトリガーを削除します。

- `--remove-all=false`
  true の場合、すべてのトリガーを削除します。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set triggers --help` / `gen-oc-help.py` で生成</sub>
