# `oc adm policy who-can`

> List who can perform the specified action on a resource

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `who-can`

## Usage

```
oc adm policy who-can VERB RESOURCE [NAME] [flags] [options]
```

## Options

- `-A, --all-namespaces=false`
  If true, list who can perform the specified action in all namespaces.

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--subresource=''`
  SubResource such as log or scale

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy who-can --help` / `gen-oc-help.py` で生成</sub>
