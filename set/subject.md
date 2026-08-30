# `oc set subject`

> ロールバインディングまたはクラスタロールバインディング内のユーザー、グループ、サービスアカウントを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `subject`

## Usage

```
oc set subject (-f FILENAME | TYPE NAME) [--user=username] [--group=groupname] [--serviceaccount=namespace:serviceaccountname] [--dry-run=server|client|none] [options]
```

ロールバインディングまたはクラスタロールバインディング内のユーザー、グループ、サービスアカウントを更新します。

## Examples

```bash
# serviceaccount1 のクラスタロールバインディングを更新する
oc set subject clusterrolebinding admin --serviceaccount=namespace:serviceaccount1

# user1、user2、group1 のロールバインディングを更新する
oc set subject rolebinding admin --user=user1 --user=user2 --group=group1

# ロールバインディングのサブジェクトをローカルで更新した結果を、サーバーに接続せずに YAML 形式で表示する
oc create rolebinding admin --role=admin --user=admin -o yaml --dry-run | oc set subject --local -f - --user=foo -o yaml
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
  サブジェクトを更新するリソースのファイル名、ディレクトリ、または URL

- `--group=[]`
  ロールにバインドするグループ

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set subject は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--serviceaccount=[]`
  ロールにバインドするサービスアカウント

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--user=[]`
  ロールにバインドするユーザー名

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set subject --help` / `gen-oc-help.py` で生成</sub>
