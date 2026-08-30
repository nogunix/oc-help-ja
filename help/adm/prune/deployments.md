# `oc adm prune deployments`

> Remove old completed and failed deployment configs

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `deployments`

## Usage

```
oc adm prune deployments [flags] [options]
```

Prune old completed and failed deployment configs.

By default, the prune operation performs a dry run making no changes to the deployment configs. A --confirm flag is needed for changes to be effective.

## Examples

```bash
# Dry run deleting all but the last complete deployment for every deployment config
oc adm prune deployments --keep-complete=1

# To actually perform the prune operation, the confirm flag must be appended
oc adm prune deployments --keep-complete=1 --confirm
```

## Options

- `--confirm=false`
  If true, specify that deployment pruning should proceed. Defaults to false, displaying what would be deleted but not actually deleting anything.

- `--keep-complete=5`
  Per DeploymentConfig, specify the number of deployments whose status is complete that will be preserved whose replica size is 0.

- `--keep-failed=1`
  Per DeploymentConfig, specify the number of deployments whose status is failed that will be preserved whose replica size is 0.

- `--keep-younger-than=1h0m0s`
  Specify the minimum age of a deployment for it to be considered a candidate for pruning.

- `--orphans=false`
  If true, prune all deployments where the associated DeploymentConfig no longer exists, the status is complete or failed, and the replica size is 0.

- `--replica-sets=false`
  EXPERIMENTAL: If true, ReplicaSets will be included in the pruning process.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune deployments --help` / `gen-oc-help.py` で生成</sub>
