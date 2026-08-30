# `oc image extract`

> Copy files from an image to the file system

[`oc`](../oc.md) / [`oc image`](../image.md) / `extract`

## Usage

```
oc image extract [flags] [options]
```

Extract the contents of an image to disk.

Download an image or parts of an image to the file system. Allows users to access the contents of images without requiring a container runtime engine running.

Unless the --path flag is passed, image contents will be extracted into the current directory.

Pass images to extract as arguments. The --path flag allows you to define multiple source to destination directory mappings. The source section may be either a file, a directory (ends with a '/'), or a file pattern within a directory. The destination section	is a directory to extract to. Both source and destination must be specified.

If the specified image supports multiple operating systems, the image that matches the current operating system will be chosen. Otherwise you must pass --filter-by-os to select the desired image.

You may further qualify the image by adding a layer selector to the end of the image string to only extract specific layers within an image. The supported selectors are:

[`<index>` ] - select the layer at the provided index (zero-indexed) [`<from_index>` ,`<to_index>` ] - select layers by index, exclusive [~`<prefix>` ] - select the layer with the matching digest prefix or return an error

Negative indices are counted from the end of the list, e.g. [-1] selects the last layer.

## Examples

```bash
# Extract the busybox image into the current directory
oc image extract docker.io/library/busybox:latest

# Extract the busybox image into a designated directory (must exist)
oc image extract docker.io/library/busybox:latest --path /:/tmp/busybox

# Extract the busybox image into the current directory for linux/s390x platform
# Note: Wildcard filter is not supported with extract; pass a single os/arch to extract
oc image extract docker.io/library/busybox:latest --filter-by-os=linux/s390x

# Extract a single file from the image into the current directory
oc image extract docker.io/library/centos:7 --path /bin/bash:.

# Extract all .repo files from the image's /etc/yum.repos.d/ folder into the current directory
oc image extract docker.io/library/centos:7 --path /etc/yum.repos.d/*.repo:.

# Extract all .repo files from the image's /etc/yum.repos.d/ folder into a designated directory (must exist)
# This results in /tmp/yum.repos.d/*.repo on local system
oc image extract docker.io/library/centos:7 --path /etc/yum.repos.d/*.repo:/tmp/yum.repos.d

# Extract an image stored on disk into the current directory ($(pwd)/v2/busybox/blobs,manifests exists)
# --confirm is required because the current directory is not empty
oc image extract file://busybox:local --confirm

# Extract an image stored on disk in a directory other than $(pwd)/v2 into the current directory
# --confirm is required because the current directory is not empty ($(pwd)/busybox-mirror-dir/v2/busybox exists)
oc image extract file://busybox:local --dir busybox-mirror-dir --confirm

# Extract an image stored on disk in a directory other than $(pwd)/v2 into a designated directory (must exist)
oc image extract file://busybox:local --dir busybox-mirror-dir --path /:/tmp/busybox

# Extract the last layer in the image
oc image extract docker.io/library/centos:7[-1]

# Extract the first three layers of the image
oc image extract docker.io/library/centos:7[:3]

# Extract the last three layers of the image
oc image extract docker.io/library/centos:7[-3:]
```

## Options

- `--all-layers=false`
  For dry-run mode, process from lowest to highest layer and don't omit duplicate files.

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--confirm=false`
  Pass to allow extracting to non-empty directories.

- `--dir=''`
  The directory on disk that file:// images will be extracted from.

- `--dry-run=false`
  Print the actions that would be taken and exit without writing any contents.

- `--file=[]`
  Extract the specified files to the current directory.

- `--filter-by-os=''`
  A regular expression to control which images are considered when multiple variants are available. Images will be passed as '`<platform>`/`<architecture>`[/`<variant>`]'.

- `--idms-file=''`
  Path to an ImageDigestMirrorSet file. If set, data from this file will be used to find alternative locations for images.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--only-files=false`
  Only extract regular files and directories from the image.

- `--path=[]`
  Extract only part of an image, or, designate the directory on disk to extract image contents into. Must be SRC:DST where SRC is the path within the image and DST a local directory. If not specified the default is to extract everything to the current directory.

- `-p, --preserve-ownership=false`
  Preserve the permissions of extracted files.

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc image extract --help` / `gen-oc-help.py` で生成</sub>
