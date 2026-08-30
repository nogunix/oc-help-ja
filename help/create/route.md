# `oc create route`

> Expose containers externally via secured routes

[`oc`](../oc.md) / [`oc create`](../create.md) / `route`

## Usage

```
oc create route [flags] [options]
```

Three types of secured routes are supported: edge, passthrough, and reencrypt. If you want to create unsecured routes, see "oc expose -h".

## Subcommands

- [`edge`](route/edge.md) — Create a route that uses edge TLS termination
- [`passthrough`](route/passthrough.md) — Create a route that uses passthrough TLS termination
- [`reencrypt`](route/reencrypt.md) — Create a route that uses reencrypt TLS termination

> Use "oc create route `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc create route --help` / `gen-oc-help.py` で生成</sub>
