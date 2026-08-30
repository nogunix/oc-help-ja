# `oc rollout cancel`

> Cancel the in-progress deployment

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `cancel`

## Usage

```
oc rollout cancel (TYPE NAME | TYPE/NAME) [flags] [options]
```

Running this command will cause the current in-progress deployment to be cancelled, but keep in mind that this is a best-effort operation and may take some time to complete. It’s possible the deployment will partially or totally complete before the cancellation is effective. In such a case an appropriate event will be emitted.

## Examples

```bash
# Cancel the in-progress deployment based on 'nginx'
oc rollout cancel dc/nginx
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

<sub>`$ oc rollout cancel --help` / `gen-oc-help.py` で生成</sub>
