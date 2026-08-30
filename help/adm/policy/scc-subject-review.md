# `oc adm policy scc-subject-review`

> Check whether a user or a service account can create a pod

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `scc-subject-review`

## Usage

```
oc adm policy scc-subject-review [flags] [options]
```

Check whether a user, service account or group can create a pod. It returns a list of security context constraints that will admit the resource. If user is specified but not groups, it is interpreted as "what if the user is not a member of any groups". If user and groups are empty, then the check is performed using the current user.

## Examples

```bash
# Check whether user bob can create a pod specified in myresource.yaml
oc adm policy scc-subject-review -u bob -f myresource.yaml

# Check whether user bob who belongs to projectAdmin group can create a pod specified in myresource.yaml
oc adm policy scc-subject-review -u bob -g projectAdmin -f myresource.yaml

# Check whether a service account specified in the pod template spec in myresourcewithsa.yaml can create the pod
oc adm policy scc-subject-review -f myresourcewithsa.yaml
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-f, --filename=[]`
  Filename, directory, or URL to files Filename, directory, or URL to a file identifying the resource to get from a server.

- `-g, --groups=[]`
  Comma separated, list of groups. Review will be performed on behalf of these groups

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--no-headers=false`
  When using the default output format, don't print headers (default print headers).

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-z, --serviceaccount=''`
  service account in the current namespace to use as a user

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `-u, --user=''`
  Review will be performed on behalf of this user

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm policy scc-subject-review --help` / `gen-oc-help.py` で生成</sub>
