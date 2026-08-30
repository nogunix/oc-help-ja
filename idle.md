# `oc idle`

> スケール可能なリソースをアイドル化する

[`oc`](oc.md) / `idle`

## Usage

```
oc idle (SERVICE_ENDPOINTS... | -l label | --all | --resource-names-file FILENAME) [flags] [options]
```

アイドル化では、Service のエンドポイントを調べることで、その Service 群に紐づくスケール可能なリソース（デプロイメント設定やレプリケーションコントローラーなど）を検出します。その上で各 Service にアイドル済みの印を付け、関連リソースを記録し、リソースをレプリカ 0 までスケールダウンします。

ネットワークトラフィックを受け取ると、その Service（および関連するルート）は、関連リソースを以前のスケールまで戻して "起こし" ます。

## Examples

```bash
# to-idle.txt に列挙された Service に紐づく、スケール可能なコントローラーをアイドル化する
$ oc idle --resource-names-file to-idle.txt
```

## Options

- `--all=false`
  true の場合、namespace 内のすべての Service を選択します

- `-A, --all-namespaces=false`
  true の場合、すべての namespace の Service を選択します

- `--dry-run=false`
  true の場合、対象オブジェクトへのアノテーション付与やアイドル化は行わず、書き込まれる予定のアノテーションを表示するだけにします

- `--resource-names-file=''`
  アイドル化対象のスケール可能なリソースを持つ Service の一覧を記載したファイル

- `-l, --selector=''`
  Service の選択に使用するセレクター（ラベルクエリ）

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc idle --help` / `gen-oc-help.py` で生成</sub>
