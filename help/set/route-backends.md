# `oc set route-backends`

> Update the backends for a route

[`oc`](../oc.md) / [`oc set`](../set.md) / `route-backends`

## Usage

```
oc set route-backends ROUTENAME [--zero|--equal] [--adjust] SERVICE=WEIGHT[%] [...] [flags] [options]
```

Set and adjust route backends.

Routes may have one or more optional backend services with weights controlling how much traffic flows to each service. Traffic is assigned proportional to the combined weights of each backend. A weight of zero means that the backend will receive no traffic. If all weights are zero the route will not send traffic to any backends.

When setting backends, the first backend is the primary and the other backends are considered alternates. For example:

        $ oc set route-backends web prod=99 canary=1

will set the primary backend to service "prod" with a weight of 99 and the first alternate backend to service "canary" with a weight of 1. This means 99%% of traffic will be sent to the service "prod".

The --adjust flag allows you to alter the weight of an individual service relative to itself or to the primary backend. Specifying a percentage will adjust the backend relative to either the primary or the first alternate (if you specify the primary). If there are other backends their weights will be kept proportional to the changed.

Not all routers may support multiple or weighted backends.

## Examples

```bash
# Print the backends on the route 'web'
oc set route-backends web

# Set two backend services on route 'web' with 2/3rds of traffic going to 'a'
oc set route-backends web a=2 b=1

# Increase the traffic percentage going to b by 10%% relative to a
oc set route-backends web --adjust b=+10%%

# Set traffic percentage going to b to 10%% of the traffic going to a
oc set route-backends web --adjust b=10%%

# Set weight of b to 10
oc set route-backends web --adjust b=10

# Set the weight to all backends to zero
oc set route-backends web --zero
```

## Options

- `--adjust=false`
  Adjust a single backend using an absolute or relative weight. If the primary backend is selected and there is more than one alternate an error will be returned.

- `--all=false`
  If true, select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--equal=false`
  If true, set the weight of all backends to 100.

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

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `-l, --selector=''`
  Selector (label query) to filter on

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--zero=false`
  If true, set the weight of all backends to zero.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set route-backends --help` / `gen-oc-help.py` で生成</sub>
