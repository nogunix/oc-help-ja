# `oc config set-context`

> Set a context entry in kubeconfig

[`oc`](../oc.md) / [`oc config`](../config.md) / `set-context`

## Usage

```
oc config set-context [NAME | --current] [--cluster=cluster_nickname] [--user=user_nickname] [--namespace=namespace] [options]
```

Specifying a name that already exists will merge new fields on top of existing values for those fields.

## Examples

```bash
# Set the user field on the gce context entry without touching other values
oc config set-context gce --user=cluster-admin
```

## Options

- `--cluster=''`
  cluster for the context entry in kubeconfig

- `--current=false`
  Modify the current context

- `-n, --namespace=''`
  namespace for the context entry in kubeconfig

- `--user=''`
  user for the context entry in kubeconfig

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config set-context --help` / `gen-oc-help.py` で生成</sub>
