# `oc image mirror`

> Mirror images from one repository to another

[`oc`](../oc.md) / [`oc image`](../image.md) / `mirror`

## Usage

```
oc image mirror SRC DST [DST ...] [flags] [options]
```

Mirror images from one image repository to another.

Accepts a list of arguments defining source images that should be pushed to the provided destination image tag. The images are streamed from registry to registry without being stored locally. The default docker credentials are used for authenticating to the registries.

You may omit the tag argument on a source or use the '*' wildcard to select all or matching tags to mirror. The destination must be a repository in that case.

When using file mirroring, the --dir and --from-dir flags control the location on disk that content will be stored to. This directory mirrors the HTTP structure of a container registry and separates layers and data (blobs) from image metadata (manifests). If --from-dir is not specified, --dir or the current working directory is used.

When using S3 mirroring the region and bucket must be the first two segments after the host. Mirroring will create the necessary metadata so that images can be pulled via tag or digest, but listing manifests and tags will not be possible. You may also specify one or more --s3-source-bucket parameters (as`<bucket>` /`<path>` ) to designate buckets to look in to find blobs (instead of uploading). The source bucket also supports the suffix "/[store]", which will transform blob identifiers into the form the container image registry uses on disk, allowing you to mirror directly from an existing S3-backed container image registry. Credentials for S3 may be stored in your docker credential file and looked up by host, or loaded via the normal AWS client locations for ENV or file.

Images in manifest list format will be copied as-is unless you use --filter-by-os to restrict the allowed images to copy in a manifest list. This flag has no effect on regular images.

## Examples

```bash
# Copy image to another tag
oc image mirror myregistry.com/myimage:latest myregistry.com/myimage:stable

# Copy image to another registry
oc image mirror myregistry.com/myimage:latest docker.io/myrepository/myimage:stable

# Copy all tags starting with mysql to the destination repository
oc image mirror myregistry.com/myimage:mysql* docker.io/myrepository/myimage

# Copy image to disk, creating a directory structure that can be served as a registry
oc image mirror myregistry.com/myimage:latest file://myrepository/myimage:latest

# Copy image to S3 (pull from <bucket>.s3.amazonaws.com/image:latest)
oc image mirror myregistry.com/myimage:latest s3://s3.amazonaws.com/<region>/<bucket>/image:latest

# Copy image to S3 without setting a tag (pull via @<digest>)
oc image mirror myregistry.com/myimage:latest s3://s3.amazonaws.com/<region>/<bucket>/image

# Copy image to multiple locations
oc image mirror myregistry.com/myimage:latest docker.io/myrepository/myimage:stable \
docker.io/myrepository/myimage:dev

# Copy multiple images
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
myregistry.com/myimage:new=myregistry.com/other:target

# Copy manifest list of a multi-architecture image, even if only a single image is found
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--keep-manifest-list=true

# Copy specific os/arch manifest of a multi-architecture image
# Run 'oc image info myregistry.com/myimage:latest' to see available os/arch for multi-arch images
# Note that with multi-arch images, this results in a new manifest list digest that includes only the filtered manifests
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--filter-by-os=os/arch

# Copy all os/arch manifests of a multi-architecture image
# Run 'oc image info myregistry.com/myimage:latest' to see list of os/arch manifests that will be mirrored
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--keep-manifest-list=true

# Note the above command is equivalent to
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--filter-by-os=.*

# Copy specific os/arch manifest of a multi-architecture image
# Run 'oc image info myregistry.com/myimage:latest' to see available os/arch for multi-arch images
# Note that the target registry may reject a manifest list if the platform specific images do not all exist
# You must use a registry with sparse registry support enabled
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--filter-by-os=linux/386 \
--keep-manifest-list=true
```

## Options

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--continue-on-error=false`
  If an error occurs, keep going and attempt to mirror as much as possible.

- `--dir=''`
  The directory on disk that file:// images will be copied under.

- `--dry-run=false`
  Print the actions that would be taken and exit without writing to the destinations.

- `-f, --filename=[]`
  One or more files to read SRC=DST or SRC DST [DST ...] mappings from.

- `--filter-by-os=''`
  A regular expression to control which images are considered when multiple variants are available. Images will be passed as '`<platform>`/`<architecture>`[/`<variant>`]'.

- `--force=false`
  Attempt to write all layers and manifests even if they exist in the remote repository.

- `--from-dir=''`
  The directory on disk that file:// images will be read from. Overrides --dir

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--keep-manifest-list=false`
  Always mirror the manifest list. The default is to mirror the architecture specific image of the platform you are performing the mirror on unless --filter-by-os is passed.

- `--max-per-registry=6`
  Number of concurrent requests allowed per registry.

- `--max-registry=4`
  Number of concurrent registries to connect to at any one time.

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--s3-source-bucket=[]`
  A list of bucket/path locations on S3 that may contain already uploaded blobs. Add [store] to the end to use the container image registry path convention.

- `--skip-missing=false`
  If an input image is not found, skip them.

- `--skip-mount=false`
  Always push layers instead of cross-mounting them

- `--skip-multiple-scopes=false`
  Some registries do not support multiple scopes passed to the registry login.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc image mirror --help` / `gen-oc-help.py` で生成</sub>
