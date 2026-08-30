# `oc adm prune renderedmachineconfigs list`

> Lists rendered MachineConfigs in an OpenShift cluster

[`oc`](../../../oc.md) / [`oc adm`](../../../adm.md) / [`oc adm prune`](../../prune.md) / [`oc adm prune renderedmachineconfigs`](../renderedmachineconfigs.md) / `list`

## Usage

```
oc adm prune renderedmachineconfigs list [options]
```

Experimental: This command is under development and may change without notice.
List rendered MachineConfigs for an OCP v4 cluster.
oc adm prune renderedmachineconfigs list

## Examples

```bash
# List all rendered MachineConfigs for the worker MachineConfigPool in the cluster
oc adm prune renderedmachineconfigs list --pool-name=worker

# List all rendered MachineConfigs in use by the cluster's MachineConfigPools
oc adm prune renderedmachineconfigs list --in-use
```

## Options

- `--in-use=false`
  List currently in use rendered MachineConfig for each MachineConfigPool if true. Invoking just the argument (--in-use) will set the flag to true. If manually set to false (--in-use=false), it will list all machine configs as the default list command does.

- `-p, --pool-name=''`
  Specify the MachineConfigPool name to filter by (default: all pools)

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune renderedmachineconfigs list --help` / `gen-oc-help.py` で生成</sub>
