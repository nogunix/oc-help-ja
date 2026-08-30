# `oc attach`

> 実行中のコンテナにアタッチする

[`oc`](oc.md) / `attach`

## Usage

```
oc attach (POD | TYPE/NAME) -c CONTAINER [options]
```

既存のコンテナ内ですでに実行中のプロセスにアタッチします。

## Examples

```bash
# 実行中の Pod mypod から出力を取得する。'oc.kubernetes.io/default-container' アノテーションを使用する
# アタッチ対象のコンテナ選択に使われ、それも無ければ Pod 内の最初のコンテナが選ばれます
oc attach mypod

# Pod mypod の ruby-container から出力を取得する
oc attach mypod -c ruby-container

# raw ターミナルモードに切り替え、Pod mypod の ruby-container 内の 'bash' に標準入力を送る
# 'bash' の標準出力 / 標準エラー出力をクライアントに返す
oc attach mypod -c ruby-container -i -t

# nginx という名前のレプリカセットの最初の Pod から出力を取得する
oc attach rs/nginx
```

## Options

- `-c, --container=''`
  コンテナ名。省略した場合は、アタッチ対象のコンテナ選択に kubectl.kubernetes.io/default-container アノテーションが使われ、それも無ければ Pod 内の最初のコンテナが選ばれます

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

<sub>`$ oc attach --help` / `gen-oc-help.py` で生成</sub>
