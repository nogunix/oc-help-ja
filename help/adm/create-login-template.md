# `oc adm create-login-template`

> Create a login template

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-login-template`

## Usage

```
oc adm create-login-template [flags] [options]
```

Create a template for customizing the login page

This command creates a basic template to use as a starting point for customizing the login page. Save the output to a file and edit the template to change the look and feel or add content. Be careful not to remove any parameter values inside curly braces.

To use the template, set oauthConfig.templates.login in the master configuration to point to the template file. For example,

        oauthConfig:
        templates:
        login: templates/login.html

## Examples

```bash
# Output a template for the login page to stdout
oc adm create-login-template
```

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm create-login-template --help` / `gen-oc-help.py` で生成</sub>
