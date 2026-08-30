# `oc auth can-i`

> Check whether an action is allowed

[`oc`](../oc.md) / [`oc auth`](../auth.md) / `can-i`

## Usage

```
oc auth can-i VERB [TYPE | TYPE/NAME | NONRESOURCEURL] [options]
```

VERB is a logical Kubernetes API verb like 'get', 'list', 'watch', 'delete', etc. TYPE is a Kubernetes resource. Shortcuts and groups will be resolved. NONRESOURCEURL is a partial URL that starts with "/". NAME is the name of a particular Kubernetes resource. This command pairs nicely with impersonation. See --as global flag.

## Examples

```bash
# Check to see if I can create pods in any namespace
oc auth can-i create pods --all-namespaces

# Check to see if I can list deployments in my current namespace
oc auth can-i list deployments.apps

# Check to see if service account "foo" of namespace "dev" can list pods in the namespace "prod"
# You must be allowed to use impersonation for the global option "--as"
oc auth can-i list pods --as=system:serviceaccount:dev:foo -n prod

# Check to see if I can do everything in my current namespace ("*" means all)
oc auth can-i '*' '*'

# Check to see if I can get the job named "bar" in namespace "foo"
oc auth can-i list jobs.batch/bar -n foo

# Check to see if I can read pod logs
oc auth can-i get pods --subresource=log

# Check to see if I can access the URL /logs/
oc auth can-i get /logs/

# Check to see if I can approve certificates.k8s.io
oc auth can-i approve certificates.k8s.io

# List all allowed actions in namespace "foo"
oc auth can-i --list --namespace=foo
```

## Options

- `-A, --all-namespaces=false`
  If true, check the specified action in all namespaces.

- `--list=false`
  If true, prints all allowed actions.

- `--no-headers=false`
  If true, prints allowed actions without headers

- `-q, --quiet=false`
  If true, suppress output and just return the exit code.

- `--subresource=''`
  SubResource such as pod/log or deployment/scale

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc auth can-i --help` / `gen-oc-help.py` で生成</sub>
