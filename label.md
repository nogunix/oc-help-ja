# `oc label`

> リソースのラベルを更新する

[`oc`](oc.md) / `label`

## Usage

```
oc label [--overwrite] (-f FILENAME | TYPE NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--resource-version=version] [options]
```

- ラベルのキーと値は英字または数字で始まる必要があり、英字・数字・ハイフン・ドット・アンダースコアを、それぞれ最大 63 文字まで含められます。
- キーの先頭には、example.com/my-app のように DNS サブドメインのプレフィックスと 1 つの '/' を付けることもできます。
- --overwrite が true の場合は既存のラベルを上書きできます。そうでない場合、ラベルを上書きしようとするとエラーになります。
- --resource-version を指定した場合はそのリソースバージョンで更新し、指定しない場合は既存のリソースバージョンを使用します。

## Examples

```bash
# Pod 'foo' にラベル 'unhealthy' を値 'true' で設定する
oc label pods foo unhealthy=true

# Pod 'foo' にラベル 'status' を値 'unhealthy' で設定し、既存の値があれば上書きする
oc label --overwrite pods foo status=unhealthy

# namespace 内のすべての Pod を更新する
oc label pods --all status=unhealthy

# "pod.json" の type と name で指定された Pod を更新する
oc label -f pod.json status=unhealthy

# リソースがバージョン 1 から変更されていない場合にのみ Pod 'foo' を更新する
oc label pods foo status=unhealthy --resource-version=1

# Pod 'foo' から、'bar' という名前のラベルがあれば削除する
# --overwrite フラグは不要です
oc label pods foo bar-
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `-A, --all-namespaces=false`
  true の場合、指定した操作をすべての namespace で確認します。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-label'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  ラベルを更新するリソースを特定するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--list=false`
  true の場合、指定したリソースのラベルを表示します。

- `--local=false`
  true の場合、label は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--overwrite=false`
  true の場合、ラベルの上書きを許可します。そうでない場合、既存のラベルを上書きする更新は拒否されます。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--resource-version=''`
  空でない場合、これがそのオブジェクトの現在の resource-version と一致するときにのみ、ラベルの更新が成功します。単一のリソースを指定した場合のみ有効です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc label --help` / `gen-oc-help.py` で生成</sub>
