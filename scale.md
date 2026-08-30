# `oc scale`

> デプロイメント、レプリカセット、またはレプリケーションコントローラーの新しいサイズを設定する

[`oc`](oc.md) / `scale`

## Usage

```
oc scale [--resource-version=version] [--current-replicas=count] --replicas=COUNT (-f FILENAME | TYPE NAME) [options]
```

デプロイメント、レプリカセット、レプリケーションコントローラー、またはステートフルセットの新しいサイズを設定します。

scale では、スケール操作に対する前提条件を 1 つ以上指定することもできます。

--current-replicas または --resource-version を指定した場合、スケール実行前に検証が行われ、スケール要求をサーバーに送る時点でその前提条件が満たされていることが保証されます。

## Examples

```bash
# 'foo' という名前のレプリカセットを 3 にスケールする
oc scale --replicas=3 rs/foo

# "foo.yaml" で指定された type と name のリソースを 3 にスケールする
oc scale --replicas=3 -f foo.yaml

# mysql という名前のデプロイメントの現在のサイズが 2 であれば、mysql を 3 にスケールする
oc scale --current-replicas=2 --replicas=3 deployment/mysql

# 複数のレプリケーションコントローラーをスケールする
oc scale --replicas=5 rc/example1 rc/example2 rc/example3

# 'web' という名前のステートフルセットを 3 にスケールする
oc scale --replicas=3 statefulset/web
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--current-replicas=-1`
  現在のサイズに対する前提条件。スケールするには、リソースの現在のサイズがこの値と一致している必要があります。-1（デフォルト）で条件なしになります。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-f, --filename=[]`
  新しいサイズを設定するリソースを特定するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--replicas=0`
  希望する新しいレプリカ数。必須です。

- `--resource-version=''`
  リソースバージョンに対する前提条件。スケールするには、現在のリソースバージョンがこの値と一致している必要があります。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--timeout=0s`
  スケール操作を諦めるまでの待ち時間。0 は待たないことを意味します。それ以外の値には対応する時間の単位を付けてください（例: 1s、2m、3h）。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc scale --help` / `gen-oc-help.py` で生成</sub>
