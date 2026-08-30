# `oc describe`

> 特定のリソース、またはリソース群の詳細を表示する

[`oc`](oc.md) / `describe`

## Usage

```
oc describe (-f FILENAME | TYPE [NAME_PREFIX | -l label] | TYPE/NAME) [options]
```

選択したリソースについて、イベントやコントローラーなどの関連リソースを含む詳細な説明を表示します。名前で 1 つのオブジェクトを選ぶ、その種類のすべてのオブジェクトを選ぶ、名前のプレフィックスを指定する、ラベルセレクターを指定する、といった方法があります。例:

        $ oc describe TYPE NAME_PREFIX
まず TYPE と NAME_PREFIX の完全一致を確認します。該当するリソースが無い場合は、NAME_PREFIX で始まる名前を持つすべてのリソースの詳細を出力します。

サポートされているリソースの完全な一覧は "oc api-resources" で確認できます。

## Examples

```bash
# ノードの詳細を表示する
oc describe nodes kubernetes-node-emt8.c.myproject.internal

# Pod の詳細を表示する
oc describe pods/nginx

# "pod.json" の type と name で指定された Pod の詳細を表示する
oc describe -f pod.json

# すべての Pod の詳細を表示する
oc describe pods

# ラベル name=myLabel で Pod の詳細を表示する
oc describe pods -l name=myLabel

# 'frontend' レプリケーションコントローラーが管理するすべての Pod の詳細を表示する
# （rc が作成した Pod は、Pod 名の先頭に rc の名前が付きます）
oc describe pods frontend
```

## Options

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--chunk-size=500`
  大きなリストを一度に返さず、チャンクに分けて返します。0 を指定すると無効になります。

- `-f, --filename=[]`
  詳細を表示するリソースを含むファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-events=true`
  true の場合、対象オブジェクトに関連するイベントを表示します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc describe --help` / `gen-oc-help.py` で生成</sub>
