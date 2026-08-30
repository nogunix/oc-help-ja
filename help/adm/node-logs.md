# `oc adm node-logs`

> Display and filter node logs

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `node-logs`

## Usage

```
oc adm node-logs [-l LABELS] [NODE...] [options]
```

This command retrieves logs for the node. The default mode is to query the systemd journal on supported operating systems, which allows searching, time based filtering, and unit based filtering. You may also use the --path argument to see a list of log files available under /var/log/ and view those contents directly.

Node logs may contain sensitive output and so are limited to privileged node administrators. The system:node-admins role grants this permission by default. You check who has that permission via:

oc adm policy who-can --all-namespaces get nodes/log

## Examples

```bash
# Show kubelet logs from all control plane nodes
oc adm node-logs --role master -u kubelet

# See what logs are available in control plane nodes in /var/log
oc adm node-logs --role master --path=/

# Display cron log file from all control plane nodes
oc adm node-logs --role master --path=cron
```

## Options

- `--boot=0`
  Show messages from a specific boot. Use negative numbers, allowed [-100, 0], passing invalid boot offset will fail retrieving logs. Only applies to node service logs.

- `--case-sensitive=true`
  Filters are case sensitive by default. Pass --case-sensitive=false to do a case insensitive filter.

- `-g, --grep=''`
  Filter log entries by the provided regex pattern. Only applies to node service logs.

- `-o, --output=''`
  Display service logs in an alternate format (short, cat, json, short-unix). Only applies to node service logs.

- `--path='journal'`
  Retrieve the specified path within the node's /var/log/ folder. The 'journal' value will allow querying the services on supported operating systems.

- `--raw=false`
  Perform no transformation of the returned data.

- `--role=''`
  Set a label selector by node role.

- `-l, --selector=''`
  Selector (label query) to filter on.

- `--since=''`
  Return logs after a specific ISO timestamp or relative date. Only applies to node service logs.

- `--tail=0`
  Return up to this many lines (not more than 100k) from the end of the log. Only applies to node service logs.

- `--unify=false`
  Interleave logs by sorting the output. Defaults on when viewing node service logs.

- `-u, --unit=[]`
  Return log entries from the specified services(s) Only applies to node service logs.

- `--until=''`
  Return logs before a specific ISO timestamp or relative date. Only applies to node service logs.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm node-logs --help` / `gen-oc-help.py` で生成</sub>
