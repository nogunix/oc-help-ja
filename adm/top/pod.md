# `oc adm top pod`

> Pod のリソース使用量 (CPU / メモリ) を表示する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm top`](../top.md) / `pod`

## Usage

```
oc adm top pod [NAME | -l label] [options]
```

'top pod' コマンドを使うと、Pod のリソース消費量を確認できます。

メトリクスパイプラインの遅延により、Pod 作成から数分間はデータを取得できないことがあります。

エイリアス: pod, pods, po

## Examples

```bash
# default namespace のすべての Pod のメトリクスを表示する
oc adm top pod

# 指定した namespace のすべての Pod のメトリクスを表示する
oc adm top pod --namespace=NAMESPACE

# 指定した Pod とそのコンテナのメトリクスを表示する
oc adm top pod POD_NAME --containers

# ラベル name=myLabel で指定される Pod のメトリクスを表示する
oc adm top pod -l name=myLabel
```

## Options

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--containers=false`
  指定した場合、Pod 内のコンテナごとの使用量を表示します。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `--no-headers=false`
  指定した場合、ヘッダーなしで出力します。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-swap=false`
  スワップメモリに関する Pod のリソースを表示します。

- `--sort-by=''`
  空でない場合、指定したフィールドで Pod 一覧をソートします。フィールドには 'cpu' または 'memory' を指定できます。

- `--sum=false`
  リソース使用量の合計を表示します

- `--use-protocol-buffers=true`
  Metrics API へのアクセスに protocol-buffers を使用します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm top pod --help` / `gen-oc-help.py` で生成</sub>
