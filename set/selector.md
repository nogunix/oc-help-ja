# `oc set selector`

> リソースにセレクターを設定する

[`oc`](../oc.md) / [`oc set`](../set.md) / `selector`

## Usage

```
oc set selector (-f FILENAME | TYPE NAME) EXPRESSIONS [--resource-version=version] [options]
```

リソースにセレクターを設定します。なお、'set selector' の実行前にリソースがセレクターを持っていた場合、新しいセレクターで上書きされます。

セレクターは英字または数字で始まる必要があり、英字・数字・ハイフン・ドット・アンダースコアを oc 文字まで含められます。--resource-version を指定した場合はそのリソースバージョンで更新し、指定しない場合は既存のリソースバージョンを使用します。注: 現時点でセレクターを設定できるのは Service オブジェクトのみです。

## Examples

```bash
# デプロイメントと Service のペアを作成する前に、ラベルとセレクターを設定する
oc create service clusterip my-svc --clusterip="None" -o yaml --dry-run | oc set selector --local -f - 'environment=qa' -o yaml | oc create -f -
oc create deployment my-dep -o yaml --dry-run | oc label --local -f - environment=qa -o yaml | oc create -f -
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
  リソースを特定する。

- `--local=false`
  true の場合、annotation は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=true`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--resource-version=''`
  空でない場合、これがそのオブジェクトの現在の resource-version と一致するときにのみ、セレクターの更新が成功します。単一のリソースを指定した場合のみ有効です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set selector --help` / `gen-oc-help.py` で生成</sub>
