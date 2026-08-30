# `oc secrets`

> Manage secrets

[`oc`](oc.md) / `secrets`

## Usage

```
oc secrets [flags] [options]
```

Manage secrets in your project

Secrets are used to store confidential information that should not be contained inside of an image. They are commonly used to hold things like keys for authentication to other internal systems like container image registries.

Aliases:
secrets, secret

## Subcommands

- [`link`](secrets/link.md) — Link secrets to a service account
- [`unlink`](secrets/unlink.md) — Detach secrets from a service account

> Use "oc secrets `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc secrets --help` / `gen-oc-help.py` で生成</sub>
