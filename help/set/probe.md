# `oc set probe`

> Update a probe on a pod template

[`oc`](../oc.md) / [`oc set`](../set.md) / `probe`

## Usage

```
oc set probe RESOURCE/NAME --readiness|--liveness [flags] (--get-url=URL|--open-tcp=PORT|-- CMD) [options]
```

Set or remove a liveness, readiness or startup probe from a pod or pod template.

Each container in a pod may define one or more probes that are used for general health checking. A liveness probe is checked periodically to ensure the container is still healthy: if the probe fails, the container is restarted. Readiness probes set or clear the ready flag for each container, which controls whether the container's ports are included in the list of endpoints for a service and whether a deployment can proceed. A readiness check should indicate when your container is ready to accept incoming traffic or begin handling work. A startup probe allows additional startup time for a container before a liveness probe is started. Setting both liveness and readiness probes for each container is highly recommended.

The three probe types are:

1.  Open a TCP socket on the pod IP
2.  Perform an HTTP GET against a URL on a container that must return 200 OK
3.  Run a command in the container that must return exit code 0

Containers that take a variable amount of time to start should set generous initial-delay-seconds values, otherwise as your application evolves you may suddenly begin to fail.

## Examples

```bash
# Clear both readiness and liveness probes off all containers
oc set probe dc/myapp --remove --readiness --liveness

# Set an exec action as a liveness probe to run 'echo ok'
oc set probe dc/myapp --liveness -- echo ok

# Set a readiness probe to try to open a TCP socket on 3306
oc set probe rc/mysql --readiness --open-tcp=3306

# Set an HTTP startup probe for port 8080 and path /healthz over HTTP on the pod IP
oc set probe dc/webapp --startup --get-url=http://:8080/healthz

# Set an HTTP readiness probe for port 8080 and path /healthz over HTTP on the pod IP
oc set probe dc/webapp --readiness --get-url=http://:8080/healthz

# Set an HTTP readiness probe over HTTPS on 127.0.0.1 for a hostNetwork pod
oc set probe dc/router --readiness --get-url=https://127.0.0.1:1936/stats

# Set only the initial-delay-seconds field on all deployments
oc set probe dc --all --readiness --initial-delay-seconds=30
```

## Options

- `--all=false`
  If true, select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-c, --containers='*'`
  The names of containers in the selected pod templates to change - may use wildcards

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--failure-threshold=0`
  The number of failures before the probe is considered to have failed

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `--get-url=''`
  A URL to perform an HTTP GET on (you can omit the host, have a string port, or omit the scheme.

- `--initial-delay-seconds=0`
  The time in seconds to wait before the probe begins checking

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--liveness=false`
  Set or remove a liveness probe to verify this container is running

- `--local=false`
  If true, set image will NOT contact api-server but run locally.

- `--open-tcp=''`
  A port number or port name to attempt to open via TCP.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--period-seconds=0`
  The time in seconds between attempts

- `--readiness=false`
  Set or remove a readiness probe to indicate when this container should receive traffic

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove=false`
  If true, remove the specified probe(s).

- `-l, --selector=''`
  Selector (label query) to filter on

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--startup=false`
  Set or remove a startup probe to verify this container is running

- `--success-threshold=0`
  The number of successes required before the probe is considered successful

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--timeout-seconds=0`
  The time in seconds to wait before considering the probe to have failed

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set probe --help` / `gen-oc-help.py` で生成</sub>
