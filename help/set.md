# `oc set`

> Commands that help set specific features on objects

[`oc`](oc.md) / `set`

## Usage

```
oc set COMMAND [flags] [options]
```

Configure application resources

These commands help you make changes to existing application resources.

## Subcommands

- [`build-hook`](set/build-hook.md) — Update a build hook on a build config
- [`build-secret`](set/build-secret.md) — Update a build secret on a build config
- [`data`](set/data.md) — Update the data within a config map or secret
- [`deployment-hook`](set/deployment-hook.md) — Update a deployment hook on a deployment config
- [`env`](set/env.md) — Update environment variables on a pod template
- [`image`](set/image.md) — Update the image of a pod template
- [`image-lookup`](set/image-lookup.md) — Change how images are resolved when deploying applications
- [`probe`](set/probe.md) — Update a probe on a pod template
- [`resources`](set/resources.md) — Update resource requests/limits on objects with pod templates
- [`route-backends`](set/route-backends.md) — Update the backends for a route
- [`selector`](set/selector.md) — Set the selector on a resource
- [`serviceaccount`](set/serviceaccount.md) — Update the service account of a resource
- [`subject`](set/subject.md) — Update the user, group, or service account in a role binding or cluster role binding
- [`triggers`](set/triggers.md) — Update the triggers on one or more objects
- [`volumes`](set/volumes.md) — Update volumes on a pod template

> Use "oc set `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc set --help` / `gen-oc-help.py` で生成</sub>
