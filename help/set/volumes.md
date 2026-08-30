# `oc set volumes`

> Update volumes on a pod template

[`oc`](../oc.md) / [`oc set`](../set.md) / `volumes`

## Usage

```
oc set volumes RESOURCE/NAME --add|--remove [flags] [options]
```

This command can add, update or remove volumes from containers for any object that has a pod template (deployment configs, replication controllers, or pods). You can list volumes in pod or any object that has a pod template. You can specify a single object or multiple, and alter volumes on all containers or just those that match a given name.

If you alter a volume setting on a deployment config, a deployment will be triggered. Changing a replication controller will not affect running pods, and you cannot change a pod's volumes once it has been created.

Volume types include:

- emptydir (empty directory) default : A directory allocated when the pod is created on a local host, is removed when the pod is deleted and is not copied across servers
- hostdir (host directory): A directory with specific path on any host (requires elevated privileges)
- persistentvolumeclaim or pvc (persistent volume claim): Link the volume directory in the container to a persistent volume claim you have allocated by name - a persistent volume claim is a request to allocate storage. Note that if your claim hasn't been bound, your pods will not start.
- secret (mounted secret): Secret volumes mount a named secret to the provided directory.

For descriptions on other volume types, see https://docs.openshift.com

Aliases:
volumes, volume

## Examples

```bash
# List volumes defined on all deployment configs in the current project
oc set volume dc --all

# Add a new empty dir volume to deployment config (dc) 'myapp' mounted under
# /var/lib/myapp
oc set volume dc/myapp --add --mount-path=/var/lib/myapp

# Use an existing persistent volume claim (PVC) to overwrite an existing volume 'v1'
oc set volume dc/myapp --add --name=v1 -t pvc --claim-name=pvc1 --overwrite

# Remove volume 'v1' from deployment config 'myapp'
oc set volume dc/myapp --remove --name=v1

# Create a new persistent volume claim that overwrites an existing volume 'v1'
oc set volume dc/myapp --add --name=v1 -t pvc --claim-size=1G --overwrite

# Change the mount point for volume 'v1' to /data
oc set volume dc/myapp --add --name=v1 -m /data --overwrite

# Modify the deployment config by removing volume mount "v1" from container "c1"
# (and by removing the volume "v1" if no other containers have volume mounts that reference it)
oc set volume dc/myapp --remove --name=v1 --containers=c1

# Add new volume based on a more complex volume source (AWS EBS, GCE PD,
# Ceph, Gluster, NFS, ISCSI, ...)
oc set volume dc/myapp --add -m /data --source=<json-string>
```

## Options

- `--add=false`
  If true, add volume and/or volume mounts for containers

- `--all=false`
  If true, select all resources in the namespace of the specified resource types

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--claim-class=''`
  StorageClass to use for the persistent volume claim

- `--claim-mode='ReadWriteOnce'`
  Set the access mode of the claim to be created. Valid values are ReadWriteOnce (rwo), ReadWriteMany (rwm), or ReadOnlyMany (rom)

- `--claim-name=''`
  Persistent volume claim name. Must be provided for persistentVolumeClaim volume type

- `--claim-size=''`
  If specified along with a persistent volume type, create a new claim with the given size in bytes. Accepts SI notation: 10, 10G, 10Gi

- `--configmap-name=''`
  Name of the persisted config map. Must be provided for configmap volume type

- `--confirm=false`
  If true, confirm that you really want to remove multiple volumes

- `-c, --containers='*'`
  The names of containers in the selected pod templates to change - may use wildcards

- `--default-mode=''`
  The default mode bits to create files with. Can be between 0000 and 0777. Defaults to 0644.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--field-manager='kubectl-set'`
  Name of the manager used to track field ownership.

- `-f, --filename=[]`
  Filename, directory, or URL to files to use to edit the resource

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `--local=false`
  If true, set image will NOT contact api-server but run locally.

- `-m, --mount-path=''`
  Mount path inside the container. Optional param for --add or --remove

- `--name=''`
  Name of the volume. If empty, auto generated for add operation

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--overwrite=false`
  If true, replace existing volume source with the provided name and/or volume mount for the given resource

- `--path=''`
  Host path. Must be provided for hostPath volume type

- `--read-only=false`
  Mount volume as ReadOnly. Optional param for --add or --remove

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--remove=false`
  If true, remove volume and/or volume mounts for containers

- `--secret-name=''`
  Name of the persisted secret. Must be provided for secret volume type

- `-l, --selector=''`
  Selector (label query) to filter on

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--source=''`
  Details of volume source as json string. This can be used if the required volume type is not supported by --type option. (e.g.: '{"nfs": {"path": "/tmp","server":"172.17.0.2"}}')

- `--sub-path=''`
  Path within the local volume from which the container's volume should be mounted. Optional param for --add or --remove

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `-t, --type=''`
  Type of the volume source for add operation. Supported options: emptyDir, hostPath, secret, configmap, persistentVolumeClaim

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set volumes --help` / `gen-oc-help.py` で生成</sub>
