# `oc kustomize`

> Build a kustomization target from a directory or URL

[`oc`](oc.md) / `kustomize`

## Usage

```
oc kustomize DIR [flags] [options]
```

Build a set of KRM resources using a 'kustomization.yaml' file. The DIR argument must be a path to a directory containing 'kustomization.yaml', or a git repository URL with a path suffix specifying same with respect to the repository root. If DIR is omitted, '.' is assumed.

## Examples

```bash
# Build the current working directory
oc kustomize

# Build some shared configuration directory
oc kustomize /home/config/production

# Build from github
oc kustomize https://github.com/kubernetes-sigs/kustomize.git/examples/helloWorld?ref=v1.0.6
```

## Options

- `--as-current-user=false`
  use the uid and gid of the command executor to run the function in the container

- `--enable-alpha-plugins=false`
  enable kustomize plugins

- `--enable-helm=false`
  Enable use of the Helm chart inflator generator.

- `-e, --env=[]`
  a list of environment variables to be used by functions

- `--helm-api-versions=[]`
  Kubernetes api versions used by Helm for Capabilities.APIVersions

- `--helm-command='helm'`
  helm command (path to executable)

- `--helm-debug=false`
  Enable debug output from the Helm chart inflator generator.

- `--helm-kube-version=''`
  Kubernetes version used by Helm for Capabilities.KubeVersion

- `--load-restrictor='LoadRestrictionsRootOnly'`
  if set to 'LoadRestrictionsNone', local kustomizations may load files from outside their root. This does, however, break the relocatability of the kustomization.

- `--mount=[]`
  a list of storage options read from the filesystem

- `--network=false`
  enable network access for functions that declare it

- `--network-name='bridge'`
  the docker network to run the container in

- `-o, --output=''`
  If specified, write output to this path.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc kustomize --help` / `gen-oc-help.py` で生成</sub>
