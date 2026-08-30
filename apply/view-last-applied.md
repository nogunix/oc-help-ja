# `oc apply view-last-applied`

> リソース / オブジェクトの最新の last-applied-configuration アノテーションを表示する

[`oc`](../oc.md) / [`oc apply`](../apply.md) / `view-last-applied`

## Usage

```
oc apply view-last-applied (TYPE [NAME | -l label] | TYPE/NAME | -f FILENAME) [options]
```

type/name またはファイルを指定して、最新の last-applied-configuration アノテーションを表示します。

デフォルトでは、出力は YAML 形式で標準出力に表示されます。-o オプションで出力形式を変更できます。

## Examples

```bash
# type/name を指定して last-applied-configuration アノテーションを YAML で表示する
oc apply view-last-applied deployment/nginx

# ファイルを指定して last-applied-configuration アノテーションを JSON で表示する
oc apply view-last-applied -f deploy.yaml -o json
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `-f, --filename=[]`
  last-applied-configuration アノテーションを含むファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output='yaml'`
  出力形式。(yaml, json) のいずれかを指定します

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc apply view-last-applied --help` / `gen-oc-help.py` で生成</sub>
