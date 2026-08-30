# `oc adm prune renderedmachineconfigs`

> OpenShift クラスタのレンダリング済み MachineConfig を prune します

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `renderedmachineconfigs`

## Usage

```
oc adm prune renderedmachineconfigs [options]
```

実験的機能: このコマンドは開発中であり、予告なく変更される可能性があります。OCP v4 クラスタのレンダリング済み MachineConfig を prune します。oc adm prune renderedmachineconfigs

## Subcommands

- [`list`](renderedmachineconfigs/list.md) — OpenShift クラスタのレンダリング済み MachineConfig を一覧表示します

## Examples

```bash
# オプションなしで実行した場合に、prune コマンドが何を削除するかを確認する
oc adm prune renderedmachineconfigs

# 実際に prune を実行するには、confirm フラグを付ける必要があります
oc adm prune renderedmachineconfigs --confirm

# worker MachineConfigPool を対象に実行した場合に、prune コマンドが何を削除するかを確認する
oc adm prune renderedmachineconfigs --pool-name=worker

# クラスタ内の最も古いレンダリング済み MachineConfig を 10 個 prune する
oc adm prune renderedmachineconfigs --count=10 --confirm

# worker MachineConfigPool について、クラスタ内の最も古いレンダリング済み MachineConfig を 10 個 prune する
oc adm prune renderedmachineconfigs --count=10 --pool-name=worker --confirm
```

## Options

- `--confirm=false`
  true の場合、prune を実際に実行します。デフォルトは false で、削除対象を表示するだけで実際には削除しません。

- `--count=0`
  一覧から削除するレンダリング済み MachineConfig の数（デフォルト: 現在使用中のもの以外をすべて削除）

- `-p, --pool-name=''`
  絞り込みに使用する MachineConfigPool 名を指定します（デフォルト: すべてのプール）

> 各コマンドの詳細については "oc adm prune renderedmachineconfigs `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune renderedmachineconfigs --help` / `gen-oc-help.py` で生成</sub>
