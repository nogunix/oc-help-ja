# `oc adm top node`

> ノードのリソース使用量 (CPU / メモリ) を表示する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm top`](../top.md) / `node`

## Usage

```
oc adm top node [NAME | -l label] [options]
```

top-node コマンドを使うと、ノードのリソース消費量を確認できます。

エイリアス: node, nodes, no

## Examples

```bash
# すべてのノードのメトリクスを表示する
oc adm top node

# 指定したノードのメトリクスを表示する
oc adm top node NODE_NAME
```

## Options

- `--no-headers=false`
  指定した場合、ヘッダーなしで出力します

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-capacity=false`
  ノードのリソースを、Allocatable（デフォルト）ではなく Capacity に基づいて表示します。

- `--show-swap=false`
  スワップメモリに関するノードのリソースを表示します。

- `--sort-by=''`
  空でない場合、指定したフィールドでノード一覧をソートします。フィールドには 'cpu' または 'memory' を指定できます。

- `--use-protocol-buffers=true`
  Metrics API へのアクセスに protocol-buffers を使用します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm top node --help` / `gen-oc-help.py` で生成</sub>
