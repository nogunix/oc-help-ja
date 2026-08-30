# `oc config refresh-ca-bundle`

> Update the OpenShift CA bundle by contacting the API server

[`oc`](../oc.md) / [`oc config`](../config.md) / `refresh-ca-bundle`

## Usage

```
oc config refresh-ca-bundle [NAME] [options]
```

Update the CA bundle by reading the content from an OpenShift cluster.

## Examples

```bash
# Refresh the CA bundle for the current context's cluster
oc config refresh-ca-bundle

# Refresh the CA bundle for the cluster named e2e in your kubeconfig
oc config refresh-ca-bundle e2e

# Print the CA bundle from the current OpenShift cluster's API server
oc config refresh-ca-bundle --dry-run
```

## Options

- `--dry-run=false`
  display the CA bundle, but don't make any changes to the kubeconfig

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config refresh-ca-bundle --help` / `gen-oc-help.py` で生成</sub>
