# `oc create identity`

> Manually create an identity (only needed if automatic creation is disabled)

[`oc`](../oc.md) / [`oc create`](../create.md) / `identity`

## Usage

```
oc create identity <PROVIDER_NAME>:<PROVIDER_USER_NAME> [flags] [options]
```

This command can be used to create an identity object.

Typically, identities are created automatically during login. If automatic creation is disabled (by using the "lookup" mapping method), identities must be created manually.

Corresponding user and user identity mapping objects must also be created to allow logging in with the created identity.

## Examples

```bash
# Create an identity with identity provider "acme_ldap" and the identity provider username "adamjones"
oc create identity acme_ldap:adamjones
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

<sub>`$ oc create identity --help` / `gen-oc-help.py` で生成</sub>
