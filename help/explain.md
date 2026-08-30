# `oc explain`

> Get documentation for a resource

[`oc`](oc.md) / `explain`

## Usage

```
oc explain TYPE [--recursive=FALSE|TRUE] [--api-version=api-version-group] [-o|--output=plaintext|plaintext-openapiv2] [options]
```

Describe fields and structure of various resources.

This command describes the fields associated with each supported API resource. Fields are identified via a simple JSONPath identifier:

        <type>.<fieldName>[.<fieldName>]

Information about each field is retrieved from the server in OpenAPI format.

Use "oc api-resources" for a complete list of supported resources.

## Examples

```bash
# Get the documentation of the resource and its fields
oc explain pods

# Get all the fields in the resource
oc explain pods --recursive

# Get the explanation for deployment in supported api versions
oc explain deployments --api-version=apps/v1

# Get the documentation of a specific field of a resource
oc explain pods.spec.containers

# Get the documentation of resources in different format
oc explain deployment --output=plaintext-openapiv2
```

## Options

- `--api-version=''`
  Get different explanations for particular API version (API group/version)

- `-o, --output='plaintext'`
  Format in which to render the schema (plaintext, plaintext-openapiv2)

- `--recursive=false`
  Print the fields of fields (Currently only 1 level deep)

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc explain --help` / `gen-oc-help.py` で生成</sub>
