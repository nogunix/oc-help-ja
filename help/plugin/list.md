# `oc plugin list`

> List all visible plugin executables on a user's PATH

[`oc`](../oc.md) / [`oc plugin`](../plugin.md) / `list`

## Usage

```
oc plugin list [flags] [options]
```

List all available plugin files on a user's PATH. To see plugins binary names without the full path use --name-only flag.

Available plugin files are those that are: - executable - anywhere on the user's PATH - begin with "oc-"

## Examples

```bash
# List all available plugins
oc plugin list

# List only binary names of available plugins without paths
oc plugin list --name-only
```

## Options

- `--name-only=false`
  If true, display only the binary name of each plugin, rather than its full path

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc plugin list --help` / `gen-oc-help.py` で生成</sub>
