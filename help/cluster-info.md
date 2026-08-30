# `oc cluster-info`

> Display cluster information

[`oc`](oc.md) / `cluster-info`

## Usage

```
oc cluster-info [flags] [options]
```

Display addresses of the control plane and services with label kubernetes.io/cluster-service=true. To further debug and diagnose cluster problems, use 'oc cluster-info dump'.

## Subcommands

- [`dump`](cluster-info/dump.md) — Dump relevant information for debugging and diagnosis

## Examples

```bash
# Print the address of the control plane and cluster services
oc cluster-info
```

> Use "oc cluster-info `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc cluster-info --help` / `gen-oc-help.py` で生成</sub>
