# `oc autoscale`

> Autoscale a deployment config, deployment, replica set, stateful set, or replication controller

[`oc`](oc.md) / `autoscale`

## Usage

```
oc autoscale (-f FILENAME | TYPE NAME | TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu=CPU] [--memory=MEMORY] [options]
```

Creates an autoscaler that automatically chooses and sets the number of pods that run in a Kubernetes cluster. The command will attempt to use the autoscaling/v2 API first, in case of an error, it will fall back to autoscaling/v1 API.

Looks up a deployment, replica set, stateful set, or replication controller by name and creates an autoscaler that uses the given resource as a reference. An autoscaler can automatically increase or decrease number of pods deployed within the system as needed.

## Examples

```bash
# Auto scale a deployment "foo", with the number of pods between 2 and 10, no target CPU utilization specified so a default autoscaling policy will be used
oc autoscale deployment foo --min=2 --max=10

# Auto scale a replication controller "foo", with the number of pods between 1 and 5, target CPU utilization at 80%
oc autoscale rc foo --max=5 --cpu=80%

# Auto scale a deployment "bar", with the number of pods between 3 and 6, target average CPU of 500m and memory of 200Mi
oc autoscale deployment bar --min=3 --max=6 --cpu=500m --memory=200Mi

# Auto scale a deployment "bar", with the number of pods between 2 and 8, target CPU utilization 60% and memory utilization 70%
oc autoscale deployment bar --min=3 --max=6 --cpu=60% --memory=70%
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--cpu=''`
  Target CPU utilization over all the pods. When specified as a percentage (e.g."70%" for 70% of requested CPU) it will target average utilization. When specified as quantity (e.g."500m" for 500 milliCPU) it will target average value. Value without units is treated as a quantity with miliCPU being the unit (e.g."500" is "500m").

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-autoscale'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files identifying the resource to autoscale.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--max=-1`
  The upper limit for the number of pods that can be set by the autoscaler. Required.

- `--memory=''`
  Target memory utilization over all the pods. When specified  as a percentage (e.g."60%" for 60% of requested memory) it will target average utilization. When specified as quantity (e.g."200Mi" for 200 MiB, "1Gi" for 1 GiB) it will target average value. Value without units is treated as a quantity with mebibytes being the unit (e.g."200" is "200Mi").

- `--min=-1`
  The lower limit for the number of pods that can be set by the autoscaler. If it's not specified or negative, the server will apply a default value.

- `--name=''`
  The name for the newly created object. If not specified, the name of the input resource will be used.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc autoscale --help` / `gen-oc-help.py` で生成</sub>
