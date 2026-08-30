# `oc adm build-chain`

> Output the inputs and dependencies of your builds

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `build-chain`

## Usage

```
oc adm build-chain IMAGESTREAMTAG [flags] [options]
```

Supported formats for the generated graph are dot and a human-readable output. Tag and namespace are optional and if they are not specified, 'latest' and the default namespace will be used respectively.

## Examples

```bash
# Build the dependency tree for the 'latest' tag in <image-stream>
oc adm build-chain <image-stream>

# Build the dependency tree for the 'v2' tag in dot format and visualize it via the dot utility
oc adm build-chain <image-stream>:v2 -o dot | dot -T svg -o deps.svg

# Build the dependency tree across all namespaces for the specified image stream tag found in the 'test' namespace
oc adm build-chain <image-stream> -n test --all
```

## Options

- `--all=false`
  If true, build dependency tree for the specified image stream tag across all namespaces

- `-o, --output=''`
  Output format of dependency tree

- `--reverse=false`
  If true, show the istags dependencies instead of its dependants.

- `--trigger-only=true`
  If true, only include dependencies based on build triggers. If false, include all dependencies.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm build-chain --help` / `gen-oc-help.py` で生成</sub>
