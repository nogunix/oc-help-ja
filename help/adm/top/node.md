# `oc adm top node`

> Display resource (CPU/memory) usage of nodes

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm top`](../top.md) / `node`

## Usage

```
oc adm top node [NAME | -l label] [options]
```

The top-node command allows you to see the resource consumption of nodes.

Aliases:
node, nodes, no

## Examples

```bash
# Show metrics for all nodes
oc adm top node

# Show metrics for a given node
oc adm top node NODE_NAME
```

## Options

- `--no-headers=false`
  If present, print output without headers

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

- `--show-capacity=false`
  Print node resources based on Capacity instead of Allocatable(default) of the nodes.

- `--show-swap=false`
  Print node resources related to swap memory.

- `--sort-by=''`
  If non-empty, sort nodes list using specified field. The field can be either 'cpu' or 'memory'.

- `--use-protocol-buffers=true`
  Enables using protocol-buffers to access Metrics API.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm top node --help` / `gen-oc-help.py` で生成</sub>
