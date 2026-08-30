# `oc adm ocp-certificates remove-old-trust`

> OpenShift クラスタで、プラットフォームの信頼バンドルを表す ConfigMap から古い CA を削除する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm ocp-certificates`](../ocp-certificates.md) / `remove-old-trust`

## Usage

```
oc adm ocp-certificates remove-old-trust [options]
```

プラットフォームが提供し、クラスタ全体の ConfigMap に保存されている CA 証明書バンドルを prune します。

このコマンドは、変更がクラスタに反映されるのを待ちません。変更によっては、関わるオペレータやオペランドがそれぞれ異なるため、クラスタ全体に行き渡るまで非常に長い時間がかかることがあります。

実験的機能: このコマンドは現在活発に開発中であり、予告なく変更される可能性があります。

## Examples

```bash
# 特定の config map に含まれる信頼バンドルを削除する
oc adm ocp-certificates remove-old-trust -n openshift-config-managed configmaps/kube-apiserver-aggregator-client-ca --created-before 2023-06-05T14:44:06Z

# すべての信頼バンドルから、特定の日付より前に作成された CA 証明書のみを削除する
oc adm ocp-certificates remove-old-trust configmaps -A --all --created-before 2023-06-05T14:44:06Z
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--created-before=''`
  この日付より前に作成された CA 証明書のみを削除します。形式: 2023-06-05T14:44:06Z

- `--dry-run=false`
  サーバーサイドの dry run を使用する場合に true を設定します。

- `--exclude-bundles=[]`
  信頼の prune 対象から除外する CA バンドル。複数回指定できます。形式: namespace/name

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

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm ocp-certificates remove-old-trust --help` / `gen-oc-help.py` で生成</sub>
