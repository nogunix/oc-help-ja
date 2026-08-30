# `oc adm ocp-certificates`

> Tools for managing a cluster's certificates

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `ocp-certificates`

## Usage

```
oc adm ocp-certificates [flags] [options]
```

OCP Certificate Commands

Actions for managing OpenShift platform certificates are exposed here.

## Subcommands

- [`monitor-certificates`](ocp-certificates/monitor-certificates.md) — Watch platform certificates
- [`regenerate-leaf`](ocp-certificates/regenerate-leaf.md) — Regenerate client and serving certificates of an OpenShift cluster
- [`regenerate-machine-config-server-serving-cert`](ocp-certificates/regenerate-machine-config-server-serving-cert.md) — Regenerate the machine config operator certificates in an OpenShift cluster
- [`regenerate-top-level`](ocp-certificates/regenerate-top-level.md) — Regenerate the top level certificates in an OpenShift cluster
- [`remove-old-trust`](ocp-certificates/remove-old-trust.md) — Remove old CAs from ConfigMaps representing platform trust bundles in an OpenShift cluster
- [`update-ignition-ca-bundle-for-machine-config-server`](ocp-certificates/update-ignition-ca-bundle-for-machine-config-server.md) — Update user-data secrets in an OpenShift cluster to use updated MCO certfs

> Use "oc adm ocp-certificates `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm ocp-certificates --help` / `gen-oc-help.py` で生成</sub>
