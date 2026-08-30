# `oc adm ocp-certificates regenerate-top-level`

> OpenShift クラスタのトップレベル証明書を再生成する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm ocp-certificates`](../ocp-certificates.md) / `regenerate-top-level`

## Usage

```
oc adm ocp-certificates regenerate-top-level [options]
```

OCP v4 クラスタが提供するルート証明書を再生成します。

このコマンドは、変更がクラスタに反映されるのを待ちません。変更によっては、関わるオペレータやオペランドがそれぞれ異なるため、クラスタ全体に行き渡るまで非常に長い時間がかかることがあります。

実験的機能: このコマンドは現在活発に開発中であり、予告なく変更される可能性があります。

## Examples

```bash
# 特定のシークレットに含まれる署名証明書を再生成する
oc adm ocp-certificates regenerate-top-level -n openshift-kube-apiserver-operator secret/loadbalancer-serving-signer-key
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

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

- `-R, --recursive=true`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!=' をサポートします（例: -l key1=value1,key2=value2）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--valid-before=''`
  この日付より前に有効なトップレベル証明書のみを再生成します。形式: 2023-06-05T14:44:06Z

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm ocp-certificates regenerate-top-level --help` / `gen-oc-help.py` で生成</sub>
