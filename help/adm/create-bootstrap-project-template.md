# `oc adm create-bootstrap-project-template`

> Create a bootstrap project template

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-bootstrap-project-template`

## Usage

```
oc adm create-bootstrap-project-template [flags] [options]
```

## Examples

```bash
# Output a bootstrap project template in YAML format to stdout
oc adm create-bootstrap-project-template -o yaml
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--name='project-request'`
  The name of the template to output.

- `-o, --output='json'`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm create-bootstrap-project-template --help` / `gen-oc-help.py` で生成</sub>
