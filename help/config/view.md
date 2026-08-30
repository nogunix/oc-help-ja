# `oc config view`

> Display merged kubeconfig settings or a specified kubeconfig file

[`oc`](../oc.md) / [`oc config`](../config.md) / `view`

## Usage

```
oc config view [flags] [options]
```

You can use --output jsonpath={...} to extract specific values using a jsonpath expression.

## Examples

```bash
# Show merged kubeconfig settings
oc config view

# Show merged kubeconfig settings, raw certificate data, and exposed secrets
oc config view --raw

# Get the password for the e2e user
oc config view -o jsonpath='{.users[?(@.name == "e2e")].user.password}'
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--flatten=false`
  Flatten the resulting kubeconfig file into self-contained output (useful for creating portable kubeconfig files)

- `--merge=true`
  Merge the full hierarchy of kubeconfig files

- `--minify=false`
  Remove all information not used by current-context from the output

- `-o, --output='yaml'`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--raw=false`
  Display raw byte data and sensitive data

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config view --help` / `gen-oc-help.py` で生成</sub>
