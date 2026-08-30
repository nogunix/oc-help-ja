# `oc rollout restart`

> Restart a resource

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `restart`

## Usage

```
oc rollout restart RESOURCE [options]
```

Resource rollout will be restarted.

## Examples

```bash
# Restart all deployments in the test-namespace namespace
oc rollout restart deployment -n test-namespace

# Restart a deployment
oc rollout restart deployment/nginx

# Restart a daemon set
oc rollout restart daemonset/abc

# Restart deployments with the app=nginx label
oc rollout restart deployment --selector=app=nginx
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--field-manager='kubectl-rollout'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files identifying the resource to get from a server.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc rollout restart --help` / `gen-oc-help.py` で生成</sub>
