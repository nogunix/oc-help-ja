# `oc adm build-chain`

> ビルドの入力と依存関係を出力する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `build-chain`

## Usage

```
oc adm build-chain IMAGESTREAMTAG [flags] [options]
```

生成されるグラフの形式としては、dot と人間が読みやすい形式がサポートされています。タグと namespace は省略可能で、指定しない場合はそれぞれ 'latest' とデフォルトの namespace が使用されます。

## Examples

```bash
# <image-stream> の 'latest' タグの依存関係ツリーを構築する
oc adm build-chain <image-stream>

# 'v2' タグの依存関係ツリーを dot 形式で構築し、dot ユーティリティで可視化する
oc adm build-chain <image-stream>:v2 -o dot | dot -T svg -o deps.svg

# 'test' namespace にある指定のイメージストリームタグについて、全 namespace を対象に依存関係ツリーを構築する
oc adm build-chain <image-stream> -n test --all
```

## Options

- `--all=false`
  true の場合、指定したイメージストリームタグについて、全 namespace を対象に依存関係ツリーを構築します

- `-o, --output=''`
  依存関係ツリーの出力形式

- `--reverse=false`
  true の場合、その istag に依存しているものではなく、その istag が依存しているものを表示します。

- `--trigger-only=true`
  true の場合、ビルドトリガーに基づく依存関係のみを含めます。false の場合はすべての依存関係を含めます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm build-chain --help` / `gen-oc-help.py` で生成</sub>
