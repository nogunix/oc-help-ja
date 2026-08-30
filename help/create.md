# `oc create`

> Create a resource from a file or from stdin

[`oc`](oc.md) / `create`

## Usage

```
oc create -f FILENAME [options]
```

JSON and YAML formats are accepted.

## Subcommands

- [`build`](create/build.md) — Create a new build
- [`clusterresourcequota`](create/clusterresourcequota.md) — Create a cluster resource quota
- [`clusterrole`](create/clusterrole.md) — Create a cluster role
- [`clusterrolebinding`](create/clusterrolebinding.md) — Create a cluster role binding for a particular cluster role
- [`configmap`](create/configmap.md) — Create a config map from a local file, directory or literal value
- [`cronjob`](create/cronjob.md) — Create a cron job with the specified name
- [`deployment`](create/deployment.md) — Create a deployment with the specified name
- [`deploymentconfig`](create/deploymentconfig.md) — Create a deployment config with default options that uses a given image
- [`identity`](create/identity.md) — Manually create an identity (only needed if automatic creation is disabled)
- [`imagestream`](create/imagestream.md) — Create a new empty image stream
- [`imagestreamtag`](create/imagestreamtag.md) — Create a new image stream tag
- [`ingress`](create/ingress.md) — Create an ingress with the specified name
- [`job`](create/job.md) — Create a job with the specified name
- [`namespace`](create/namespace.md) — Create a namespace with the specified name
- [`poddisruptionbudget`](create/poddisruptionbudget.md) — Create a pod disruption budget with the specified name
- [`priorityclass`](create/priorityclass.md) — Create a priority class with the specified name
- [`quota`](create/quota.md) — Create a quota with the specified name
- [`role`](create/role.md) — Create a role with single rule
- [`rolebinding`](create/rolebinding.md) — Create a role binding for a particular role or cluster role
- [`route`](create/route.md) — Expose containers externally via secured routes
- [`secret`](create/secret.md) — Create a secret using a specified subcommand
- [`service`](create/service.md) — Create a service using a specified subcommand
- [`serviceaccount`](create/serviceaccount.md) — Create a service account with the specified name
- [`token`](create/token.md) — Request a service account token
- [`user`](create/user.md) — Manually create a user (only needed if automatic creation is disabled)
- [`useridentitymapping`](create/useridentitymapping.md) — Manually map an identity to a user

## Examples

```bash
# Create a pod using the data in pod.json
oc create -f ./pod.json

# Create a pod based on the JSON passed into stdin
cat pod.json | oc create -f -

# Edit the data in registry.yaml in JSON then create the resource using the edited data
oc create -f registry.yaml --edit -o json
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--edit=false`
  Edit the API resource before creating

- `--field-manager='kubectl-create'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to create the resource

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--raw=''`
  Raw URI to POST to the server.  Uses the transport specified by the kubeconfig file.

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--validate='ignore'`
  Must be one of: strict (or true), warn, ignore (or false). "true" or "strict" will use a schema to validate the input and fail the request if invalid. It will perform server side validation if ServerSideFieldValidation is enabled on the api-server, but will fall back to less reliable client-side validation if not. "warn" will warn about unknown or duplicate fields without blocking the request if server-side field validation is enabled on the API server, and behave as "ignore" otherwise. "false" or "ignore" will not perform any schema validation, silently dropping any unknown or duplicate fields.

- `--windows-line-endings=false`
  Only relevant if --edit=true. Defaults to the line ending native to your platform.

> Use "oc create `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create --help` / `gen-oc-help.py` で生成</sub>
