# `oc rollout retry`

> Retry the latest failed rollout

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `retry`

## Usage

```
oc rollout retry (TYPE NAME | TYPE/NAME) [flags] [options]
```

If a rollout fails, you may opt to retry it (if the error was transient). Some rollouts may never successfully complete - in which case you can use the rollout latest to force a redeployment. If a deployment config has completed rolling out successfully at least once in the past, it would be automatically rolled back in the event of a new failed rollout. Note that you would still need to update the erroneous deployment config in order to have its template persisted across your application.

## Examples

```bash
# Retry the latest failed deployment based on 'frontend'
# The deployer pod and any hook pods are deleted for the latest failed deployment
oc rollout retry dc/frontend
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-f, --filename=[]`
  Filename, directory, or URL to files Filename, directory, or URL to a file identifying the resource to get from a server.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc rollout retry --help` / `gen-oc-help.py` で生成</sub>
