# `oc create build`

> Create a new build

[`oc`](../oc.md) / [`oc create`](../create.md) / `build`

## Usage

```
oc create build NAME [flags] [options]
```

Builds create container images from source code or Dockerfiles. A build can pull source code from Git or accept a Dockerfile that pulls the source content.

## Examples

```bash
# Create a new build
oc create build myapp
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `--build-loglevel=0`
  Set the log level for builds (0-10, 0 default).

- `--context-dir=''`
  A relative path within the repository to use as the root of the build.

- `--dockerfile-contents=''`
  The contents of a Dockerfile to build.

- `--dockerfile-path=''`
  The relative path within the repository context that the Dockerfile is located at.

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `--env=[]`
  Add enviroment variables to the build strategy.

- `--from-image=''`
  A container image pull spec to use as the basis for the image build.

- `--image-optimization-policy=''`
  Controls whether individual layers are created: SkipLayers, SkipLayersAndWarn, or None.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `--save-config=false`
  If true, the configuration of current object will be saved in its annotation. Otherwise, the annotation will be unchanged. This flag is useful when you want to perform kubectl apply on this object in the future.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--source-git=''`
  A URL or Git spec link to a Git repository.

- `--source-revision=''`
  A commit, branch, or tag within the source repository.

- `--strategy=''`
  The build strategy to use: Docker, Source, or Custom. Can be defaulted by other arguments.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

- `--to-image=''`
  A location to push the output image to.

- `--to-image-stream=''`
  An image stream tag to push the output image to. Accepts [NAMESPACE/]STREAM:TAG

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create build --help` / `gen-oc-help.py` で生成</sub>
