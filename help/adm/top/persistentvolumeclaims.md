# `oc adm top persistentvolumeclaims`

> Experimental: Show usage statistics for bound persistentvolumeclaims

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm top`](../top.md) / `persistentvolumeclaims`

## Usage

```
oc adm top persistentvolumeclaims [flags] [options]
```

This command analyzes all the bound persistentvolumeclaims managed by the platform and presents current usage statistics.

Aliases:
persistentvolumeclaims, persistentvolumeclaim, pvc

## Examples

```bash
# Show usage statistics for all the bound persistentvolumeclaims across the cluster
oc adm top persistentvolumeclaims -A

# Show usage statistics for all the bound persistentvolumeclaims in a specific namespace
oc adm top persistentvolumeclaims -n default

# Show usage statistics for specific bound persistentvolumeclaims
oc adm top persistentvolumeclaims database-pvc app-pvc -n default
```

## Options

- `-A, --all-namespaces=false`
  If present, list the pvc usage across all namespaces. Namespace in current context is ignored even if specified with --namespace

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm top persistentvolumeclaims --help` / `gen-oc-help.py` で生成</sub>
