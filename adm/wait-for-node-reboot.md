# `oc adm wait-for-node-reboot`

> `oc adm reboot-machine-config-pool` の実行後、ノードの再起動を待つ

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `wait-for-node-reboot`

## Usage

```
oc adm wait-for-node-reboot [options]
```

## Examples

```bash
# 'oc adm reboot-machine-config-pool mcp/worker mcp/master' で要求した再起動を、すべてのノードが完了するまで待つ
oc adm wait-for-node-reboot nodes --all

# 'oc adm reboot-machine-config-pool mcp/master' で要求した再起動を、master が完了するまで待つ
oc adm wait-for-node-reboot nodes -l node-role.kubernetes.io/master

# master が特定の再起動を完了するまで待つ
oc adm wait-for-node-reboot nodes -l node-role.kubernetes.io/master --reboot-number=4
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  リソースを特定する。

- `--reboot-number=0`
  指定しない場合は現在の再起動回数が使用されます。指定した場合、その再起動回数に達している、またはそれを超えているノードは完了とみなされます。

- `-R, --recursive=true`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!=' をサポートします（例: -l key1=value1,key2=value2）

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm wait-for-node-reboot --help` / `gen-oc-help.py` で生成</sub>
