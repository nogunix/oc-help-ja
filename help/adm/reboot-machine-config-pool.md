# `oc adm reboot-machine-config-pool`

> Initiate reboot of the specified MachineConfigPool

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `reboot-machine-config-pool`

## Usage

```
oc adm reboot-machine-config-pool [options]
```

Reboot the specified machine config pool by modifying an appropriate MachineConfig.

Does not wait for the reboot to complete, only initiates it.  This command will honor paused pools. Degraded, failed, or otherwise not healthy nodes will not restart.

Experimental: This command is under active development and may change without notice.

## Examples

```bash
# Reboot all MachineConfigPools
oc adm reboot-machine-config-pool mcp/worker mcp/master

# Reboot all MachineConfigPools that inherit from worker.  This include all custom MachineConfigPools and infra.
oc adm reboot-machine-config-pool mcp/worker

# Reboot masters
oc adm reboot-machine-config-pool mcp/master
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--dry-run=false`
  Set to true to use server-side dry run.

- `-f, --filename=[]`
  identifying the resource.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=true`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm reboot-machine-config-pool --help` / `gen-oc-help.py` で生成</sub>
