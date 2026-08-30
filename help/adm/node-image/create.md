# `oc adm node-image create`

> Create an ISO image for booting the nodes to be added to the target cluster

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm node-image`](../node-image.md) / `create`

## Usage

```
oc adm node-image create [flags] [options]
```

Create an ISO image from an initial configuration for a given set of nodes, to add them to an existing on-prem cluster.

This command creates a pod in a temporary namespace on the target cluster to retrieve the required information for creating a customized ISO image. The downloaded ISO image could then be used to boot a previously selected set of nodes, and add them to the target cluster in a fully automated way.

The command also requires a connection to the target cluster, and a valid registry credentials to retrieve the required information from the target cluster release.

A nodes-config.yaml config file must be created to provide the required initial configuration for the selected nodes. Alternatively, to support simpler configurations for adding just a single node, it's also possible to use a set of flags to configure the host. In such case the '--mac-address' is the only mandatory flag - while all the others will be optional (note: any eventual configuration file present will be ignored).

In case of a command failure a report.json file is automatically created with the error details, and additional troubleshooting information.

## Examples

```bash
# Create the ISO image and download it in the current folder
oc adm node-image create

# Use a different assets folder
oc adm node-image create --dir=/tmp/assets

# Specify a custom image name
oc adm node-image create -o=my-node.iso

# In place of an ISO, creates files that can be used for PXE boot
oc adm node-image create --pxe

# Create an ISO to add a single node without using the configuration file
oc adm node-image create --mac-address=00:d8:e7:c7:4b:bb

# Create an ISO to add a single node with a root device hint and without
# using the configuration file
oc adm node-image create --mac-address=00:d8:e7:c7:4b:bb --root-device-hint=deviceName:/dev/sda
```

## Options

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `-c, --cpu-architecture=''`
  Single node flag. The CPU architecture to be used to install the node. Valid only when `mac-address` is defined.

- `--dir=''`
  The path containing the configuration file, used also to store the generated artifacts.

- `--hostname=''`
  Single node flag. The hostname to be set for the node. Valid only when `mac-address` is defined.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `-m, --mac-address=''`
  Single node flag. MAC address used to identify the host to apply the configuration. If specified, the nodes-config.yaml config file will not be used.

- `--network-config-path=''`
  Single node flag. YAML file containing the NMState configuration to be applied for the node. Valid only when `mac-address` is defined.

- `-o, --output-name=''`
  The name of the output image.

- `-p, --pxe=false`
  Instead of an ISO, create files that can be used for PXE boot

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `-r, --report=false`
  When set, the report.json is always generated in the asset folder

- `--root-device-hint=''`
  Single node flag. Hint for specifying the storage location for the image root filesystem. Format accepted is `<hint name>`:`<value>`.. Valid only when `mac-address` is defined.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

- `-k, --ssh-key-path=''`
  Single node flag. Path to the SSH key used to access the node. Valid only when `mac-address` is defined.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm node-image create --help` / `gen-oc-help.py` で生成</sub>
