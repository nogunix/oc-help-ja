# `oc adm wait-for-node-reboot`

> Wait for nodes to reboot after running `oc adm reboot-machine-config-pool`

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `wait-for-node-reboot`

## Usage

```
oc adm wait-for-node-reboot [options]
```

## Examples

```bash
# Wait for all nodes to complete a requested reboot from 'oc adm reboot-machine-config-pool mcp/worker mcp/master'
oc adm wait-for-node-reboot nodes --all

# Wait for masters to complete a requested reboot from 'oc adm reboot-machine-config-pool mcp/master'
oc adm wait-for-node-reboot nodes -l node-role.kubernetes.io/master

# Wait for masters to complete a specific reboot
oc adm wait-for-node-reboot nodes -l node-role.kubernetes.io/master --reboot-number=4
```

## Options

- `--all=false`
  Select all resources in the namespace of the specified resource types

- `--field-selector=''`
  Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector key1=value1,key2=value2). The server only supports a limited number of field queries per type.

- `-f, --filename=[]`
  identifying the resource.

- `--reboot-number=0`
  If unset, the current reboot numbers are used. If specified, any node at or beyond that reboot number is considered complete.

- `-R, --recursive=true`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l key1=value1,key2=value2)

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm wait-for-node-reboot --help` / `gen-oc-help.py` で生成</sub>
