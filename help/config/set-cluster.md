# `oc config set-cluster`

> Set a cluster entry in kubeconfig

[`oc`](../oc.md) / [`oc config`](../config.md) / `set-cluster`

## Usage

```
oc config set-cluster NAME [--server=server] [--certificate-authority=path/to/certificate/authority] [--insecure-skip-tls-verify=true] [--tls-server-name=example.com] [options]
```

Specifying a name that already exists will merge new fields on top of existing values for those fields.

## Examples

```bash
# Set only the server field on the e2e cluster entry without touching other values
oc config set-cluster e2e --server=https://1.2.3.4

# Embed certificate authority data for the e2e cluster entry
oc config set-cluster e2e --embed-certs --certificate-authority=~/.kube/e2e/kubernetes.ca.crt

# Disable cert checking for the e2e cluster entry
oc config set-cluster e2e --insecure-skip-tls-verify=true

# Set the custom TLS server name to use for validation for the e2e cluster entry
oc config set-cluster e2e --tls-server-name=my-cluster-name

# Set the proxy URL for the e2e cluster entry
oc config set-cluster e2e --proxy-url=https://1.2.3.4
```

## Options

- `--certificate-authority=''`
  Path to certificate-authority file for the cluster entry in kubeconfig

- `--embed-certs=false`
  embed-certs for the cluster entry in kubeconfig

- `--insecure-skip-tls-verify=false`
  insecure-skip-tls-verify for the cluster entry in kubeconfig

- `--proxy-url=''`
  proxy-url for the cluster entry in kubeconfig

- `--server=''`
  server for the cluster entry in kubeconfig

- `--tls-server-name=''`
  tls-server-name for the cluster entry in kubeconfig

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config set-cluster --help` / `gen-oc-help.py` で生成</sub>
