# `oc adm prune renderedmachineconfigs`

> Prunes rendered MachineConfigs in an OpenShift cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `renderedmachineconfigs`

## Usage

```
oc adm prune renderedmachineconfigs [options]
```

Experimental: This command is under development and may change without notice.
Prune rendered MachineConfigs for an OCP v4 cluster.
oc adm prune renderedmachineconfigs

## Subcommands

- [`list`](renderedmachineconfigs/list.md) — Lists rendered MachineConfigs in an OpenShift cluster

## Examples

```bash
# See what the prune command would delete if run with no options
oc adm prune renderedmachineconfigs

# To actually perform the prune operation, the confirm flag must be appended
oc adm prune renderedmachineconfigs --confirm

# See what the prune command would delete if run on the worker MachineConfigPool
oc adm prune renderedmachineconfigs --pool-name=worker

# Prunes 10 oldest rendered MachineConfigs in the cluster
oc adm prune renderedmachineconfigs --count=10 --confirm

# Prunes 10 oldest rendered MachineConfigs in the cluster for the worker MachineConfigPool
oc adm prune renderedmachineconfigs --count=10 --pool-name=worker --confirm
```

## Options

- `--confirm=false`
  If true, specify that pruning should proceed. Defaults to false, displaying what would be deleted but not actually deleting anything.

- `--count=0`
  Number of rendered MachineConfigs to delete from the list (default: delete all but current rendered MachineConfigs)

- `-p, --pool-name=''`
  Specify the MachineConfigPool name to filter by (default: all pools)

> Use "oc adm prune renderedmachineconfigs `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune renderedmachineconfigs --help` / `gen-oc-help.py` で生成</sub>
