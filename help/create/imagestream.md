# `oc create imagestream`

> Create a new empty image stream

[`oc`](../oc.md) / [`oc create`](../create.md) / `imagestream`

## Usage

```
oc create imagestream NAME [flags] [options]
```

Create a new image stream.

Image streams allow you to track, tag, and import images from other registries. They also define an access controlled destination that you can push images to. An image stream can reference images from many different registries and control how those images are referenced by pods, deployments, and builds.

If --lookup-local is passed, the image stream will be used as the source when pods reference it by name. For example, if stream 'mysql' resolves local names, a pod that points to 'mysql:latest' will use the image the image stream points to under the "latest" tag.

Aliases:
imagestream, is

## Examples

```bash
# Create a new image stream
oc create imagestream mysql
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--lookup-local=false`
  If true, the image stream will be the source for any top-level image reference in this project.

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

<sub>`$ oc create imagestream --help` / `gen-oc-help.py` で生成</sub>
