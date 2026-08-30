# `oc adm upgrade recommend`

> Displays cluster update recommendations.

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm upgrade`](../upgrade.md) / `recommend`

## Usage

```
oc adm upgrade recommend [flags] [options]
```

This subcommand is read-only and does not affect the state of the cluster. To request an update, use the 'oc adm upgrade' subcommand.

By default, this command displays recent potential target releases.  Use '--version VERSION' to display context for a particular target release.  Use '--show-outdated-releases' to display all known targets, including older releases.

## Options

- `--accept=[]`
  Comma-delimited names for issues that you find acceptable.  With --version, any unaccepted issues will result in a non-zero exit code.

- `--quiet=false`
  When --quiet is true and --version is set, only print unaccepted issue names.

- `--show-outdated-releases=false`
  Display additional older releases.  These releases may be exposed to known issues which have been fixed in more recent releases.  But all updates will contain fixes not present in your current release.

- `--version=''`
  Select a particular target release to display by version.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm upgrade recommend --help` / `gen-oc-help.py` で生成</sub>
