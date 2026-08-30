# `oc adm migrate icsp`

> Update imagecontentsourcepolicy file(s) to imagedigestmirrorset file(s)

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm migrate`](../migrate.md) / `icsp`

## Usage

```
oc adm migrate icsp [flags] [options]
```

Update imagecontentsourcepolicy file(s) to imagedigestmirrorset file(s). If --dest-dir is unset, the imagedigestmirrorset file(s) that can be added to a cluster will be written to file(s) under the current directory.

## Examples

```bash
# Update the imagecontentsourcepolicy.yaml file to a new imagedigestmirrorset file under the mydir directory
oc adm migrate icsp imagecontentsourcepolicy.yaml --dest-dir mydir
```

## Options

- `--dest-dir=''`
  Set a specific directory on the local machine to write imagedigestmirrorset file(s) to.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm migrate icsp --help` / `gen-oc-help.py` で生成</sub>
