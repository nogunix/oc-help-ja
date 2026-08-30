# `oc adm cordon`

> Mark node as unschedulable

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `cordon`

## Usage

```
oc adm cordon NODE [options]
```

## Examples

```bash
# Mark node "foo" as unschedulable
oc adm cordon foo
```

## Options

- `--dry-run='none'`
  Must be "none", "server", or "client". If client strategy, only print the object that would be sent, without sending it. If server strategy, submit server-side request without persisting the resource.

- `-l, --selector=''`
  Selector (label query) to filter on, supports '=', '==', '!=', 'in', 'notin'.(e.g. -l key1=value1,key2=value2,key3 in (value3)). Matching objects must satisfy all of the specified label constraints.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm cordon --help` / `gen-oc-help.py` で生成</sub>
