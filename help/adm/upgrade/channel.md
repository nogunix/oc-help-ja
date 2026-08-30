# `oc adm upgrade channel`

> Set or clear the update channel

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm upgrade`](../upgrade.md) / `channel`

## Usage

```
oc adm upgrade channel CHANNEL [flags] [options]
```

This command will set or clear the update channel, which impacts the list of updates recommended for the cluster.

If desired channel is empty, the command will clear the update channel. If there is a list of acceptable channels and the current update channel is in that list, you must pass --allow-explicit-channel to allow channel clear to proceed.

If desired channel is not empty, the command will set the update channel to it. If there is a list of acceptable channels and the desired channel is not in that list, you must pass --allow-explicit-channel to allow channel change to proceed.

## Options

- `--allow-explicit-channel=false`
  Change the channel, even if there is a list of acceptable channels and the desired channel is not in that list.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm upgrade channel --help` / `gen-oc-help.py` で生成</sub>
