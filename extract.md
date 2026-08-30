# `oc extract`

> シークレットまたは config map をディスクに取り出す

[`oc`](oc.md) / `extract`

## Usage

```
oc extract RESOURCE/NAME [--to=DIRECTORY] [--keys=KEY ...] [flags] [options]
```

シークレットと config map からファイルを取り出します。

extract コマンドを使うと、config map やシークレットの内容を簡単にディレクトリへダウンロードできます。config map やシークレットの各キーは、コンテナにシークレットや config map をマウントしたときと同じように、キー名を持つ個別のファイルとして作成されます。

--to オプションに '-' を渡すと、シークレットや config map の内容を標準出力に取り出せます。各キーの名前は標準エラー出力に書き出されます。

--keys=NAME フラグで取り出すキーを絞り込んだり、--to=DIRECTORY で取り出し先のディレクトリを指定したりできます。

## Examples

```bash
# シークレット "test" をカレントディレクトリに取り出す
oc extract secret/test

# config map "nginx" を /tmp ディレクトリに取り出す
oc extract configmap/nginx --to=/tmp

# config map "nginx" を標準出力に取り出す
oc extract configmap/nginx --to=-

# config map "nginx" からキー "nginx.conf" だけを /tmp ディレクトリに取り出す
oc extract configmap/nginx --to=/tmp --keys=nginx.conf
```

## Options

- `--confirm=false`
  true の場合、既に存在するファイルを上書きします。

- `-f, --filename=[]`
  取り出すリソースを特定するファイル名、ディレクトリ、または URL。

- `--keys=[]`
  抽出するキーのリスト（省略可。デフォルトはすべてのキー）。

- `--to='.'`
  ファイルの展開先ディレクトリ。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc extract --help` / `gen-oc-help.py` で生成</sub>
