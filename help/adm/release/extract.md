# `oc adm release extract`

> Extract the contents of an update payload to disk

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm release`](../release.md) / `extract`

## Usage

```
oc adm release extract [flags] [options]
```

Extract the contents of a release image to disk.

Extracts the contents of an OpenShift release image to disk for inspection or debugging. Update images contain manifests and metadata about the operators that must be installed on the cluster for a given version.

The --tools and --command flags allow you to extract the appropriate client binaries for your operating system to disk. --tools will create archive files containing the current OS tools (or, if --command-os is set to '*', all OS versions). Specifying --command for either 'oc' or 'openshift-install' will extract the binaries directly. You may pass a PGP private key file with --signing-key which will create an ASCII armored sha256sum.txt.asc file describing the content that was extracted that is signed by the key. For more advanced signing, use the generated sha256sum.txt and an external tool like gpg.

The --credentials-requests flag filters extracted manifests to only cloud credential requests. The --cloud flag further filters credential requests to a specific cloud. Valid values for --cloud include alibabacloud, aws, azure, gcp, ibmcloud, nutanix, openstack, ovirt, powervs, and vsphere.

The --included flag filters extracted manifests to those that are expected to be included with the cluster.  Filters are cumulative, so '--credentials-requests --included' will only include cloud credential requests which are expected to be included with the cluster. If --install-config is set, it will be used to determine the expected cluster configuration, otherwise the command will interrogate your current cluster to determine its configuration. This command is most accurate when the version of the extracting client matches the version of the cluster under consideration.

Instead of extracting the manifests, you can specify --git=DIR to perform a Git checkout of the source code that comprises the release. A warning will be printed if the component is not associated with source code. The command will not perform any destructive actions on your behalf except for executing a 'git checkout' which may change the current branch. Requires 'git' to be on your path.

If the specified image supports multiple operating systems, the image that matches the current operating system will be chosen. Otherwise you must pass --filter-by-os to select the desired image.

## Examples

```bash
# Use git to check out the source code for the current cluster release to DIR
oc adm release extract --git=DIR

# Extract cloud credential requests for AWS
oc adm release extract --credentials-requests --cloud=aws

# Use git to check out the source code for the current cluster release to DIR from linux/s390x image
# Note: Wildcard filter is not supported; pass a single os/arch to extract
oc adm release extract --git=DIR quay.io/openshift-release-dev/ocp-release:4.11.2 --filter-by-os=linux/s390x
```

## Options

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--cloud=''`
  Exclude credential requests which are not relevant to the given cloud provider.  Works only in combination with --credentials-requests.

- `--command=''`
  Specify 'oc' or 'openshift-install' to extract the client for your operating system.

- `--command-os=''`
  Override which operating system command is extracted (mac, windows, linux) or can be specified with arch(linux/arm64, mac/amd64). You map specify '*' to extract all tool archives.

- `--credentials-requests=false`
  Exclude manifests which are not credential requests.

- `--dir=''`
  The directory on disk that file:// images will be copied under.

- `--file=''`
  Extract a single file from the payload to standard output.

- `--filter-by-os=''`
  A regular expression to control which images are considered when multiple variants are available. Images will be passed as '`<platform>`/`<architecture>`[/`<variant>`]'.

- `--from=''`
  Image containing the release payload.

- `--git=''`
  Check out the sources that created this release into the provided dir. Repos will be created at `<dir>`/`<host>`/`<path>`. Requires 'git' on your path.

- `--idms-file=''`
  Path to an ImageDigestMirrorSet file. If set, data from this file will be used to find alternative locations for images.

- `--included=false`
  Exclude manifests that are not expected to be included in the cluster.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--install-config=''`
  Path to an install-config file, as consumed by the openshift-install command.  Works only in combination with --included.

- `--max-per-registry=0`
  Number of concurrent requests allowed per registry.

- `-o, --output=''`
  Output format. Supports 'commit' when used with '--git'.

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--signing-key=''`
  Sign the sha256sum.txt generated by --tools with this GPG key. A sha256sum.txt.asc file signed by this key will be created. The key is assumed to be encrypted.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

- `--to='.'`
  Directory to write release contents to, defaults to the current directory.

- `--tools=false`
  Extract the tools archives from the release image. Implies --command=*

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm release extract --help` / `gen-oc-help.py` で生成</sub>
