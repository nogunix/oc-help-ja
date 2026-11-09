# `oc kuberc`

> Manage kuberc configuration files

[`oc`](oc.md) / `kuberc`

## Usage

```
oc kuberc SUBCOMMAND [options]
```

Manage user preferences (kuberc) file.

The kuberc file allows you to customize your oc experience.

## Subcommands

- [`set`](kuberc/set.md) — Set values in the kuberc configuration
- [`view`](kuberc/view.md) — Display the current kuberc configuration

## Examples

```bash
# View the current kuberc configuration
oc kuberc view

# Set a default value for a command flag
oc kuberc set --section defaults --command get --option output=wide

# Create an alias for a command
oc kuberc set --section aliases --name getn --command get --prependarg nodes --option output=wide
```

> Use "oc kuberc `<command>` --help" for more information about a given command.

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc kuberc --help` / `gen-oc-help.py` で生成</sub>
