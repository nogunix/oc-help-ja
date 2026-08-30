# `oc rsync`

> ローカルファイルシステムと Pod の間でファイルをコピーする

[`oc`](oc.md) / `rsync`

## Usage

```
oc rsync SOURCE DESTINATION [flags] [options]
```

ローカルファイルを Pod のコンテナとの間でコピーします。

このコマンドは、リモートのコンテナとの間でローカルファイルをコピーします。コピーには OS の rsync コマンドを使い、変更されたファイルのみを転送します。最適な性能を得るには、ローカルに rsync をインストールしてください。UNIX 系システムではパッケージマネージャを使い、Windows では https://www.itefix.net/cwrsync から cwRsync をインストールします。

コンテナを指定しない場合、Pod 内の最初のコンテナがコピーに使用されます。

デフォルトでは、次のフラグが rsync に渡されます: --archive --no-owner --no-group --omit-dir-times --numeric-ids

## Examples

```bash
# ローカルディレクトリを Pod のディレクトリと同期する
oc rsync ./local/dir/ POD:/remote/dir

# Pod のディレクトリをローカルディレクトリと同期する
oc rsync POD:/remote/dir/ ./local/dir
```

## Options

- `--compress=false`
  転送中にファイルデータを圧縮します

- `-c, --container=''`
  Pod 内のコンテナ

- `--delete=false`
  true の場合、コピー元に存在しないファイルを削除します

- `--exclude=[]`
  指定した場合、パターンに一致するファイルを除外します

- `--include=[]`
  指定した場合、パターンに一致するファイルを含めます

- `--no-perms=false`
  true の場合、権限を移譲しません

- `--progress=false`
  true の場合、転送中の進捗を表示します

- `-q, --quiet=false`
  エラー以外のメッセージを抑制します

- `--strategy=''`
  コピーに使用する方式を指定します: rsync、rsync-daemon、tar のいずれか

- `-w, --watch=false`
  ディレクトリの変更を監視して自動的に再同期する

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rsync --help` / `gen-oc-help.py` で生成</sub>
