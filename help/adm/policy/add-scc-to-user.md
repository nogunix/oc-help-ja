# `oc adm policy add-scc-to-user`

> Add a security context constraint to users or a service account

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-scc-to-user`

## Usage

```
oc adm policy add-scc-to-user SCC (USER | -z SERVICEACCOUNT) [USER ...] [flags] [options]
```

## Examples

```bash
# Add the 'restricted' security context constraint to user1 and user2
oc adm policy add-scc-to-user restricted user1 user2

# Add the 'privileged' security context constraint to serviceaccount1 in the current namespace
oc adm policy add-scc-to-user privileged -z serviceaccount1
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-z, --serviceaccount=[]`
  service account in the current namespace to use as a user

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy add-scc-to-user --help` / `gen-oc-help.py` で生成</sub>
