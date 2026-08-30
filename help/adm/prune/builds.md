# `oc adm prune builds`

> Remove old completed and failed builds

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `builds`

## Usage

```
oc adm prune builds [flags] [options]
```

Prune old completed and failed builds.

By default, the prune operation performs a dry run making no changes to internal registry. A --confirm flag is needed for changes to be effective.

## Examples

```bash
# Dry run deleting older completed and failed builds and also including
# all builds whose associated build config no longer exists
oc adm prune builds --orphans

# To actually perform the prune operation, the confirm flag must be appended
oc adm prune builds --orphans --confirm
```

## Options

- `--confirm=false`
  If true, specify that build pruning should proceed. Defaults to false, displaying what would be deleted but not actually deleting anything.

- `--keep-complete=5`
  Per BuildConfig, specify the number of builds whose status is complete that will be preserved.

- `--keep-failed=1`
  Per BuildConfig, specify the number of builds whose status is failed, error, or cancelled that will be preserved.

- `--keep-younger-than=1h0m0s`
  Specify the minimum age of a Build for it to be considered a candidate for pruning.

- `--orphans=false`
  If true, prune all builds whose associated BuildConfig no longer exists and whose status is complete, failed, error, or cancelled.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune builds --help` / `gen-oc-help.py` で生成</sub>
