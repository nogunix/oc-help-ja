# `oc set data`

> Update the data within a config map or secret

[`oc`](../oc.md) / [`oc set`](../set.md) / `data`

## Usage

```
oc set data RESOURCE/NAME [KEY=VALUE|KEY- ...] [--from-file=file|dir|key=path] [flags] [options]
```

Add, update, or remove data keys from secrets and config maps.

Secrets and config maps allow users to store keys and values that can be passed into pods or loaded by other Kubernetes resources. This command lets you set or remove keys from those objects from arguments or files. Use the --from-file flag when you want to load the contents of a file or directory, or pass command line arguments that contain either a KEY=VALUE pair (to set a value) or KEY- (to remove that key).

You may also use this command as part of a chain to modify an object before submitting to the server with the --local and --dry-run flags. This allows you to update local resources to contain additional keys.

## Examples

```bash
# Set the 'password' key of a secret
oc set data secret/foo password=this_is_secret

# Remove the 'password' key from a secret
oc set data secret/foo password-

# Update the 'haproxy.conf' key of a config map from a file on disk
oc set data configmap/bar --from-file=../haproxy.conf

# Update a secret with the contents of a directory, one key per file
oc set data secret/foo --from-file=secret-dir
```

## Options

- `--all=false`
  If true, select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `--from-file=[]`
  Specify a file using its file path, in which case the file basename will be used as the key or optionally with a key and file path, in which case the given key will be used.  Specifying a directory will iterate each named file in the directory whose basename is a valid secret key.

- `--from-literal=[]`
  Specify a key and literal value to set (i.e. mykey=somevalue)

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--local=false`
  If true, set image will NOT contact api-server but run locally.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set data --help` / `gen-oc-help.py` で生成</sub>
