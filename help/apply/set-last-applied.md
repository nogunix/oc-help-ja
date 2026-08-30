# `oc apply set-last-applied`

> Set the last-applied-configuration annotation on a live object to match the contents of a file

[`oc`](../oc.md) / [`oc apply`](../apply.md) / `set-last-applied`

## Usage

```
oc apply set-last-applied -f FILENAME [options]
```

Set the latest last-applied-configuration annotations by setting it to match the contents of a file. This results in the last-applied-configuration being updated as though 'oc apply -f`<file>` ' was run, without updating any other parts of the object.

## Examples

```bash
# Set the last-applied-configuration of a resource to match the contents of a file
oc apply set-last-applied -f deploy.yaml

# Execute set-last-applied against each configuration file in a directory
oc apply set-last-applied -f path/

# Set the last-applied-configuration of a resource to match the contents of a file; will create the annotation if it does not already exist
oc apply set-last-applied -f deploy.yaml --create-annotation=true
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--create-annotation=false`
  Will create 'last-applied-configuration' annotations if current objects doesn't have one

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-f, --filename=[]`
  Filename, directory, or URL to files that contains the last-applied-configuration annotations

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc apply set-last-applied --help` / `gen-oc-help.py` で生成</sub>
