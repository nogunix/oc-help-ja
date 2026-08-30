# `oc secrets link`

> Link secrets to a service account

[`oc`](../oc.md) / [`oc secrets`](../secrets.md) / `link`

## Usage

```
oc secrets link serviceaccounts-name secret-name [another-secret-name]... [flags] [options]
```

Linking a secret enables a service account to automatically use that secret for some forms of authentication.

## Examples

```bash
# Add an image pull secret to a service account to automatically use it for pulling pod images
oc secrets link serviceaccount-name pull-secret --for=pull

# Add an image pull secret to a service account to automatically use it for both pulling and pushing build images
oc secrets link builder builder-image-secret --for=pull,mount
```

## Options

- `--for=[mount]`
  type of secret to link: mount or pull

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc secrets link --help` / `gen-oc-help.py` で生成</sub>
