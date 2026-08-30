# `oc adm release new`

> Create a new OpenShift release

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm release`](../release.md) / `new`

## Usage

```
oc adm release new [SRC=DST ...] [flags] [options]
```

Build a new OpenShift release image that will update a cluster.

OpenShift uses long-running active management processes called "operators" to keep the cluster running and manage component lifecycle. This command composes a set of images with operator definitions into a single update payload that can be used to install or update a cluster.

Operators are expected to host the config they need to be installed to a cluster in the '/manifests' directory in their image. This command iterates over a set of operator images and extracts those manifests into a single, ordered list of Kubernetes objects that can then be iteratively updated on a cluster by the cluster version operator when it is time to perform an update. Manifest files are renamed to '0000 70`<image_name>`_`<filename>` ' by default, and an operator author that needs to provide a global-ordered file (before or after other operators) should prepend '0000 NN`<component>`_' to their file name, which instructs the release builder to not assign a component prefix. Only images in the input that have the image label 'io.openshift.release.operator=true' will have manifests loaded.

If an image is in the input but is not referenced by an operator's image-references file, the image will not be included in the final release image unless --include=NAME is provided.

Mappings specified via SRC=DST positional arguments allows overriding particular operators with a specific image.  For example:

cluster-version-operator=registry.example.com/openshift/cluster-version-operator:test-123

will override the default cluster-version-operator image with one pulled from registry.example.com.

## Examples

```bash
# Create a release from the latest origin images and push to a DockerHub repository
oc adm release new --from-image-stream=4.11 -n origin --to-image docker.io/mycompany/myrepo:latest

# Create a new release with updated metadata from a previous release
oc adm release new --from-release registry.ci.openshift.org/origin/release:v4.11 --name 4.11.1 \
--previous 4.11.0 --metadata ... --to-image docker.io/mycompany/myrepo:latest

# Create a new release and override a single image
oc adm release new --from-release registry.ci.openshift.org/origin/release:v4.11 \
cli=docker.io/mycompany/cli:latest --to-image docker.io/mycompany/myrepo:latest

# Run a verification pass to ensure the release can be reproduced
oc adm release new --from-release registry.ci.openshift.org/origin/release:v4.11
```

## Options

- `--allow-missing-images=false`
  Ignore errors when an operator references a release image that is not included.

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--component-versions=''`
  Supply additional version strings to the release in key=value[,key=value] form.

- `--component-versions-display-names=''`
  Supply additional version display names to the release in key=value[,key=value] form.

- `--dir=''`
  Directory to write release contents to, will default to a temporary directory.

- `--dry-run=false`
  Skips changes to external registries via mirroring or pushing images.

- `--exclude=[]`
  A list of image names or tags to exclude. It is applied after all inputs. Comma separated or individual arguments.

- `--from-dir=''`
  Use this directory as the source for the release payload.

- `--from-image-stream=''`
  Look at all tags in the provided image stream and build a release payload from them.

- `-f, --from-image-stream-file=''`
  Take the provided image stream on disk and build a release payload from it.

- `--from-release=''`
  Use an existing release image as input.

- `--include=[]`
  A list of image tags that should not be pruned. Excluding a tag takes precedence. Comma separated or individual arguments.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--keep-manifest-list=false`
  If an image is part of a manifest list, always mirror the list even if only one image is found.

- `--mapping-file=[]`
  A file defining a mapping of input images to use to build the release

- `--max-per-registry=4`
  Number of concurrent requests allowed per registry.

- `--metadata=''`
  A JSON object to attach as the metadata for the release manifest.

- `--mirror=''`
  Mirror the contents of the release to this repository.

- `--name=''`
  The name of the release. Will default to the current time.

- `--next=[]`
  A list of semantic versions that should succeed this version in the release manifest. Using --next can potentially cause regressions given the release does not exist. Use with caution

- `-o, --output=''`
  Output the mapping definition in this format.

- `--previous=[]`
  A list of semantic versions that should precede this version in the release manifest.

- `--reference-mode=''`
  By default, the image reference from an image stream points to the public registry for the stream and the image digest. Pass 'source' to build references to the originating image.

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--release-manifest=false`
  If true, a release manifest will be created using --name as the semantic version.

- `--skip-manifest-check=false`
  Ignore errors when an operator includes a yaml/yml/json file that is not parseable.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

- `--to-dir=''`
  Output the release manifests to a directory instead of creating an image.

- `--to-file=''`
  Output the release to a tar file instead of creating an image.

- `--to-image=''`
  The location to upload the release image to.

- `--to-image-base=''`
  If specified, the image to add the release layer on top of.

- `--to-image-base-tag='cluster-version-operator'`
  If specified, the image tag in the input to add the release layer on top of. Defaults to cluster-version-operator.

- `--to-signature=''`
  If specified, output a message that can be signed that describes this release. Requires --to-image.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm release new --help` / `gen-oc-help.py` で生成</sub>
