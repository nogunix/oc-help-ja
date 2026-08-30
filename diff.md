# `oc diff`

> 稼働中のバージョンと、適用した場合のバージョンの差分を表示する

[`oc`](oc.md) / `diff`

## Usage

```
oc diff -f FILENAME [options]
```

ファイル名または標準入力で指定した設定について、現在オンライン上にある設定と、適用した場合の設定との差分を表示します。

出力は常に YAML です。

KUBECTL_EXTERNAL_DIFF 環境変数で、独自の diff コマンドを指定できます。パラメータ付きの外部コマンドも使用できます。例: KUBECTL_EXTERNAL_DIFF="colordiff -N -u"

デフォルトでは、PATH 上にある "diff" コマンドが "-u"（unified diff）と "-N"（存在しないファイルを空として扱う）オプション付きで実行されます。

終了ステータス: 0 差分なし。 1 差分あり。 >1 kubectl または diff がエラーで失敗。

注: KUBECTL_EXTERNAL_DIFF を使用する場合は、その規約に従うことが前提です。

## Examples

```bash
# pod.json に含まれるリソースの差分を表示する
oc diff -f pod.json

# 標準入力から読み込んだファイルの差分を表示する
cat service.yaml | oc diff -f -
```

## Options

- `--concurrency=1`
  稼働中のバージョンと差分を取る際に、並列処理するオブジェクトの数。大きくすると速くなりますが、その短い時間により多くのメモリ・I/O・CPU を消費します。

- `--field-manager='kubectl-client-side-apply'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  差分を取る設定を含むファイル名、ディレクトリ、または URL

- `--force-conflicts=false`
  true の場合、サーバーサイド apply は競合があっても変更を強制適用します。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--prune=false`
  prune によって削除されるリソースを含めます。-l と併用でき、デフォルトでは prune 対象となるすべてのリソースを表示します

- `--prune-allowlist=[]`
  --prune のデフォルトの許可リストを <group/version/kind> で上書きします

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--server-side=false`
  true の場合、apply はクライアントではなくサーバー側で実行されます。

- `--show-managed-fields=false`
  true の場合、managed fields も差分に含めます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc diff --help` / `gen-oc-help.py` で生成</sub>
