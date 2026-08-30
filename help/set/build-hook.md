# `oc set build-hook`

> Update a build hook on a build config

[`oc`](../oc.md) / [`oc set`](../set.md) / `build-hook`

## Usage

```
oc set build-hook BUILDCONFIG --post-commit [--command] [--script] -- CMD [flags] [options]
```

Set or remove a build hook on a build config.

Build hooks allow behavior to be injected into the build process.

A post-commit build hook is executed after a build has committed an image but before the image has been pushed to a registry. It can be used to execute tests on the image and verify it before it is made available in a registry or for any other logic that is needed to execute before the image is pushed to the registry. A new container with the recently built image is launched with the build hook command. If the command or script run by the build hook returns a non-zero exit code, the resulting image will not be pushed to the registry.

The command for a build hook may be specified as a shell script (with the --script argument), as a new entrypoint command on the image with the --command argument, or as a set of arguments to the image's entrypoint (default).

## Examples

```bash
# Clear post-commit hook on a build config
oc set build-hook bc/mybuild --post-commit --remove

# Set the post-commit hook to execute a test suite using a new entrypoint
oc set build-hook bc/mybuild --post-commit --command -- /bin/bash -c /var/lib/test-image.sh

# Set the post-commit hook to execute a shell script
oc set build-hook bc/mybuild --post-commit --script="/var/lib/test-image.sh param1 param2 && /var/lib/done.sh"
```

## Options

- `--all=false`
  If true, select all build configs in the namespace

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--command=false`
  If true, set the entrypoint of the hook container to the given command

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--local=false`
  If true, set image will NOT contact api-server but run locally.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--post-commit=false`
  If true, set the post-commit build hook on a build config

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove=false`
  If true, remove the build hook.

- `--script=''`
  Specify a script to run for the build-hook

- `-l, --selector=''`
  Selector (label query) to filter build configs

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set build-hook --help` / `gen-oc-help.py` で生成</sub>
