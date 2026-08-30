# `oc image append`

> Add layers to images and push them to a registry

[`oc`](../oc.md) / [`oc image`](../image.md) / `append`

## Usage

```
oc image append [flags] [options]
```

Add layers to container images.

Modifies an existing image by adding layers or changing configuration and then pushes that image to a remote registry. Any inherited layers are streamed from registry to registry without being stored locally. The default docker credentials are used for authenticating to the registries.

Layers may be provided as arguments to the command and must each be a gzipped tar archive representing a filesystem overlay to the inherited images. The archive may contain a "whiteout" file (the prefix '.wh.' and the filename) which will hide files in the lower layers. All supported filesystem attributes present in the archive will be used as is.

Metadata about the image (the configuration passed to the container runtime) may be altered by passing a JSON string to the --image or --meta options. The --image flag changes what the container runtime sees, while the --meta option allows you to change the attributes of the image used by the runtime. Use --dry-run to see the result of your changes. You may add the --drop-history flag to remove information from the image about the system that built the base image.

Images in manifest list format with keep-manifest-list specified will automatically append layers to all sub manifests in the list unless filter-by-os is specified in which case the append will only happen for the filtered manifests while preserving the manifestlist. If keep-manifest-list is not specified, automatically select an image that matches the current operating system and architecture unless --filter-by-os is used to select a different image. These flags have no effect on regular images.

## Examples

```bash
# Remove the entrypoint on the mysql:latest image
oc image append --from mysql:latest --to myregistry.com/myimage:latest --image '{"Entrypoint":null}'

# Add a new layer to the image
oc image append --from mysql:latest --to myregistry.com/myimage:latest layer.tar.gz

# Add a new layer to the image and store the result on disk
# This results in $(pwd)/v2/mysql/blobs,manifests
oc image append --from mysql:latest --to file://mysql:local layer.tar.gz

# Add a new layer to the image and store the result on disk in a designated directory
# This will result in $(pwd)/mysql-local/v2/mysql/blobs,manifests
oc image append --from mysql:latest --to file://mysql:local --dir mysql-local layer.tar.gz

# Add a new layer to an image that is stored on disk (~/mysql-local/v2/image exists)
oc image append --from-dir ~/mysql-local --to myregistry.com/myimage:latest layer.tar.gz

# Add a new layer to an image that was mirrored to the current directory on disk ($(pwd)/v2/image exists)
oc image append --from-dir v2 --to myregistry.com/myimage:latest layer.tar.gz

# Add a new layer to a multi-architecture image for an os/arch that is different from the system's os/arch
# Note: The first image in the manifest list that matches the filter will be returned when --keep-manifest-list is not specified
oc image append --from docker.io/library/busybox:latest --filter-by-os=linux/s390x --to myregistry.com/myimage:latest layer.tar.gz

# Add a new layer to a multi-architecture image for all the os/arch manifests when keep-manifest-list is specified
oc image append --from docker.io/library/busybox:latest --keep-manifest-list --to myregistry.com/myimage:latest layer.tar.gz

# Add a new layer to a multi-architecture image for all the os/arch manifests that is specified by the filter, while preserving the manifestlist
oc image append --from docker.io/library/busybox:latest --filter-by-os=linux/s390x --keep-manifest-list --to myregistry.com/myimage:latest layer.tar.gz
```

## Options

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--created-at=''`
  The creation date for this image, in RFC3339 format or milliseconds from the Unix epoch.

- `--dir=''`
  The directory on disk that file:// images will be copied under.

- `--drop-history=false`
  Fields on the image that relate to the history of how the image was created will be removed.

- `--dry-run=false`
  Print the actions that would be taken and exit without writing to the destination.

- `--filter-by-os=''`
  A regular expression to control which images are considered when multiple variants are available. Images will be passed as '`<platform>`/`<architecture>`[/`<variant>`]'.

- `--force=false`
  If set, the command will attempt to upload all layers instead of skipping those that are already uploaded.

- `--from=''`
  The image to use as a base. If empty, a new scratch image is created.

- `--from-dir=''`
  The directory on disk that file:// images will be read from. Overrides --dir

- `--image=''`
  A JSON patch that will be used with the output image data.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--keep-manifest-list=false`
  If an image is part of a manifest list, always append to each image in the list. The default is to append to all images unless --filter-by-os is passed.

- `--max-per-registry=4`
  Number of concurrent requests allowed per registry.

- `--meta=''`
  A JSON patch that will be used with image base metadata (advanced config).

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

- `--to=''`
  The Docker repository tag to upload the appended image to.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc image append --help` / `gen-oc-help.py` で生成</sub>
