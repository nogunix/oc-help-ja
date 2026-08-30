# `oc config set-context`

> kubeconfig にコンテキストエントリを設定する

[`oc`](../oc.md) / [`oc config`](../config.md) / `set-context`

## Usage

```
oc config set-context [NAME | --current] [--cluster=cluster_nickname] [--user=user_nickname] [--namespace=namespace] [options]
```

既に存在する名前を指定した場合、そのフィールドの既存の値の上に新しいフィールドがマージされます。

## Examples

```bash
# 他の値には触れず、gce コンテキストエントリの user フィールドを設定する
oc config set-context gce --user=cluster-admin
```

## Options

- `--cluster=''`
  kubeconfig 内のコンテキストエントリの cluster

- `--current=false`
  現在のコンテキストを変更する

- `-n, --namespace=''`
  kubeconfig 内のコンテキストエントリの namespace

- `--user=''`
  kubeconfig 内のコンテキストエントリの user

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config set-context --help` / `gen-oc-help.py` で生成</sub>
