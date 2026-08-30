# `oc adm migrate template-instances`

> Update template instances to point to the latest group-version-kinds

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm migrate`](../migrate.md) / `template-instances`

## Usage

```
oc adm migrate template-instances [flags] [options]
```

Migrate template instances to refer to new API groups.

This command locates and updates every template instance which refers to a particular group-version-kind to refer to some other, equivalent group-version-kind.

The following transformations will occur:

- .Build --> build.openshift.io/v1.Build
- .BuildConfig --> build.openshift.io/v1.BuildConfig
- .DeploymentConfig --> apps.openshift.io/v1.DeploymentConfig
- .Route --> route.openshift.io/v1.Route
- v1.Build --> build.openshift.io/v1.Build
- v1.BuildConfig --> build.openshift.io/v1.BuildConfig
- v1.DeploymentConfig --> apps.openshift.io/v1.DeploymentConfig
- v1.Route --> route.openshift.io/v1.Route

## Examples

```bash
# Perform a dry-run of updating all objects
oc adm migrate template-instances

# To actually perform the update, the confirm flag must be appended
oc adm migrate template-instances --confirm
```

## Options

- `-A, --all-namespaces=true`
  Migrate objects in all namespaces. Defaults to true.

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--confirm=false`
  If true, all requested objects will be migrated. Defaults to false.

- `-f, --filename=[]`
  Filename, directory, or URL to docker-compose.yml file to use

- `--from-key=''`
  If specified, only migrate items with a key (namespace/name or name) greater than or equal to this value

- `--include=[templateinstance]`
  Resource types to migrate. Passing --filename will override this flag.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--to-key=''`
  If specified, only migrate items with a key (namespace/name or name) less than this value

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm migrate template-instances --help` / `gen-oc-help.py` で生成</sub>
