# `oc adm ocp-certificates regenerate-machine-config-server-serving-cert`

> Regenerate the machine config operator certificates in an OpenShift cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm ocp-certificates`](../ocp-certificates.md) / `regenerate-machine-config-server-serving-cert`

## Usage

```
oc adm ocp-certificates regenerate-machine-config-server-serving-cert [options]
```

Regenerate the Machine Config Operator certificates for an OCP v4 cluster. This is the certificate used to verify the MCS contents when a new nodes attempts to join the cluster.

Experimental: This command is under active development and may change without notice.

## Examples

```bash
# Regenerate the MCO certs without modifying user-data secrets
oc adm ocp-certificates regenerate-machine-config-server-serving-cert --update-ignition=false

# Update the user-data secrets to use new MCS certs
oc adm ocp-certificates update-ignition-ca-bundle-for-machine-config-server
```

## Options

- `--update-ignition=true`
  If true, automatically update user-data secrets (ignition) in machine-api namespace. Not useful if node scaling not backed by MachineSet.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm ocp-certificates regenerate-machine-config-server-serving-cert --help` / `gen-oc-help.py` で生成</sub>
