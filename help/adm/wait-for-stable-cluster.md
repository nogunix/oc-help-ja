# `oc adm wait-for-stable-cluster`

> Wait for the platform operators to become stable

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `wait-for-stable-cluster`

## Usage

```
oc adm wait-for-stable-cluster [flags] [options]
```

Wait for all OCP v4 clusteroperators to report Available=true, Progressing=false, Degraded=false.

## Examples

```bash
# Wait for all cluster operators to become stable
oc adm wait-for-stable-cluster

# Consider operators to be stable if they report as such for 5 minutes straight
oc adm wait-for-stable-cluster --minimum-stable-period 5m
```

## Options

- `--minimum-stable-period=5m0s`
  minimum duration to consider a cluster stable. Defaults to 5 minutes.

- `--timeout=1h0m0s`
  duration before the command times out. Defaults to 1 hour.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm wait-for-stable-cluster --help` / `gen-oc-help.py` で生成</sub>
