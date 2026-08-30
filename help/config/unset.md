# `oc config unset`

> Unset an individual value in a kubeconfig file

[`oc`](../oc.md) / [`oc config`](../config.md) / `unset`

## Usage

```
oc config unset PROPERTY_NAME [options]
```

PROPERTY_NAME is a dot delimited name where each token represents either an attribute name or a map key.  Map keys may not contain dots.

## Examples

```bash
# Unset the current-context
oc config unset current-context

# Unset namespace in foo context
oc config unset contexts.foo.namespace
```

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config unset --help` / `gen-oc-help.py` で生成</sub>
