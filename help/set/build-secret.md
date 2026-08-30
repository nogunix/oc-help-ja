# `oc set build-secret`

> Update a build secret on a build config

[`oc`](../oc.md) / [`oc set`](../set.md) / `build-secret`

## Usage

```
oc set build-secret BUILDCONFIG SECRETNAME [flags] [options]
```

Set or remove a build secret on a build config.

A build config can reference a secret to push or pull images from private registries or to access private source repositories.

Specify the type of secret being set by using the --push, --pull, or --source flags. A secret reference can be removed by using --remove flag.

A label selector may be specified with the --selector flag to select the build configs on which to set or remove secrets. Alternatively, all build configs in the namespace can be selected with the --all flag.

## Examples

```bash
# Clear the push secret on a build config
oc set build-secret --push --remove bc/mybuild

# Set the pull secret on a build config
oc set build-secret --pull bc/mybuild mysecret

# Set the push and pull secret on a build config
oc set build-secret --push --pull bc/mybuild mysecret

# Set the source secret on a set of build configs matching a selector
oc set build-secret --source -l app=myapp gitsecret
```

## Options

- `--all=false`
  If true, select all build configs in the namespace

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--local=false`
  If true, set build-secret will NOT contact api-server but run locally.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--pull=false`
  If true, set the pull secret on a build config

- `--push=false`
  If true, set the push secret on a build config

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove=false`
  If true, remove the build secret.

- `-l, --selector=''`
  Selector (label query) to filter build configs

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--source=false`
  If true, set the source secret on a build config

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set build-secret --help` / `gen-oc-help.py` で生成</sub>
