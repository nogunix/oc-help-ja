# `oc rollout`

> Manage the rollout of a resource

[`oc`](oc.md) / `rollout`

## Usage

```
oc rollout SUBCOMMAND [flags] [options]
```

Manage the rollout of one or more resources. Valid resource types include:

- deployments
- daemonsets
- statefulsets
- deploymentConfigs (deprecated)

## Subcommands

- [`cancel`](rollout/cancel.md) — Cancel the in-progress deployment
- [`history`](rollout/history.md) — View rollout history
- [`latest`](rollout/latest.md) — Start a new rollout for a deployment config with the latest state from its triggers
- [`pause`](rollout/pause.md) — Mark the provided resource as paused
- [`restart`](rollout/restart.md) — Restart a resource
- [`resume`](rollout/resume.md) — Resume a paused resource
- [`retry`](rollout/retry.md) — Retry the latest failed rollout
- [`status`](rollout/status.md) — Show the status of the rollout
- [`undo`](rollout/undo.md) — Undo a previous rollout

## Examples

```bash
# Roll back to the previous deployment
oc rollout undo deployment/abc

# Check the rollout status of a daemonset
oc rollout status daemonset/foo

# Restart a deployment
oc rollout restart deployment/abc

# Restart deployments with the 'app=nginx' label
oc rollout restart deployment --selector=app=nginx
```

> Use "oc rollout `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc rollout --help` / `gen-oc-help.py` で生成</sub>
