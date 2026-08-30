# `oc set image-lookup`

> Change how images are resolved when deploying applications

[`oc`](../oc.md) / [`oc set`](../set.md) / `image-lookup`

## Usage

```
oc set image-lookup STREAMNAME [...] [flags] [options]
```

Use an image stream from pods and other objects.

Image streams make it easy to tag images, track changes from other registries, and centralize access control to images. Local name lookup allows an image stream to be the source of images for pods, deployments, replica sets, and other resources that reference images, without having to provide the full registry URL. If local name lookup is enabled for an image stream named 'mysql', a pod or other resource that references 'mysql:latest' (or any other tag) will pull from the location specified by the image stream tag, not from an upstream registry.

Once lookup is enabled, simply reference the image stream tag in the image field of the object. For example:

        $ oc import-image mysql:latest --confirm
        $ oc set image-lookup mysql
        $ oc run mysql --image=mysql

will import the latest MySQL image from the DockerHub, set that image stream to handle the "mysql" name within the project, and then launch a deployment that points to the image we imported.

You may also force image lookup for all of the images on a resource with this command. An annotation is placed on the object which forces an image stream tag lookup in the current namespace for any image that matches, regardless of whether the image stream has lookup enabled.

        $ oc run mysql --image=myregistry:5000/test/mysql:v1
        $ oc tag --source=docker myregistry:5000/test/mysql:v1 mysql:v1
        $ oc set image-lookup deploy/mysql

Which should trigger a deployment pointing to the imported mysql:v1 tag.

## Examples

```bash
# Print all of the image streams and whether they resolve local names
oc set image-lookup

# Use local name lookup on image stream mysql
oc set image-lookup mysql

# Force a deployment to use local name lookup
oc set image-lookup deploy/mysql

# Show the current status of the deployment lookup
oc set image-lookup deploy/mysql --list

# Disable local name lookup on image stream mysql
oc set image-lookup mysql --enabled=false

# Set local name lookup on all image streams
oc set image-lookup --all
```

## Options

- `--all=false`
  If true, select all resources in the namespace of the specified resource types.

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--enabled=true`
  Mark the image stream as resolving tagged images in this namespace.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--list=false`
  Display the current states of the requested resources.

- `--local=false`
  If true, operations will be performed locally.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set image-lookup --help` / `gen-oc-help.py` で生成</sub>
