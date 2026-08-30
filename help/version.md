# `oc version`

> Print the client and server version information

[`oc`](oc.md) / `version`

## Usage

```
oc version [flags] [options]
```

Print the client and server version information for the current context

## Examples

```bash
# Print the OpenShift client, kube-apiserver, and openshift-apiserver version information for the current context
oc version

# Print the OpenShift client, kube-apiserver, and openshift-apiserver version numbers for the current context in JSON format
oc version --output json

# Print the OpenShift client version information for the current context
oc version --client
```

## Options

- `--client=false`
  Client version only (no server required).

- `-o, --output=''`
  One of 'yaml' or 'json'.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc version --help` / `gen-oc-help.py` で生成</sub>
