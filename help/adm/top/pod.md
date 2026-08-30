# `oc adm top pod`

> Display resource (CPU/memory) usage of pods

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm top`](../top.md) / `pod`

## Usage

```
oc adm top pod [NAME | -l label] [options]
```

The 'top pod' command allows you to see the resource consumption of pods.

Due to the metrics pipeline delay, they may be unavailable for a few minutes since pod creation.

Aliases:
pod, pods, po

## Examples

```bash
# Show metrics for all pods in the default namespace
oc adm top pod

# Show metrics for all pods in the given namespace
oc adm top pod --namespace=NAMESPACE

# Show metrics for a given pod and its containers
oc adm top pod POD_NAME --containers

# Show metrics for the pods defined by label name=myLabel
oc adm top pod -l name=myLabel
```

## Options

- `-A, --all-namespaces=false`
  If present, list the requested object(s) across all namespaces. Namespace in current context is ignored even if specified with --namespace.

- `--containers=false`
  If present, print usage of containers within a pod.

- `--field-selector=''`
  Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector key1=value1,key2=value2). The server only supports a limited number of field queries per type.

- `--no-headers=false`
  If present, print output without headers.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

- `--show-swap=false`
  Print pod resources related to swap memory.

- `--sort-by=''`
  If non-empty, sort pods list using specified field. The field can be either 'cpu' or 'memory'.

- `--sum=false`
  Print the sum of the resource usage

- `--use-protocol-buffers=true`
  Enables using protocol-buffers to access Metrics API.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm top pod --help` / `gen-oc-help.py` で生成</sub>
