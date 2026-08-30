# `oc auth reconcile`

> Reconciles rules for RBAC role, role binding, cluster role, and cluster role binding objects

[`oc`](../oc.md) / [`oc auth`](../auth.md) / `reconcile`

## Usage

```
oc auth reconcile -f FILENAME [options]
```

Missing objects are created, and the containing namespace is created for namespaced objects, if required.

Existing roles are updated to include the permissions in the input objects, and remove extra permissions if --remove-extra-permissions is specified.

Existing bindings are updated to include the subjects in the input objects, and remove extra subjects if --remove-extra-subjects is specified.

This is preferred to 'apply' for RBAC resources so that semantically-aware merging of rules and subjects is done.

## Examples

```bash
# Reconcile RBAC resources from a file
oc auth reconcile -f my-rbac-rules.yaml
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-f, --filename=[]`
  Filename, directory, or URL to files identifying the resource to reconcile.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove-extra-permissions=false`
  If true, removes extra permissions added to roles

- `--remove-extra-subjects=false`
  If true, removes extra subjects added to rolebindings

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc auth reconcile --help` / `gen-oc-help.py` で生成</sub>
