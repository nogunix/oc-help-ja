# `oc adm prune groups`

> Remove old OpenShift groups referencing missing records from an external provider

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `groups`

## Usage

```
oc adm prune groups [WHITELIST] [--whitelist=WHITELIST-FILE] [--blacklist=BLACKLIST-FILE] --sync-config=CONFIG-SOURCE [flags] [options]
```

Prune OpenShift groups referencing missing records from an external provider.

In order to prune OpenShift group records using those from an external provider, determine which groups you want to prune. For instance, all or some groups may be selected from the current groups stored in OpenShift that have been synced previously. Any combination of a literal whitelist, a whitelist file and a blacklist file is supported. The path to a sync configuration file that was used for syncing the groups in question is required in order to describe how data is requested from the external record store. Default behavior is to indicate all OpenShift groups for which the external record does not exist, to run the pruning process and commit the results, use the --confirm flag.

## Examples

```bash
# Prune all orphaned groups
oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm

# Prune all orphaned groups except the ones from the denylist file
oc adm prune groups --blacklist=/path/to/denylist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm

# Prune all orphaned groups from a list of specific groups specified in an allowlist file
oc adm prune groups --whitelist=/path/to/allowlist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm

# Prune all orphaned groups from a list of specific groups specified in a list
oc adm prune groups groups/group_name groups/other_name --sync-config=/path/to/ldap-sync-config.yaml --confirm
```

## Options

- `--blacklist=''`
  path to the group blacklist file

- `--confirm=false`
  if true, modify OpenShift groups; if false, display groups

- `--sync-config=''`
  path to the sync config

- `--whitelist=''`
  path to the group whitelist file

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune groups --help` / `gen-oc-help.py` で生成</sub>
