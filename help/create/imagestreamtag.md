# `oc create imagestreamtag`

> Create a new image stream tag

[`oc`](../oc.md) / [`oc create`](../create.md) / `imagestreamtag`

## Usage

```
oc create imagestreamtag NAME [flags] [options]
```

Image streams tags allow you to track, tag, and import images from other registries. They also define an access controlled destination that you can push images to. An image stream tag can reference images from many different registries and control how those images are referenced by pods, deployments, and builds.

If --resolve-local is passed, the image stream will be used as the source when pods reference it by name. For example, if stream 'mysql' resolves local names, a pod that points to 'mysql:latest' will use the image the image stream points to under the "latest" tag.

Aliases:
imagestreamtag, istag

## Examples

```bash
# Create a new image stream tag based on an image in a remote registry
oc create imagestreamtag mysql:latest --from-image=myregistry.local/mysql/mysql:5.0
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-A, --annotation=[]`
  Set an annotation on this image stream tag.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--from=''`
  Use the provided image stream tag or image stream image as the source: [`<namespace>`/]name[:`<tag>`|@`<id>`]

- `--from-image=''`
  Use the provided remote image with this tag.

- `--insecure=false`
  Allow importing from registries that are not fully secured by HTTPS.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--reference=false`
  If true, the tag value will be used whenever the image stream tag is referenced.

- `--reference-policy=''`
  If set to 'Local', referenced images will be pulled from the integrated registry. Ignored when reference is true.

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--scheduled=false`
  If set the remote source of this image will be periodically checked for imports.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create imagestreamtag --help` / `gen-oc-help.py` で生成</sub>
