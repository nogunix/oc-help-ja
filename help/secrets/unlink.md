# `oc secrets unlink`

> Detach secrets from a service account

[`oc`](../oc.md) / [`oc secrets`](../secrets.md) / `unlink`

## Usage

```
oc secrets unlink serviceaccount-name secret-name [another-secret-name] ... [flags] [options]
```

Unlink (detach) secrets from a service account.

If a secret is no longer valid for a pod, build or image pull, you may unlink it from a service account.

## Examples

```bash
# Unlink a secret currently associated with a service account
oc secrets unlink serviceaccount-name secret-name another-secret-name ...
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

<sub>`$ oc secrets unlink --help` / `gen-oc-help.py` で生成</sub>
