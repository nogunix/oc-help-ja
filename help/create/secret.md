# `oc create secret`

> Create a secret using a specified subcommand

[`oc`](../oc.md) / [`oc create`](../create.md) / `secret`

## Usage

```
oc create secret (docker-registry | generic | tls) [options]
```

Create a secret with specified type.

A docker-registry type secret is for accessing a container registry.

A generic type secret indicate an Opaque secret type.

A tls type secret holds TLS certificate and its associated key.

## Subcommands

- [`docker-registry`](secret/docker-registry.md) — Create a secret for use with a Docker registry
- [`generic`](secret/generic.md) — Create a secret from a local file, directory, or literal value
- [`tls`](secret/tls.md) — Create a TLS secret

> Use "oc create secret `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create secret --help` / `gen-oc-help.py` で生成</sub>
