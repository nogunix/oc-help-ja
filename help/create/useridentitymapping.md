# `oc create useridentitymapping`

> Manually map an identity to a user

[`oc`](../oc.md) / [`oc create`](../create.md) / `useridentitymapping`

## Usage

```
oc create useridentitymapping <IDENTITY_NAME> <USER_NAME> [flags] [options]
```

Typically, identities are automatically mapped to users during login. If automatic mapping is disabled (by using the "lookup" mapping method), or a mapping needs to be manually established between an identity and a user, this command can be used to create a user identity mapping object.

## Examples

```bash
# Map the identity "acme_ldap:adamjones" to the user "ajones"
oc create useridentitymapping acme_ldap:adamjones ajones
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create useridentitymapping --help` / `gen-oc-help.py` で生成</sub>
