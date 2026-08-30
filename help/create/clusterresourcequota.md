# `oc create clusterresourcequota`

> Create a cluster resource quota

[`oc`](../oc.md) / [`oc create`](../create.md) / `clusterresourcequota`

## Usage

```
oc create clusterresourcequota NAME --project-label-selector=key=value [--hard=RESOURCE=QUANTITY]... [flags] [options]
```

Create a cluster resource quota that controls certain resources.

Cluster resource quota objects define quota restrictions that span multiple projects based on label selectors.

Aliases:
clusterresourcequota, clusterquota

## Examples

```bash
# Create a cluster resource quota limited to 10 pods
oc create clusterresourcequota limit-bob --project-annotation-selector=openshift.io/requester=user-bob --hard=pods=10
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--hard=[]`
  The resource to constrain: RESOURCE=QUANTITY (pods=10)

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--project-annotation-selector=''`
  The project annotation selector for the cluster resource quota

- `--project-label-selector=''`
  The project label selector for the cluster resource quota

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create clusterresourcequota --help` / `gen-oc-help.py` で生成</sub>
