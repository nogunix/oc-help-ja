# `oc adm create-error-template`

> Create an error page template

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-error-template`

## Usage

```
oc adm create-error-template [flags] [options]
```

Create a template for customizing the error page

This command creates a basic template to use as a starting point for customizing the authentication error page. Save the output to a file and edit the template to change the look and feel or add content.

To use the template, set oauthConfig.templates.error in the master configuration to point to the template file. For example,

        oauthConfig:
        templates:
        error: templates/error.html

## Examples

```bash
# Output a template for the error page to stdout
oc adm create-error-template
```

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm create-error-template --help` / `gen-oc-help.py` で生成</sub>
