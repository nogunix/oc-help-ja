# `oc adm top`

> Show usage statistics of resources on the server

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `top`

## Usage

```
oc adm top [flags] [options]
```

This command analyzes resources managed by the platform and presents current usage statistics.

## Subcommands

- [`images`](top/images.md) — Show usage statistics for images
- [`imagestreams`](top/imagestreams.md) — Show usage statistics for image streams
- [`node`](top/node.md) — Display resource (CPU/memory) usage of nodes
- [`persistentvolumeclaims`](top/persistentvolumeclaims.md) — Experimental: Show usage statistics for bound persistentvolumeclaims
- [`pod`](top/pod.md) — Display resource (CPU/memory) usage of pods

> Use "oc adm top `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm top --help` / `gen-oc-help.py` で生成</sub>
