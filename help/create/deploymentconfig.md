# `oc create deploymentconfig`

> Create a deployment config with default options that uses a given image

[`oc`](../oc.md) / [`oc create`](../create.md) / `deploymentconfig`

## Usage

```
oc create deploymentconfig NAME --image=IMAGE -- [COMMAND] [args...] [flags] [options]
```

Create a deployment config that uses a given image.

Deployment configs define the template for a pod and manage deploying new images or configuration changes.

Aliases:
deploymentconfig, dc

## Examples

```bash
# Create an nginx deployment config named my-nginx
oc create deploymentconfig my-nginx --image=nginx
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--image=''`
  The image for the container to run.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create deploymentconfig --help` / `gen-oc-help.py` で生成</sub>
