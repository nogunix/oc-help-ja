# `oc adm policy add-role-to-group`

> Add a role to groups for the project

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-role-to-group`

## Usage

```
oc adm policy add-role-to-group ROLE GROUP [GROUP ...] [flags] [options]
```

This command allows you to grant a group access to specific resources and actions within the current project, by assigning them to a role. It creates or modifies a role binding referencing the specified role adding the group(s) to the list of subjects. The command does not require that the matching role or group resources exist and will create the binding successfully even when the role or group do not exist or when the user does not have access to view them.

If the --rolebinding-name argument is supplied, it will look for an existing role binding with that name. The role on the matching role binding MUST match the role name supplied to the command. If no role binding name is given, a default name will be used. When --role-namespace argument is specified as a non-empty value, it MUST match the current namespace. When role-namespace is specified, the role binding will reference a namespaced role. Otherwise, the role binding will reference a cluster role resource.

To learn more, see information about RBAC and policy, or use the 'get' and 'describe' commands on the following resources: 'clusterroles', 'clusterrolebindings', 'roles', 'rolebindings', 'users', 'groups', and 'serviceaccounts'.

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
  Name of the rolebinding to modify or create. If left empty creates a new rolebinding with a default name

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy add-role-to-group --help` / `gen-oc-help.py` で生成</sub>
