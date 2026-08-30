# `oc adm policy add-cluster-role-to-group`

> Add a role to groups for all projects in the cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-cluster-role-to-group`

## Usage

```
oc adm policy add-cluster-role-to-group ROLE GROUP [GROUP...] [flags] [options]
```

Add a role to groups for the project

This command creates or modifies a cluster role binding with the named cluster role by adding the named group(s) to the list of subjects. The command does not require the matching role or group resources exist and will create the binding successfully even when the role or group do not exist or when the user does not have access to view them.

If the --rolebinding-name argument is supplied, it will look for an existing cluster role binding with that name. The role on the matching cluster role binding MUST match the role name supplied to the command. If no rolebinding name is given, a default name will be used.

## Examples

```bash
# Add the 'cluster-admin' cluster role to the 'cluster-admins' group
oc adm policy add-cluster-role-to-group cluster-admin cluster-admins
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--rolebinding-name=''`
  Name of the rolebinding to modify or create. If left empty creates a new rolebinding with a default name

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy add-cluster-role-to-group --help` / `gen-oc-help.py` で生成</sub>
