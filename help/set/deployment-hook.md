# `oc set deployment-hook`

> Update a deployment hook on a deployment config

[`oc`](../oc.md) / [`oc set`](../set.md) / `deployment-hook`

## Usage

```
oc set deployment-hook DEPLOYMENTCONFIG --pre|--post|--mid -- CMD [flags] [options]
```

Set or remove a deployment hook on a deployment config.

Deployment configs allow hooks to execute at different points in the lifecycle of the deployment, depending on the deployment strategy.

For deployments with a Recreate strategy, a Pre, Mid, and Post hook can be specified. The Pre hook will execute before the deployment starts. The Mid hook will execute once the previous deployment has been scaled down to 0, but before the new one ramps up. The Post hook will execute once the deployment has completed.

For deployments with a Rolling strategy, a Pre and Post hook can be specified. The Pre hook will execute before the deployment starts and the Post hook will execute once the deployment has completed.

For each hook, a new pod will be started using one of the containers in the deployment's pod template with a specific command to execute. Additional environment variables may be specified for the hook, as well as which volumes from the pod template will be mounted on the hook pod.

Each hook can have its own cancellation policy. One of: abort, retry, or ignore. Not all cancellation policies can be set on all hooks. For example, a Post hook on a rolling strategy does not support the abort policy, because at that point the deployment has already happened.

## Examples

```bash
# Clear pre and post hooks on a deployment config
oc set deployment-hook dc/myapp --remove --pre --post

# Set the pre deployment hook to execute a db migration command for an application
# using the data volume from the application
oc set deployment-hook dc/myapp --pre --volumes=data -- /var/lib/migrate-db.sh

# Set a mid deployment hook along with additional environment variables
oc set deployment-hook dc/myapp --mid --volumes=data -e VAR1=value1 -e VAR2=value2 -- /var/lib/prepare-deploy.sh
```

## Options

- `--all=false`
  If true, select all deployment configs in the namespace

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-c, --container=''`
  The name of the container in the selected deployment config to use for the deployment hook

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-e, --environment=[]`
  Environment variable to use in the deployment hook pod

- `--failure-policy='ignore'`
  The failure policy for the deployment hook. Valid values are: abort,retry,ignore

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--local=false`
  If true, set deployment hook will NOT contact api-server but run locally.

- `--mid=false`
  Set or remove a mid deployment hook

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--post=false`
  Set or remove a post deployment hook

- `--pre=false`
  Set or remove a pre deployment hook

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove=false`
  If true, remove the specified deployment hook(s).

- `-l, --selector=''`
  Selector (label query) to filter deployment configs

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--volumes=[]`
  Volumes from the pod template to use in the deployment hook pod

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set deployment-hook --help` / `gen-oc-help.py` で生成</sub>
