# `oc adm restart-kubelet`

> 指定したノードで kubelet を再起動する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `restart-kubelet`

## Usage

```
oc adm restart-kubelet [options]
```

OCP v4 クラスタが提供する証明書を再生成します。

このコマンドは、変更がクラスタに反映されるのを待ちません。変更によっては、関わるオペレータやオペランドがそれぞれ異なるため、クラスタ全体に行き渡るまで非常に長い時間がかかることがあります。

実験的機能: このコマンドは現在活発に開発中であり、予告なく変更される可能性があります。

## Examples

```bash
# すべてのノードを 10% ずつ再起動する
oc adm restart-kubelet nodes --all --directive=RemoveKubeletKubeconfig

# すべてのノードを 20 台ずつ再起動する
oc adm restart-kubelet nodes --all --parallelism=20 --directive=RemoveKubeletKubeconfig

# すべてのノードを 15% ずつ再起動する
oc adm restart-kubelet nodes --all --parallelism=15% --directive=RemoveKubeletKubeconfig

# すべての master を同時に再起動する
oc adm restart-kubelet nodes -l node-role.kubernetes.io/master --parallelism=100% --directive=RemoveKubeletKubeconfig
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--command=''`
  kubelet の停止後、起動前に実行するコマンド。

- `--directive=''`
  kubelet の再起動時に、既知のコマンドを実行します: RemoveKubeletKubeconfig

- `--dry-run=false`
  サーバーサイドの dry run を使用する場合に true を設定します。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  リソースを特定する。

- `--local=false`
  true の場合、annotation は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--parallelism='10%'`
  parallelism は、同時に処理するノードの実数または割合です。

- `-R, --recursive=true`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!=' をサポートします（例: -l key1=value1,key2=value2）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm restart-kubelet --help` / `gen-oc-help.py` で生成</sub>
