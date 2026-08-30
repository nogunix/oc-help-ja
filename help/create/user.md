# `oc create user`

> Manually create a user (only needed if automatic creation is disabled)

[`oc`](../oc.md) / [`oc create`](../create.md) / `user`

## Usage

```
oc create user NAME [flags] [options]
```

This command can be used to create a user object.

Typically, users are created automatically during login. If automatic creation is disabled (by using the "lookup" mapping method), users must be created manually.

Corresponding identity and user identity mapping objects must also be created to allow logging in as the created user.

## Examples

```bash
# Create a user with the username "ajones" and the display name "Adam Jones"
oc create user ajones --full-name="Adam Jones"
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--full-name=''`
  Display name of the user

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

<sub>`$ oc create user --help` / `gen-oc-help.py` で生成</sub>
