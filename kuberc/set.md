# `oc kuberc set`

> Set values in the kuberc configuration

[`oc`](../oc.md) / [`oc kuberc`](../kuberc.md) / `set`

## Usage

```
oc kuberc set --section (defaults|aliases) --command COMMAND [options]
```

Set values in the kuberc configuration file.

Use --section to specify whether to set defaults or aliases.

For defaults: Sets default flag values for oc commands. The --command flag should specify only the command (e.g., "get", "create", "set env"), not resources.

For aliases: Creates command aliases with optional default flag values and arguments. Use --prependarg and --appendarg to include resources or other arguments.

## Examples

```bash
# Set default output format for 'get' command
oc kuberc set --section defaults --command get --option output=wide

# Set default output format for a subcommand
oc kuberc set --section defaults --command "set env" --option output=yaml

# Create an alias 'getn' for 'get' command with prepended 'nodes' resource
oc kuberc set --section aliases --name getn --command get --prependarg nodes --option output=wide

# Create an alias 'runx' for 'run' command with appended arguments
oc kuberc set --section aliases --name runx --command run --option image=nginx --appendarg "--" --appendarg custom-arg1

# Overwrite an existing default
oc kuberc set --section defaults --command get --option output=json --overwrite

# Set the credential plugin policy and allowlist
oc kuberc set --section credentialplugin --policy Allowlist --allowlist-entry command=cloud-credential-helper
```

## Options

- `--allowlist-entry=[]`
  Allowlist entry the form field=value (can be specified multiple times)

- `--appendarg=[]`
  Argument to append to the command (can be specified multiple times, for aliases only)

- `--command=''`
  Command to configure (e.g., 'get', 'create', 'set env')

- `--kuberc=''`
  Path to the kuberc file to use for preferences. This can be disabled by exporting KUBECTL_KUBERC=false feature gate or turning off the feature KUBERC=off.

- `--name=''`
  Alias name (required for --section=aliases)

- `--option=[]`
  Flag option in the form flag=value (can be specified multiple times)

- `--overwrite=false`
  Allow overwriting existing entries

- `--policy=''`
  Plugin policy to use for exec credential plugins, must be one of 'AllowAll', 'DenyAll' or 'Allowlist'

- `--prependarg=[]`
  Argument to prepend to the command (can be specified multiple times, for aliases only)

- `--section=''`
  Section to modify: 'defaults', 'aliases', or 'credentialplugin'

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc kuberc set --help` / `gen-oc-help.py` で生成</sub>
