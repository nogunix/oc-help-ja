# `oc annotate`

> リソースのアノテーションを更新する

[`oc`](oc.md) / `annotate`

## Usage

```
oc annotate [--overwrite] (-f FILENAME | TYPE NAME) KEY_1=VAL_1 ... KEY_N=VAL_N [--resource-version=version] [options]
```

1 つ以上のリソースのアノテーションを更新します。

Kubernetes のすべてのオブジェクトは、アノテーションとして追加データをオブジェクトに保存できます。アノテーションはキー / 値のペアで、ラベルより大きなデータを持てるほか、構造化された JSON のような任意の文字列値も格納できます。ツールやシステム拡張が独自のデータを保存する用途にも使われます。

既に存在するアノテーションを設定しようとすると、--overwrite が指定されていない限り失敗します。--resource-version を指定し、それがサーバー上の現在のリソースバージョンと一致しない場合、コマンドは失敗します。

サポートされているリソースの完全な一覧は "oc api-resources" で確認できます。

## Examples

```bash
# Pod 'foo' にアノテーション 'description' を値 'my frontend' で設定する
# 同じアノテーションを複数回設定した場合、最後の値だけが適用されます
oc annotate pods foo description='my frontend'

# "pod.json" の type と name で指定された Pod を更新する
oc annotate -f pod.json description='my frontend'

# Pod 'foo' にアノテーション 'description' を値 'my frontend running nginx' で設定し、既存の値があれば上書きする
oc annotate --overwrite pods foo description='my frontend running nginx'

# namespace 内のすべての Pod を更新する
oc annotate pods --all description='my frontend running nginx'

# リソースがバージョン 1 から変更されていない場合にのみ Pod 'foo' を更新する
oc annotate pods foo description='my frontend running nginx' --resource-version=1

# Pod 'foo' から、'description' という名前のアノテーションがあれば削除する
# --overwrite フラグは不要です
oc annotate pods foo description-
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します。

- `-A, --all-namespaces=false`
  true の場合、指定した操作をすべての namespace で確認します。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-annotate'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  アノテーションを更新するリソースを特定するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--list=false`
  true の場合、指定したリソースのアノテーションを表示します。

- `--local=false`
  true の場合、annotation は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--overwrite=false`
  true の場合、アノテーションの上書きを許可します。そうでない場合、既存のアノテーションを上書きする更新は拒否されます。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--resource-version=''`
  空でない場合、これがそのオブジェクトの現在の resource-version と一致するときにのみ、アノテーションの更新が成功します。単一のリソースを指定した場合のみ有効です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc annotate --help` / `gen-oc-help.py` で生成</sub>
