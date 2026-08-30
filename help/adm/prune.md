# `oc adm prune`

> Remove older versions of resources from the server

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `prune`

## Usage

```
oc adm prune [flags] [options]
```

The commands here allow administrators to manage the older versions of resources on the system by removing them.

## Subcommands

- [`auth`](prune/auth.md) — Removes references to the specified roles, clusterroles, users, and groups
- [`builds`](prune/builds.md) — Remove old completed and failed builds
- [`deployments`](prune/deployments.md) — Remove old completed and failed deployment configs
- [`groups`](prune/groups.md) — Remove old OpenShift groups referencing missing records from an external provider
- [`images`](prune/images.md) — Remove unreferenced images
- [`renderedmachineconfigs`](prune/renderedmachineconfigs.md) — Prunes rendered MachineConfigs in an OpenShift cluster

> Use "oc adm prune `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune --help` / `gen-oc-help.py` で生成</sub>
