# `oc adm copy-to-node`

> Copy specified files to the node

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `copy-to-node`

## Usage

```
oc adm copy-to-node [options]
```

Copies file from the host to the specified nodes.

Experimental: This command is under active development and may change without notice.

## Examples

```bash
# Copy a new bootstrap kubeconfig file to node-0
oc adm copy-to-node --copy=new-bootstrap-kubeconfig=/etc/kubernetes/kubeconfig node/node-0
```

## Options

- `--all=false`
  Select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--copy=[]`
  `<source-path>`=`<node-destination>`.  Specifying a directory will iterate each named file in the directory, non-recursive (PR welcome) that is a valid secret key.

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

- `--parallelism='10%'`
  parallelism is a raw number or a percentage of the nodes to work with concurrently.

- `-R, --recursive=true`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', and '!='.(e.g. -l key1=value1,key2=value2)

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm copy-to-node --help` / `gen-oc-help.py` で生成</sub>
