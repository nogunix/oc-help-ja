# `oc set triggers`

> Update the triggers on one or more objects

[`oc`](../oc.md) / [`oc set`](../set.md) / `triggers`

## Usage

```
oc set triggers RESOURCE/NAME [--from-config|--from-image|--from-github|--from-webhook] [--auto|--manual] [flags] [options]
```

Set or remove triggers.

Build configs, deployment configs, and most Kubernetes workload objects may have a set of triggers that result in a new deployment or build being created when an image changes. This command enables you to alter those triggers - making them automatic or manual, adding new entries, or changing existing entries.

Deployments support triggering off of image changes and on config changes. Config changes are any alterations to the pod template, while image changes will result in the container image value being updated whenever an image stream tag is updated. You may also trigger Kubernetes stateful sets, daemon sets, deployments, and cron jobs from images. Disabling the config change trigger is equivalent to pausing most objects. Deployment configs will not perform their first deployment until all image change triggers have been submitted.

Build configs support triggering off of image changes, config changes, and webhooks. The config change trigger for a build config will only trigger the first build.

## Examples

```bash
# Print the triggers on the deployment config 'myapp'
oc set triggers dc/myapp

# Set all triggers to manual
oc set triggers dc/myapp --manual

# Enable all automatic triggers
oc set triggers dc/myapp --auto

# Reset the GitHub webhook on a build to a new, generated secret
oc set triggers bc/webapp --from-github
oc set triggers bc/webapp --from-webhook

# Remove all triggers
oc set triggers bc/webapp --remove-all

# Stop triggering on config change
oc set triggers dc/myapp --from-config --remove

# Add an image trigger to a build config
oc set triggers bc/webapp --from-image=namespace1/image:latest

# Add an image trigger to a stateful set on the main container
oc set triggers statefulset/db --from-image=namespace1/image:latest -c main
```

## Options

- `--all=false`
  If true, select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--auto=false`
  If true, enable all triggers, or just the specified trigger

- `-c, --containers=''`
  Comma delimited list of container names this trigger applies to on deployments; defaults to the name of the only container

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `--from-bitbucket=false`
  If true, a Bitbucket webhook - a secret value will be generated automatically

- `--from-config=false`
  If set, configuration changes will result in a change

- `--from-github=false`
  If true, a GitHub webhook - a secret value will be generated automatically

- `--from-gitlab=false`
  If true, a GitLab webhook - a secret value will be generated automatically

- `--from-image=''`
  An image stream tag to trigger off of

- `--from-webhook=false`
  If true, a generic webhook - a secret value will be generated automatically

- `--from-webhook-allow-env=false`
  If true, a generic webhook which can provide environment variables - a secret value will be generated automatically

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--local=false`
  If true, set image will NOT contact api-server but run locally.

- `--manual=false`
  If true, set all triggers to manual, or just the specified trigger

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove=false`
  If true, remove the specified trigger(s).

- `--remove-all=false`
  If true, remove all triggers.

- `-l, --selector=''`
  Selector (label query) to filter on

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set triggers --help` / `gen-oc-help.py` で生成</sub>
