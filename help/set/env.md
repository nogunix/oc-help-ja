# `oc set env`

> Update environment variables on a pod template

[`oc`](../oc.md) / [`oc set`](../set.md) / `env`

## Usage

```
oc set env RESOURCE/NAME KEY_1=VAL_1 ... KEY_N=VAL_N [flags] [options]
```

Update environment variables on a pod template or a build config.

List environment variable definitions in one or more pods, pod templates or build configuration. Add, update, or remove container environment variable definitions in one or more pod templates (within replication controllers or deployment configurations) or build configurations. View or modify the environment variable definitions on all containers in the specified pods or pod templates, or just those that match a wildcard.

If "--env -" is passed, environment variables can be read from STDIN using the standard env syntax.

## Examples

```bash
# Update deployment config 'myapp' with a new environment variable
oc set env dc/myapp STORAGE_DIR=/local

# List the environment variables defined on a build config 'sample-build'
oc set env bc/sample-build --list

# List the environment variables defined on all pods
oc set env pods --all --list

# Output modified build config in YAML
oc set env bc/sample-build STORAGE_DIR=/data -o yaml

# Update all containers in all replication controllers in the project to have ENV=prod
oc set env rc --all ENV=prod

# Import environment from a secret
oc set env --from=secret/mysecret dc/myapp

# Import environment from a config map with a prefix
oc set env --from=configmap/myconfigmap --prefix=MYSQL_ dc/myapp

# Remove the environment variable ENV from container 'c1' in all deployment configs
oc set env dc --all --containers="c1" ENV-

# Remove the environment variable ENV from a deployment config definition on disk and
# update the deployment config on the server
oc set env -f dc.json ENV-

# Set some of the local shell environment into a deployment config on the server
oc set env | grep RAILS_ | oc env -e - dc/myapp
```

## Options

- `--all=false`
  If true, select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-c, --containers='*'`
  The names of containers in the selected pod templates to change - may use wildcards

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-e, --env=[]`
  Specify a key-value pair for an environment variable to set into each container.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `--from=''`
  The name of a resource from which to inject environment variables

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--list=false`
  If true, display the environment and any changes in the standard format

- `--local=false`
  If true, set image will NOT contact api-server but run locally.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--overwrite=true`
  If true, allow environment to be overwritten, otherwise reject updates that overwrite existing environment.

- `--prefix=''`
  Prefix to append to variable names

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--resolve=false`
  If true, show secret or configmap references when listing variables

- `--resource-version=''`
  If non-empty, the labels update will only succeed if this is the current resource-version for the object. Only valid when specifying a single resource.

- `-l, --selector=''`
  Selector (label query) to filter on

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set env --help` / `gen-oc-help.py` で生成</sub>
