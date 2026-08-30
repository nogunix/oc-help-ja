# `oc config rename-context`

> Rename a context from the kubeconfig file

[`oc`](../oc.md) / [`oc config`](../config.md) / `rename-context`

## Usage

```
oc config rename-context CONTEXT_NAME NEW_NAME [options]
```

Renames a context from the kubeconfig file.

CONTEXT_NAME is the context name that you want to change.

NEW_NAME is the new name you want to set.

Note: If the context being renamed is the 'current-context', this field will also be updated.

## Examples

```bash
# Rename the context 'old-name' to 'new-name' in your kubeconfig file
oc config rename-context old-name new-name
```

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config rename-context --help` / `gen-oc-help.py` で生成</sub>
