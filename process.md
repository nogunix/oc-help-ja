# `oc process`

> テンプレートを処理してリソースのリストにする

[`oc`](oc.md) / `process`

## Usage

```
oc process (TEMPLATE | -f FILENAME) [-p=KEY=VALUE] [flags] [options]
```

ファイル名または標準入力で指定したテンプレートを処理し、リソースのリストにします。

テンプレートを使うと、作成や更新のためにサーバーへ送る前にリソースをパラメータ化できます。テンプレートは "パラメータ" を持ち、その値は作成時に生成することも、ユーザーが指定することもできます。また、テンプレート自体を説明するメタデータも持ちます。

process コマンドの出力は、常に 1 つ以上のリソースのリストです。この出力を（'-f -' オプションで）標準入力経由で create コマンドにパイプしたり、ファイルにリダイレクトしたりできます。

process はサーバー上でテンプレートを解決しますが、--local を指定するとローカルでパラメータを埋め込めます。ローカルで実行する場合、どのテンプレート変換がサポートされるかはサーバーではなくクライアントツールのバージョンで決まる点に注意してください。

## Examples

```bash
# template.json ファイルをリソースのリストに変換し、create に渡す
oc process -f template.json | oc create -f -

# サーバーに接続せず、ローカルでファイルを処理する
oc process -f template.json --local -o yaml

# ユーザー定義のラベルを渡しながらテンプレートを処理する
oc process -f template.json -l name=mytemplate

# 保存されたテンプレートをリソースのリストに変換する
oc process foo

# パラメータ値を設定 / 上書きして、保存されたテンプレートをリソースのリストに変換する
oc process foo PARM1=VALUE1 PARM2=VALUE2

# 別の namespace に保存されたテンプレートをリソースのリストに変換する
oc process openshift//foo

# template.json をリソースのリストに変換する
cat template.json | oc process -f -
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-f, --filename=''`
  テンプレートを読み込むファイル名または URL

- `--ignore-unknown-parameters=false`
  true の場合、指定したパラメータがテンプレートに存在しなくても処理を中断しません。

- `-l, --labels=''`
  このテンプレートのすべてのリソースに設定するラベル

- `--local=false`
  true の場合、サーバーに接続せずローカルでテンプレートを処理します。

- `-o, --output='json'`
  出力形式。次のいずれかを指定します: (json, yaml, name, describe, go-template-file, templatefile, template, go-template, jsonpath, jsonpath-file)。

- `-p, --param=[]`
  テンプレート内のパラメータ値を設定 / 上書きするキーと値のペアを指定します（例: -p FOO=BAR）。

- `--param-file=[]`
  テンプレート内で設定 / 上書きするテンプレートパラメータ値を記述したファイル。

- `--parameters=false`
  true の場合、処理は行わず、利用可能なパラメータを表示するだけにします

- `--raw=false`
  true の場合、テンプレートのオブジェクトではなく、処理後のテンプレートを出力します。-o describe を指定した場合は自動的に有効になります

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc process --help` / `gen-oc-help.py` で生成</sub>
