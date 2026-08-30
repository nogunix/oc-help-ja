# `oc adm policy`

> Manage cluster authorization and security policy

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `policy`

## Usage

```
oc adm policy [flags] [options]
```

Manage policy on the cluster

These commands allow you to assign and manage the roles and policies that apply to users. The reconcile commands allow you to reset and upgrade your system policies to the latest default policies.

To see more information on roles and bindings, use the 'get' and 'describe' commands on the following resources: 'clusterroles', 'clusterrolebindings', 'roles', 'rolebindings', and 'scc'.

## Subcommands

- [`add-cluster-role-to-group`](policy/add-cluster-role-to-group.md) — Add a role to groups for all projects in the cluster
- [`add-cluster-role-to-user`](policy/add-cluster-role-to-user.md) — Add a role to users for all projects in the cluster
- [`add-role-to-group`](policy/add-role-to-group.md) — Add a role to groups for the project
- [`add-role-to-user`](policy/add-role-to-user.md) — Add a role to users or service accounts for the current project
- [`add-scc-to-group`](policy/add-scc-to-group.md) — Add a security context constraint to groups
- [`add-scc-to-user`](policy/add-scc-to-user.md) — Add a security context constraint to users or a service account
- [`remove-cluster-role-from-group`](policy/remove-cluster-role-from-group.md) — Remove a role from groups for all projects in the cluster
- [`remove-cluster-role-from-user`](policy/remove-cluster-role-from-user.md) — Remove a role from users for all projects in the cluster
- [`remove-group`](policy/remove-group.md) — Remove group from the project
- [`remove-role-from-group`](policy/remove-role-from-group.md) — Remove a role from groups for the project
- [`remove-role-from-user`](policy/remove-role-from-user.md) — Remove a role from users for the project
- [`remove-scc-from-group`](policy/remove-scc-from-group.md) — Remove a group from a security context constraint
- [`remove-scc-from-user`](policy/remove-scc-from-user.md) — Remove a user from a security context constraint
- [`remove-user`](policy/remove-user.md) — Remove user from the project
- [`scc-review`](policy/scc-review.md) — Check which service account can create a pod
- [`scc-subject-review`](policy/scc-subject-review.md) — Check whether a user or a service account can create a pod
- [`who-can`](policy/who-can.md) — List who can perform the specified action on a resource

> Use "oc adm policy `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy --help` / `gen-oc-help.py` で生成</sub>
