# `oc adm release info`

> Display information about a release

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm release`](../release.md) / `info`

## Usage

```
oc adm release info IMAGE [--changes-from=IMAGE] [--verify|--commits|--pullspecs] [flags] [options]
```

Show information about an OpenShift release.

This command retrieves, verifies, and formats the information describing an OpenShift update. Updates are delivered as container images with metadata describing the component images and the configuration necessary to install the system operators. A release image is usually referenced via its content digest, which allows this command and the update infrastructure to validate that updates have not been tampered with.

If no arguments are specified the release of the currently connected cluster is displayed. Specify one or more images via pull spec to see details of each release image. You may also pass a semantic version (4.11.2) as an argument, and if cluster version object has seen such a version in the upgrades channel it will find the release info for that version.

The --commits flag will display the Git commit IDs and repository URLs for the source of each component image. The --pullspecs flag will display the full component image pull spec. --size will show a breakdown of each image, their layers, and the total size of the payload. --contents shows the configuration that will be applied to the cluster when the update is run. If you have specified two images the difference between the first and second image will be shown. You may use -o name, -o digest, or -o pullspec to output the tag name, digest for image, or pullspec of the images referenced in the release image.

The --verify flag will display one summary line per input release image and verify the integrity of each. The command will return an error if the release has been tampered with. Passing a pull spec with a digest (e.g. quay.io/openshift/release@sha256:a9bc...) instead of a tag when verifying an image is recommended since it ensures an attacker cannot trick you into installing an older, potentially vulnerable version.

The --bugs and --changelog flags will use git to clone the git history of the release and display the code changes that occurred between the two release arguments. This operation is slow and requires sufficient disk space on the selected drive to clone all repositories.

Additionally, the --rpmdb-cache flag will cache rpmdb content for images in the release. Then, the --rpmdb flag will display the RPM contents of an image. The --rpmdb-diff flag will display RPM changes that occurred between the two release arguments. For images optimized for this operation (e.g. recent enough machine-os images), this is quite fast and efficient. Otherwise, it is a slow operation that requires sufficient disk space. By default, the image containing the machine-os component is targeted for RPM queries. Other images can be targeted with --rpmdb-image.

If the specified image supports multiple operating systems, the image that matches the current operating system will be chosen. Otherwise you must pass --filter-by-os to select the desired image.

## Examples

```bash
# Show information about the cluster's current release
oc adm release info

# Show the source code that comprises a release
oc adm release info 4.11.2 --commit-urls

# Show the source code difference between two releases
oc adm release info 4.11.0 4.11.2 --commits

# Show where the images referenced by the release are located
oc adm release info quay.io/openshift-release-dev/ocp-release:4.11.2 --pullspecs

# Show information about linux/s390x image
# Note: Wildcard filter is not supported; pass a single os/arch to extract
oc adm release info quay.io/openshift-release-dev/ocp-release:4.11.2 --filter-by-os=linux/s390x
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--bugs=''`
  Generate bug listings from the changelogs in the git repositories extracted to this path.

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. If --insecure is used, this flag will be ignored.

- `--changelog=''`
  Generate changelog output from the git directories extracted to this path.

- `--changes-from=''`
  Show changes from this image to the requested image.

- `--commit-urls=false`
  Display a link (if possible) to the source code.

- `--commits=false`
  Display information about the source an image was created with.

- `--contents=false`
  Display the contents of a release.

- `--dir=''`
  The directory on disk that file:// images will be copied under.

- `--filter-by-os=''`
  A regular expression to control which images are considered when multiple variants are available. Images will be passed as '`<platform>`/`<architecture>`[/`<variant>`]'.

- `--idms-file=''`
  Path to an ImageDigestMirrorSet file. If set, data from this file will be used to find alternative locations for images.

- `--image-for=''`
  Print the pull spec of the specified image or an error if it does not exist.

- `--include-images=false`
  When displaying JSON output of a release output the images the release references.

- `--insecure=false`
  Allow push and pull operations to registries to be made over HTTP

- `--max-per-registry=4`
  Number of concurrent requests allowed per registry.

- `-o, --output=''`
  Display the release info in an alternative format: digest|json|name|pullspec|template|jsonpath.

- `--pullspecs=false`
  Display the pull spec of each image instead of the digest.

- `-a, --registry-config=''`
  Path to your registry credentials. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json, /run/containers/${UID}/auth.json, ${XDG_CONFIG_HOME}/containers/auth.json, ${DOCKER_CONFIG}, ~/.docker/config.json, ~/.dockercfg. The order can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--rpmdb=false`
  List RPM packages in image.

- `--rpmdb-cache=''`
  Cache rpmdb content in this directory.

- `--rpmdb-diff=false`
  Generate RPM package diff.

- `--rpmdb-image=''`
  The image to use for RPM queries.

- `--size=false`
  Display the size of each image including overlap.

- `--skip-bug-check=false`
  Do not check bug statuses when running generating bug listing with --output=name

- `--skip-verification=false`
  Skip verifying the integrity of the retrieved content. This is not recommended, but may be necessary when importing images from older image registries. Only bypass verification if the registry is known to be trustworthy.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--verify=false`
  Generate bug listings from the changelogs in the git repositories extracted to this path.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm release info --help` / `gen-oc-help.py` で生成</sub>
