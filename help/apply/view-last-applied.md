# `oc apply view-last-applied`

> View the latest last-applied-configuration annotations of a resource/object

[`oc`](../oc.md) / [`oc apply`](../apply.md) / `view-last-applied`

## Usage

```
oc apply view-last-applied (TYPE [NAME | -l label] | TYPE/NAME | -f FILENAME) [options]
```

View the latest last-applied-configuration annotations by type/name or file.

The default output will be printed to stdout in YAML format. You can use the -o option to change the output format.

## Examples

```bash
# View the last-applied-configuration annotations by type/name in YAML
oc apply view-last-applied deployment/nginx

# View the last-applied-configuration annotations by file in JSON
oc apply view-last-applied -f deploy.yaml -o json
```

## Options

- `--all=false`
  Select all resources in the namespace of the specified resource types

- `-f, --filename=[]`
  Filename, directory, or URL to files that contains the last-applied-configuration annotations

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-o, --output='yaml'`
  Output format. Must be one of (yaml, json)

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc apply view-last-applied --help` / `gen-oc-help.py` で生成</sub>
