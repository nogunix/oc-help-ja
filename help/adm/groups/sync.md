# `oc adm groups sync`

> Sync OpenShift groups with records from an external provider

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm groups`](../groups.md) / `sync`

## Usage

```
oc adm groups sync [--type=TYPE] [WHITELIST] [--whitelist=WHITELIST-FILE] --sync-config=CONFIG-FILE [--confirm] [flags] [options]
```

In order to sync OpenShift group records with those from an external provider, determine which groups you want to sync and where their records live. For instance, all or some groups may be selected from the current groups stored in OpenShift that have been synced previously, or similarly all or some groups may be selected from those stored on an LDAP server. The path to a sync configuration file is required in order to describe how data is requested from the external record store and migrated to OpenShift records. Default behavior is to do a dry-run without changing OpenShift records. Passing '--confirm' will sync all groups from the LDAP server returned by the LDAP query templates.

## Examples

```bash
# Sync all groups with an LDAP server
oc adm groups sync --sync-config=/path/to/ldap-sync-config.yaml --confirm

# Sync all groups except the ones from the blacklist file with an LDAP server
oc adm groups sync --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm

# Sync specific groups specified in an allowlist file with an LDAP server
oc adm groups sync --whitelist=/path/to/allowlist.txt --sync-config=/path/to/sync-config.yaml --confirm

# Sync all OpenShift groups that have been synced previously with an LDAP server
oc adm groups sync --type=openshift --sync-config=/path/to/ldap-sync-config.yaml --confirm

# Sync specific OpenShift groups if they have been synced previously with an LDAP server
oc adm groups sync groups/group1 groups/group2 groups/group3 --sync-config=/path/to/sync-config.yaml --confirm
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--blacklist=''`
  path to the group blacklist file

- `--confirm=false`
  if true, modify OpenShift groups; if false, display results of a dry-run

- `-o, --output='yaml'`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--sync-config=''`
  path to the sync config

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--type='ldap'`
  which groups white- and blacklist entries refer to: ldap,openshift

- `--whitelist=''`
  path to the group whitelist file

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm groups sync --help` / `gen-oc-help.py` で生成</sub>
