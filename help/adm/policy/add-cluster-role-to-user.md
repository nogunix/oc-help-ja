# `oc adm policy add-cluster-role-to-user`

> Add a role to users for all projects in the cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-cluster-role-to-user`

## Usage

```
oc adm policy add-cluster-role-to-user ROLE (USER | -z serviceaccount) [user]... [flags] [options]
```

Add a role to users or service accounts across all projects

This command allows you to grant a user access to specific resources and actions within the cluster, by assigning them to a role. It creates or modifies a cluster role binding referencing the specified cluster role, adding the user(s) or service account(s) to the list of subjects. This command does not require that the matching cluster role or user/service account resources exist and will create the binding successfully even when the role or user/service account do not exist or when the user does not have access to view them.

If the --rolebinding-name argument is supplied, it will look for an existing cluster role binding with that name. The role on the matching cluster role binding MUST match the role name supplied to the command. If no role binding name is given, a default name will be used.

To learn more, see information about RBAC and policy, or use the 'get' and 'describe' commands on the following resources: 'clusterroles', 'clusterrolebindings', 'roles', 'rolebindings', 'users', 'groups', and 'serviceaccounts'.

## Examples

```bash
# Add the 'system:build-strategy-docker' cluster role to the 'devuser' user
oc adm policy add-cluster-role-to-user system:build-strategy-docker devuser
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--rolebinding-name=''`
  Name of the rolebinding to modify or create. If left empty creates a new rolebindo.RoleBindingNameg with a default name

- `-z, --serviceaccount=[]`
  service account in the current namespace to use o.SANamess a user

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy add-cluster-role-to-user --help` / `gen-oc-help.py` で生成</sub>
