# `oc policy`

> Manage authorization policy

[`oc`](oc.md) / `policy`

## Usage

```
oc policy [flags] [options]
```

## Subcommands

- [`add-role-to-group`](policy/add-role-to-group.md) — Add a role to groups for the project
- [`add-role-to-user`](policy/add-role-to-user.md) — Add a role to users or service accounts for the current project
- [`remove-group`](policy/remove-group.md) — Remove group from the project
- [`remove-role-from-group`](policy/remove-role-from-group.md) — Remove a role from groups for the project
- [`remove-role-from-user`](policy/remove-role-from-user.md) — Remove a role from users for the project
- [`remove-user`](policy/remove-user.md) — Remove user from the project
- [`scc-review`](policy/scc-review.md) — Check which service account can create a pod
- [`scc-subject-review`](policy/scc-subject-review.md) — Check whether a user or a service account can create a pod
- [`who-can`](policy/who-can.md) — List who can perform the specified action on a resource

> Use "oc policy `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc policy --help` / `gen-oc-help.py` で生成</sub>
