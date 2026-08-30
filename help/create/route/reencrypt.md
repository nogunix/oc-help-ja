# `oc create route reencrypt`

> Create a route that uses reencrypt TLS termination

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create route`](../route.md) / `reencrypt`

## Usage

```
oc create route reencrypt [NAME] --service=SERVICE [flags] [options]
```

Specify the service (either just its name or using type/name syntax) that the generated route should expose using the --service flag. You may also specify a destination CA certificate using the --dest-ca-cert flag. If --dest-ca-cert is omitted, the route will use the service CA, meaning the service must use a serving certificate from the serving cert signer.

## Examples

```bash
# Create a route named "my-route" that exposes the frontend service
oc create route reencrypt my-route --service=frontend --dest-ca-cert cert.cert

# Create a reencrypt route that exposes the frontend service, letting the
# route name default to the service name and the destination CA certificate
# default to the service CA
oc create route reencrypt --service=frontend
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--ca-cert=''`
  Path to a CA certificate file.

- `--cert=''`
  Path to a certificate file.

- `--dest-ca-cert=''`
  Path to a CA certificate file, used for securing the connection from the router to the destination. Defaults to the Service CA.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--hostname=''`
  Set a hostname for the new route

- `--insecure-policy=''`
  Set an insecure policy for the new route

- `--key=''`
  Path to a key file.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--path=''`
  Path that the router watches to route traffic to the service.

- `--port=''`
  Name of the service port or number of the container port the route will route traffic to

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--service=''`
  Name of the service that the new route is exposing

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--validate='ignore'`
  Must be one of: strict (or true), warn, ignore (or false). "true" or "strict" will use a schema to validate the input and fail the request if invalid. It will perform server side validation if ServerSideFieldValidation is enabled on the api-server, but will fall back to less reliable client-side validation if not. "warn" will warn about unknown or duplicate fields without blocking the request if server-side field validation is enabled on the API server, and behave as "ignore" otherwise. "false" or "ignore" will not perform any schema validation, silently dropping any unknown or duplicate fields.

- `--wildcard-policy=''`
  Sets the WilcardPolicy for the hostname, the default is "None". valid values are "None" and "Subdomain"

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create route reencrypt --help` / `gen-oc-help.py` で生成</sub>
