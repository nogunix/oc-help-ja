# `oc adm groups`

> Manage groups

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `groups`

## Usage

```
oc adm groups [flags] [options]
```

Manage groups in your cluster

Groups are sets of users that can be used when describing policy.

## Subcommands

- [`add-users`](groups/add-users.md) — Add users to a group
- [`new`](groups/new.md) — Create a new group
- [`prune`](groups/prune.md) — Remove old OpenShift groups referencing missing records from an external provider
- [`remove-users`](groups/remove-users.md) — Remove users from a group
- [`sync`](groups/sync.md) — Sync OpenShift groups with records from an external provider

> Use "oc adm groups `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm groups --help` / `gen-oc-help.py` で生成</sub>
