# `oc adm create-provider-selection-template`

> Create a provider selection template

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-provider-selection-template`

## Usage

```
oc adm create-provider-selection-template [flags] [options]
```

Create a template for customizing the provider selection page

This command creates a basic template to use as a starting point for customizing the login provider selection page. Save the output to a file and edit the template to change the look and feel or add content. Be careful not to remove any parameter values inside curly braces.

To use the template, set oauthConfig.templates.providerSelection in the master configuration to point to the template file. For example,

        oauthConfig:
        templates:
        providerSelection: templates/provider-selection.html

## Examples

```bash
# Output a template for the provider selection page to stdout
oc adm create-provider-selection-template
```

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm create-provider-selection-template --help` / `gen-oc-help.py` で生成</sub>
