# `oc config get-contexts`

> Describe one or many contexts

[`oc`](../oc.md) / [`oc config`](../config.md) / `get-contexts`

## Usage

```
oc config get-contexts [(-o|--output=)name)] [options]
```

Display one or many contexts from the kubeconfig file.

## Examples

```bash
# List all the contexts in your kubeconfig file
oc config get-contexts

# Describe one context in your kubeconfig file
oc config get-contexts my-context
```

## Options

- `--no-headers=false`
  When using the default or custom-column output format, don't print headers (default print headers).

- `-o, --output=''`
  Output format. One of: (name).

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config get-contexts --help` / `gen-oc-help.py` で生成</sub>
