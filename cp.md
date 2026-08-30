# `oc cp`

> コンテナとの間でファイルやディレクトリをコピーする

[`oc`](oc.md) / `cp`

## Usage

```
oc cp <file-spec-src> <file-spec-dest> [options]
```

## Examples

```bash
# !!!重要な注意!!!
# コンテナ内に 'tar' バイナリが存在している必要があります
# イメージ。'tar' が存在しない場合、'oc cp' は失敗します。
#
# シンボリックリンクやワイルドカード展開などの高度な使い方をする場合は
# ファイルモードの維持が必要な場合は 'oc exec' の使用を検討してください。

# ローカルファイル /tmp/foo を、namespace <some-namespace> のリモート Pod の /tmp/bar にコピーする
tar cf - /tmp/foo | oc exec -i -n <some-namespace> <some-pod> -- tar xf - -C /tmp/bar

# リモート Pod の /tmp/foo をローカルの /tmp/bar にコピーする
oc exec -n <some-namespace> <some-pod> -- tar cf - /tmp/foo | tar xf - -C /tmp/bar

# ローカルディレクトリ /tmp/foo_dir を、default namespace のリモート Pod の /tmp/bar_dir にコピーする
oc cp /tmp/foo_dir <some-pod>:/tmp/bar_dir

# ローカルファイル /tmp/foo を、リモート Pod 内の特定のコンテナの /tmp/bar にコピーする
oc cp /tmp/foo <some-pod>:/tmp/bar -c <specific-container>

# ローカルファイル /tmp/foo を、namespace <some-namespace> のリモート Pod の /tmp/bar にコピーする
oc cp /tmp/foo <some-namespace>/<some-pod>:/tmp/bar

# リモート Pod の /tmp/foo をローカルの /tmp/bar にコピーする
oc cp <some-namespace>/<some-pod>:/tmp/foo /tmp/bar
```

## Options

- `-c, --container=''`
  コンテナ名。省略した場合は、アタッチ対象のコンテナ選択に kubectl.kubernetes.io/default-container アノテーションが使われ、それも無ければ Pod 内の最初のコンテナが選ばれます

- `--no-preserve=false`
  コピーされたファイル / ディレクトリの所有者とパーミッションは、コンテナ内では維持されません

- `--retries=0`
  コンテナからのコピー操作を完了させるための再試行回数を設定します。0 を指定すると無効、負の値を指定すると無制限に再試行します。デフォルトは 0（再試行しない）です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc cp --help` / `gen-oc-help.py` で生成</sub>
