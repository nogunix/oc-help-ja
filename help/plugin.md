# `oc plugin`

> Provides utilities for interacting with plugins

[`oc`](oc.md) / `plugin`

## Usage

```
oc plugin [flags] [options]
```

Plugins provide extended functionality that is not part of the major command-line distribution. Please refer to the documentation and examples for more information about how write your own plugins.

The easiest way to discover and install plugins is via the kubernetes sub-project krew: [krew.sigs.k8s.io]. To install krew, visit https://krew.sigs.k8s.io/docs/user-guide/setup/install

## Subcommands

- [`list`](plugin/list.md) — List all visible plugin executables on a user's PATH

## Examples

```bash
# List all available plugins
oc plugin list

# List only binary names of available plugins without paths
oc plugin list --name-only
```

> Use "oc plugin `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc plugin --help` / `gen-oc-help.py` で生成</sub>
