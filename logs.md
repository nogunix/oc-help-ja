# `oc logs`

> Pod 内のコンテナのログを表示する

[`oc`](oc.md) / `logs`

## Usage

```
oc logs [-f] [-p] (POD | TYPE/NAME) [-c CONTAINER] [flags] [options]
```

リソースのログを表示します。

サポートされるリソースは、ビルド、ビルド設定 (bc)、デプロイメント設定 (dc)、Pod です。Pod を指定し、その Pod に複数のコンテナがある場合は、-c でコンテナ名を指定してください。ビルド設定やデプロイメント設定を指定した場合は、--version で特定のバージョンのログを表示できます。

Pod が起動に失敗している場合は、--previous オプションで直前の試行のログを確認する必要があるかもしれません。

## Examples

```bash
# openldap ビルド設定の最新ビルドのログのストリーミングを開始する
oc logs -f bc/openldap

# mysql デプロイメント設定の最新デプロイのログのストリーミングを開始する
oc logs -f dc/mysql

# mysql デプロイメント設定の最初のデプロイのログを取得する。なお、ログは
# デプロイが成功したか、デプロイの prune や手動削除が行われたため、古いデプロイのログは
# 存在しないこともあります
oc logs --version=1 dc/mysql

# Pod backend の ruby-container のログのスナップショットを取得する
oc logs backend -c ruby-container

# Pod backend の ruby-container のログのストリーミングを開始する
oc logs -f pod/backend -c ruby-container
```

## Options

- `--all-containers=false`
  Pod 内のすべてのコンテナのログを取得します。

- `--all-pods=false`
  すべての Pod のログを取得します。prefix を true に設定します。

- `-c, --container=''`
  このコンテナのログを表示する

- `-f, --follow=false`
  ログをストリーミングするかどうかを指定します。

- `--ignore-errors=false`
  Pod のログを watch / follow している場合に、発生したエラーを致命的として扱わないようにします

- `--insecure-skip-tls-verify-backend=false`
  ログの取得元となる kubelet の identity 検証をスキップします。理論上、攻撃者が不正なログ内容を返す可能性があります。kubelet のサービング証明書が失効している場合などに使用するとよいでしょう。

- `--limit-bytes=0`
  返すログの最大バイト数。デフォルトは無制限です。

- `--max-log-requests=5`
  セレクターで指定した場合に、同時に follow するログの最大数を指定します。デフォルトは 5 です。

- `--pod-running-timeout=20s`
  少なくとも 1 つの Pod が実行状態になるまで待つ時間（5s、2m、3h のような 0 より大きい値）

- `--prefix=false`
  各ログ行の先頭に、そのログの出所（Pod 名とコンテナ名）を付けます

- `-p, --previous=false`
  true の場合、Pod 内のコンテナの以前のインスタンスが存在すれば、そのログを表示します。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--since=0s`
  5s、2m、3h のような相対時間より新しいログのみを返します。デフォルトはすべてのログです。since-time と since は同時に指定できません。

- `--since-time=''`
  指定した日時 (RFC3339) 以降のログのみを返します。デフォルトはすべてのログです。since-time と since は同時に指定できません。

- `--tail=-1`
  表示する最近のログの行数。セレクターを指定しない場合のデフォルトは -1 ですべての行を表示し、セレクターを指定した場合は 10 行になります。

- `--timestamps=false`
  ログ出力の各行にタイムスタンプを付けます

- `--version=0`
  0 より大きいバージョンを指定して、特定のビルドまたはデプロイのログを表示する

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc logs --help` / `gen-oc-help.py` で生成</sub>
