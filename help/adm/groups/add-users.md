# `oc adm groups add-users`

> Add users to a group

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm groups`](../groups.md) / `add-users`

## Usage

```
oc adm groups add-users GROUP USER [USER ...] [flags] [options]
```

This command will append unique users to the list of members for a group.

## Examples

```bash
# Add user1 and user2 to my-group
oc adm groups add-users my-group user1 user2
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm groups add-users --help` / `gen-oc-help.py` で生成</sub>
