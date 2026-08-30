# `oc set serviceaccount`

> リソースのサービスアカウントを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `serviceaccount`

## Usage

```
oc set serviceaccount (-f FILENAME | TYPE NAME) SERVICE_ACCOUNT [options]
```

Pod テンプレートを持つリソースの ServiceAccount を更新します。

エイリアス: serviceaccount, sa

## Examples

```bash
# デプロイメント nginx-deployment のサービスアカウントを serviceaccount1 に設定する
oc set serviceaccount deployment nginx-deployment serviceaccount1

# ローカルファイルの nginx デプロイメントにサービスアカウントを設定した結果を、API サーバーに接続せずに YAML 形式で表示する
oc set sa -f nginx-deployment.yaml serviceaccount1 --local --dry-run -o yaml
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set serviceaccount は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set serviceaccount --help` / `gen-oc-help.py` で生成</sub>
