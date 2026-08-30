# `oc adm prune auth`

> Removes references to the specified roles, clusterroles, users, and groups

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `auth`

## Usage

```
oc adm prune auth [flags] [options]
```

Removes references to the specified roles, clusterroles, users, and groups.  Other types are ignored.

## Options

- `--all=false`
  Prune all roles in the namespace.

- `-f, --filename=[]`
  Filename, directory, or URL to files containing the resource to delete.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune auth --help` / `gen-oc-help.py` で生成</sub>
