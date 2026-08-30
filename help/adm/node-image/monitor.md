# `oc adm node-image monitor`

> Monitor new nodes being added to an OpenShift cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm node-image`](../node-image.md) / `monitor`

## Usage

```
oc adm node-image monitor [flags] [options]
```

Monitor nodes being added to a cluster using an image generated from the "oc adm node-image create" command.

After the node image ISO has been booted on the host, the monitor command reports any pre-flight validations that may have failed impeding the host from being added to the cluster. If validations are successful, the node installation starts.

Before a node joins the cluster and becomes fully functional, two certificate signing requests (CSRs) need to be approved. The monitor command will display CSRs pending your approval.

The command ends when the nodes have successfully joined the cluster.

The command creates a pod in a temporary namespace on the target cluster to monitor the nodes.

The command also requires a connection to the target cluster, and a valid registry credentials to retrieve the required information from the target cluster release.

## Examples

```bash
# Monitor a single node being added to a cluster
oc adm node-image monitor --ip-addresses 192.168.111.83

# Monitor multiple nodes being added to a cluster by separating each
# IP address with a comma
oc adm node-image monitor --ip-addresses 192.168.111.83,192.168.111.84
```

## Options

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--ip-addresses=''`
  IP addresses of nodes to monitor.

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm node-image monitor --help` / `gen-oc-help.py` で生成</sub>
