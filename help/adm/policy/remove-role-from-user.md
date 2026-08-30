# `oc adm policy remove-role-from-user`

> Remove a role from users for the project

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `remove-role-from-user`

## Usage

```
oc adm policy remove-role-from-user ROLE USER [USER ...] [flags] [options]
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--role-namespace=''`
  namespace where the role is located: empty means a role defined in cluster policy

- `--rolebinding-name=''`
  Name of the rolebinding to modify. If left empty it will operate on all rolebindings

- `-z, --serviceaccount=[]`
  service account in the current namespace to use as a user

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy remove-role-from-user --help` / `gen-oc-help.py` で生成</sub>
