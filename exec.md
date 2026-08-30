# `oc exec`

> コンテナ内でコマンドを実行する

[`oc`](oc.md) / `exec`

## Usage

```
oc exec (POD | TYPE/NAME) [-c CONTAINER] [flags] -- COMMAND [args...] [options]
```

## Examples

```bash
# Pod mypod で 'date' コマンドを実行し、その出力を取得する（コンテナはデフォルトで最初のもの）
oc exec mypod -- date

# Pod mypod の ruby-container で 'date' コマンドを実行し、その出力を取得する
oc exec mypod -c ruby-container -- date

# raw ターミナルモードに切り替え、Pod mypod の ruby-container 内の 'bash' に標準入力を送る
# 'bash' の標準出力 / 標準エラー出力をクライアントに返す
oc exec mypod -c ruby-container -i -t -- bash -il

# Pod mypod の最初のコンテナで /usr の内容を一覧し、更新時刻順に並べる
# Pod 内で実行したいコマンドに共通のフラグ（-i など）が含まれる場合は、
# コマンドのフラグ / 引数を区切るために、2 つのダッシュ (--) を使う必要があります
# また、コマンドとそのフラグ / 引数をクォートで囲まないでください
# 普段そう実行している場合を除きます（つまり ls -t /usr であって、"ls -t /usr" ではありません）
oc exec mypod -i -t -- ls -t /usr

# デプロイメント mydeployment の最初の Pod で 'date' コマンドを実行し、その出力を取得する（コンテナはデフォルトで最初のもの）
oc exec deploy/mydeployment -- date

# Service myservice の最初の Pod で 'date' コマンドを実行し、その出力を取得する（コンテナはデフォルトで最初のもの）
oc exec svc/myservice -- date
```

## Options

- `-c, --container=''`
  コンテナ名。省略した場合は、アタッチ対象のコンテナ選択に kubectl.kubernetes.io/default-container アノテーションが使われ、それも無ければ Pod 内の最初のコンテナが選ばれます

- `-f, --filename=[]`
  リソース内で exec するために使用する

- `--pod-running-timeout=1m0s`
  少なくとも 1 つの Pod が実行状態になるまで待つ時間（5s、2m、3h のような 0 より大きい値）

- `-q, --quiet=false`
  リモートセッションからの出力のみを表示します

- `-i, --stdin=false`
  標準入力をコンテナに渡します

- `-t, --tty=false`
  標準入力は TTY です

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc exec --help` / `gen-oc-help.py` で生成</sub>
