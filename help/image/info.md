# `oc image info`

> Display information about an image

[`oc`](../oc.md) / [`oc image`](../image.md) / `info`

## Usage

```
oc image info IMAGE [...] [flags] [options]
```

Show information about an image in a remote image registry.

This command will retrieve metadata about container images in a remote image registry. You may specify images by tag or digest and specify multiple at a time.

Images in manifest list format will be shown for your current operating system. To see the image for a particular OS use the --filter-by-os=OS/ARCH flag. When --filter-by-os is used against an image which is not in manifest list format, --filter-by-os flag will be ignored.

## Examples

```bash
# Show information about an image
oc image info quay.io/openshift/cli:latest

# Show information about images matching a wildcard
oc image info quay.io/openshift/cli:4.*

# Show information about a file mirrored to disk under DIR
oc image info --dir=DIR file://library/busybox:latest

# Select which image from a multi-OS image to show
oc image info library/busybox:latest --filter-by-os=linux/arm64
```

## Options

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--dir=''`
  The directory on disk that file:// images will be read from.

- `--filter-by-os=''`
  A regular expression to control which images are considered when multiple variants are available. Images will be passed as '`<platform>`/`<architecture>`[/`<variant>`]'.

- `--icsp-file=''`
  Path to an ImageContentSourcePolicy file.  If set, data from this file will be used to find alternative locations for images.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `-o, --output=''`
  Print the image in an alternative format: json

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--show-multiarch=false`
  Show information even if the image is multiarch image. If not set, error is thrown for multiarch images.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc image info --help` / `gen-oc-help.py` で生成</sub>
