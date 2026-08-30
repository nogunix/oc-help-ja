# `oc auth whoami`

> Experimental: Check self subject attributes

[`oc`](../oc.md) / [`oc auth`](../auth.md) / `whoami`

## Usage

```
oc auth whoami [options]
```

Experimental: Check who you are and your attributes (groups, extra).

        This command is helpful to get yourself aware of the current user attributes,
        especially when dynamic authentication, e.g., token webhook, auth proxy, or OIDC provider,
        is enabled in the Kubernetes cluster.

## Examples

```bash
# Get your subject attributes
oc auth whoami

# Get your subject attributes in JSON format
oc auth whoami -o json
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc auth whoami --help` / `gen-oc-help.py` で生成</sub>
