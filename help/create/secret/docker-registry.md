# `oc create secret docker-registry`

> Create a secret for use with a Docker registry

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create secret`](../secret.md) / `docker-registry`

## Usage

```
oc create secret docker-registry NAME --docker-username=user --docker-password=password --docker-email=email [--docker-server=string] [--from-file=[key=]source] [--dry-run=server|client|none] [options]
```

Create a new secret for use with Docker registries.

        Dockercfg secrets are used to authenticate against Docker registries.

        When using the Docker command line to push images, you can authenticate to a given registry by running:
        '$ docker login DOCKER_REGISTRY_SERVER --username=DOCKER_USER --password=DOCKER_PASSWORD --email=DOCKER_EMAIL'.

That produces a ~/.dockercfg file that is used by subsequent 'docker push' and 'docker pull' commands to authenticate to the registry. The email address is optional.

        When creating applications, you may have a Docker registry that requires authentication.  In order for the
        nodes to pull images on your behalf, they must have the credentials.  You can provide this information
        by creating a dockercfg secret and attaching it to your service account.

## Examples

```bash
# If you do not already have a .dockercfg file, create a dockercfg secret directly
oc create secret docker-registry my-secret --docker-server=DOCKER_REGISTRY_SERVER --docker-username=DOCKER_USER --docker-password=DOCKER_PASSWORD --docker-email=DOCKER_EMAIL

# Create a new secret named my-secret from ~/.docker/config.json
oc create secret docker-registry my-secret --from-file=path/to/.docker/config.json
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--append-hash=false`
  Append a hash of the secret to its name.

- `--docker-email=''`
  Email for Docker registry

- `--docker-password=''`
  Password for Docker registry authentication

- `--docker-server='https://index.docker.io/v1/'`
  Server location for Docker registry

- `--docker-username=''`
  Username for Docker registry authentication

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-create'`
  Name of the manager used to track field ownership.

- `--from-file=[]`
  Key files can be specified using their file path, in which case a default name of .dockerconfigjson will be given to them, or optionally with a name and file path, in which case the given name will be used. Specifying a directory will iterate each named file in the directory that is a valid secret key. For this command, the key should always be .dockerconfigjson.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--validate='ignore'`
  Must be one of: strict (or true), warn, ignore (or false). "true" or "strict" will use a schema to validate the input and fail the request if invalid. It will perform server side validation if ServerSideFieldValidation is enabled on the api-server, but will fall back to less reliable client-side validation if not. "warn" will warn about unknown or duplicate fields without blocking the request if server-side field validation is enabled on the API server, and behave as "ignore" otherwise. "false" or "ignore" will not perform any schema validation, silently dropping any unknown or duplicate fields.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create secret docker-registry --help` / `gen-oc-help.py` で生成</sub>
