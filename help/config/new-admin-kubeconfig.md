# `oc config new-admin-kubeconfig`

> Generate, make the server trust, and display a new admin.kubeconfig

[`oc`](../oc.md) / [`oc config`](../config.md) / `new-admin-kubeconfig`

## Usage

```
oc config new-admin-kubeconfig [options]
```

The key is produced locally and is not persisted to disk.  The public half is pushed to the cluster for the kube-apiserver to trust the locally created admin.kubeconfig.

## Examples

```bash
# Generate a new admin kubeconfig
oc config new-admin-kubeconfig
```

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config new-admin-kubeconfig --help` / `gen-oc-help.py` で生成</sub>
