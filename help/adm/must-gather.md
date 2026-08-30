# `oc adm must-gather`

> Launch a new instance of a pod for gathering debug information

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `must-gather`

## Usage

```
oc adm must-gather [flags] [options]
```

Launch a pod to gather debugging information.

This command will launch a pod in a temporary namespace on your cluster that gathers debugging information and then downloads the gathered information.

## Examples

```bash
# Gather information using the default plug-in image and command, writing into ./must-gather.local.<rand>
oc adm must-gather

# Gather information with a specific local folder to copy to
oc adm must-gather --dest-dir=/local/directory

# Gather audit information
oc adm must-gather -- /usr/bin/gather_audit_logs

# Gather information using multiple plug-in images
oc adm must-gather --image=quay.io/kubevirt/must-gather --image=quay.io/openshift/origin-must-gather

# Gather information using a specific image stream plug-in
oc adm must-gather --image-stream=openshift/must-gather:latest

# Gather information using a specific image, command, and pod directory
oc adm must-gather --image=my/image:tag --source-dir=/pod/directory -- myspecial-command.sh
```

## Options

- `--all-images=false`
  Collect must-gather using the default image for all Operators on the cluster annotated with operators.openshift.io/must-gather-image

- `--dest-dir=''`
  Set a specific directory on the local machine to write gathered data to.

- `--host-network=false`
  Run must-gather pods as hostNetwork: true - relevant if a specific command and image needs to capture host-level data

- `--image=[]`
  Specify a must-gather plugin image to run. If not specified, OpenShift's default must-gather image will be used.

- `--image-stream=[]`
  Specify an image stream (namespace/name:tag) containing a must-gather plugin image to run.

- `--node-name=''`
  Set a specific node to use - by default a random master will be used

- `--node-selector=''`
  Set a specific node selector to use - only relevant when specifying a command and image which needs to capture data on a set of cluster nodes simultaneously

- `--run-namespace=''`
  An existing privileged namespace where must-gather pods should run. If not specified a temporary namespace will be generated.

- `--since=0s`
  Only return logs newer than a relative duration like 5s, 2m, or 3h. Defaults to all logs. Plugins are encouraged but not required to support this. Only one of since-time / since may be used.

- `--since-time=''`
  Only return logs after a specific date (RFC3339). Defaults to all logs. Plugins are encouraged but not required to support this. Only one of since-time / since may be used. This may not be applied to all commands in must-gather image (e.g. not every command complies with RFC3339, the use might be limited, etc.).

- `--source-dir='/must-gather/'`
  Set the specific directory on the pod copy the gathered data from.

- `--timeout='10m'`
  The length of time to wait for data gathering to complete, like 5s, 2m, or 3h, higher than zero. Defaults to 10 minutes. NOTE: This timeout only applies to the data gathering phase. After gathering completes, copying to the local destination will continue until finished.

- `--volume-percentage=70`
  Specify maximum percentage of must-gather pod's allocated volume that can be used. If this limit is exceeded, must-gather will stop gathering, but still copy gathered data.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm must-gather --help` / `gen-oc-help.py` で生成</sub>
