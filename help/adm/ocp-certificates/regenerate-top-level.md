# `oc adm ocp-certificates regenerate-top-level`

> Regenerate the top level certificates in an OpenShift cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm ocp-certificates`](../ocp-certificates.md) / `regenerate-top-level`

## Usage

```
oc adm ocp-certificates regenerate-top-level [options]
```

Regenerate root certificates provided by an OCP v4 cluster.

This command does not wait for changes to be acknowledged by the cluster. Some may take a very long time to roll out into a cluster, with different operators and operands involved for each.

Experimental: This command is under active development and may change without notice.

## Examples

```bash
# Regenerate the signing certificate contained in a particular secret
oc adm ocp-certificates regenerate-top-level -n openshift-kube-apiserver-operator secret/loadbalancer-serving-signer-key
```

## Options

- `--all=false`
  Select all resources in the namespace of the specified resource types

- `-A, --all-namespaces=false`
  If present, list the requested object(s) across all namespaces. Namespace in current context is ignored even if specified with --namespace.

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run=false`
  Set to true to use server-side dry run.

- `--field-selector=''`
  Selector (field query) to filter on, supports '=', '==', and '!='.(e.g. --field-selector key1=value1,key2=value2). The server only supports a limited number of field queries per type.

- `-f, --filename=[]`
  identifying the resource.

- `--local=false`
  If true, annotation will NOT contact api-server but run locally.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=true`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l key1=value1,key2=value2)

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--valid-before=''`
  Only regenerate top level certificates valid before this date.  Format: 2023-06-05T14:44:06Z

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm ocp-certificates regenerate-top-level --help` / `gen-oc-help.py` で生成</sub>
