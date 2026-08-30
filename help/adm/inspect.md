# `oc adm inspect`

> Collect debugging data for a given resource

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `inspect`

## Usage

```
oc adm inspect (TYPE[.VERSION][.GROUP] [NAME] | TYPE[.VERSION][.GROUP]/NAME ...) [flags] [options]
```

Gather debugging information for a resource.

This command downloads the specified resource and any related resources for the purpose of gathering debugging information.

## Examples

```bash
# Collect debugging data for the "openshift-apiserver" clusteroperator
oc adm inspect clusteroperator/openshift-apiserver

# Collect debugging data for the "openshift-apiserver" and "kube-apiserver" clusteroperators
oc adm inspect clusteroperator/openshift-apiserver clusteroperator/kube-apiserver

# Collect debugging data for all clusteroperators
oc adm inspect clusteroperator

# Collect debugging data for all clusteroperators and clusterversions
oc adm inspect clusteroperators,clusterversions
```

## Options

- `-A, --all-namespaces=false`
  If present, list the requested object(s) across all namespaces. Namespace in current context is ignored even if specified with --namespace.

- `--as=''`
  Username to impersonate for the operation. User could be a regular user or a service account in a namespace.

- `--as-group=[]`
  Group to impersonate for the operation, this flag can be repeated to specify multiple groups.

- `--as-uid=''`
  UID to impersonate for the operation.

- `--as-user-extra=[]`
  User extras to impersonate for the operation, this flag can be repeated to specify multiple values for the same key.

- `--cache-dir='/home/mnoguchi/.kube/cache'`
  Default cache directory

- `--certificate-authority=''`
  Path to a cert file for the certificate authority

- `--client-certificate=''`
  Path to a client certificate file for TLS

- `--client-key=''`
  Path to a client key file for TLS

- `--cluster=''`
  The name of the kubeconfig cluster to use

- `--context=''`
  The name of the kubeconfig context to use

- `--dest-dir=''`
  Root directory used for storing all gathered cluster operator data. Defaults to $(PWD)/inspect.local.`<rand>`

- `--disable-compression=false`
  If true, opt-out of response compression for all requests to the server

- `--events-file=''`
  A path to an events.json file to create a HTML page from

- `--insecure-skip-tls-verify=false`
  If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure

- `--kubeconfig=''`
  Path to the kubeconfig file to use for CLI requests.

- `-n, --namespace=''`
  If present, the namespace scope for this CLI request

- `--request-timeout='0'`
  The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests.

- `-s, --server=''`
  The address and port of the Kubernetes API server

- `--since=0s`
  Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs. Only one of since-time / since may be used.

- `--since-time=''`
  Only return logs after a specific date (RFC3339). Defaults to all logs. Only one of since-time / since may be used.

- `--tls-server-name=''`
  Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used

- `--token=''`
  Bearer token for authentication to the API server

- `--user=''`
  The name of the kubeconfig user to use

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm inspect --help` / `gen-oc-help.py` で生成</sub>
