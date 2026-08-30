# `oc adm restart-kubelet`

> Restart kubelet on the specified nodes

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `restart-kubelet`

## Usage

```
oc adm restart-kubelet [options]
```

Regenerate certificates provided by an OCP v4 cluster.

This command does not wait for changes to be acknowledged by the cluster. Some may take a very long time to roll out into a cluster, with different operators and operands involved for each.

Experimental: This command is under active development and may change without notice.

## Examples

```bash
# Restart all the nodes, 10% at a time
oc adm restart-kubelet nodes --all --directive=RemoveKubeletKubeconfig

# Restart all the nodes, 20 nodes at a time
oc adm restart-kubelet nodes --all --parallelism=20 --directive=RemoveKubeletKubeconfig

# Restart all the nodes, 15% at a time
oc adm restart-kubelet nodes --all --parallelism=15% --directive=RemoveKubeletKubeconfig

# Restart all the masters at the same time
oc adm restart-kubelet nodes -l node-role.kubernetes.io/master --parallelism=100% --directive=RemoveKubeletKubeconfig
```

## Options

- `--all=false`
  Select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--command=''`
  command to run after the kubelet stops, before the kubelet starts.

- `--directive=''`
  run a well-known command while restarting kubelets: RemoveKubeletKubeconfig

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

<sub>`$ oc adm restart-kubelet --help` / `gen-oc-help.py` で生成</sub>
