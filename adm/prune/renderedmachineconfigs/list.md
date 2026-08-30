# `oc adm prune renderedmachineconfigs list`

> OpenShift クラスタのレンダリング済み MachineConfig を一覧表示します

[`oc`](../../../oc.md) / [`oc adm`](../../../adm.md) / [`oc adm prune`](../../prune.md) / [`oc adm prune renderedmachineconfigs`](../renderedmachineconfigs.md) / `list`

## Usage

```
oc adm prune renderedmachineconfigs list [options]
```

実験的機能: このコマンドは開発中であり、予告なく変更される可能性があります。OCP v4 クラスタのレンダリング済み MachineConfig を一覧表示します。oc adm prune renderedmachineconfigs list

## Examples

```bash
# クラスタ内の worker MachineConfigPool 向けにレンダリングされた MachineConfig をすべて一覧する
oc adm prune renderedmachineconfigs list --pool-name=worker

# クラスタの MachineConfigPool が使用中の、レンダリング済み MachineConfig をすべて一覧する
oc adm prune renderedmachineconfigs list --in-use
```

## Options

- `--in-use=false`
  true の場合、各 MachineConfigPool が現在使用中のレンダリング済み MachineConfig を一覧します。引数 (--in-use) を指定するだけでこのフラグは true になります。明示的に false (--in-use=false) にすると、通常の list コマンドと同様にすべての machine config を一覧します。

- `-p, --pool-name=''`
  絞り込みに使用する MachineConfigPool 名を指定します（デフォルト: すべてのプール）

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune renderedmachineconfigs list --help` / `gen-oc-help.py` で生成</sub>
