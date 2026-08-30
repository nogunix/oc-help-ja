# `oc rollout status`

> Show the status of the rollout

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `status`

## Usage

```
oc rollout status (TYPE NAME | TYPE/NAME) [flags] [options]
```

By default 'rollout status' will watch the status of the latest rollout until it is done. If you do not want to wait for the rollout to finish then you can use --watch=false. Note that if a new rollout starts in-between, then 'rollout status' will continue watching the latest revision. If you want to pin to a specific revision and abort if it is rolled over by another revision, use --revision=N where N is the revision you need to watch for.

## Examples

```bash
# Watch the rollout status of a deployment
oc rollout status deployment/nginx
```

## Options

- `-f, --filename=[]`
  Filename, directory, or URL to files identifying the resource to get from a server.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--revision=0`
  Pin to a specific revision for showing its status. Defaults to 0 (last revision).

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

- `--timeout=0s`
  The length of time to wait before ending watch, zero means never. Any other values should contain a corresponding time unit (e.g. 1s, 2m, 3h).

- `-w, --watch=true`
  Watch the status of the rollout until it's done.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc rollout status --help` / `gen-oc-help.py` で生成</sub>
