# `oc adm certificate approve`

> Approve a certificate signing request

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm certificate`](../certificate.md) / `approve`

## Usage

```
oc adm certificate approve (-f FILENAME | NAME) [options]
```

oc adm certificate approve allows a cluster admin to approve a certificate signing request (CSR). This action tells a certificate signing controller to issue a certificate to the requester with the attributes requested in the CSR.

SECURITY NOTICE: Depending on the requested attributes, the issued certificate can potentially grant a requester access to cluster resources or to authenticate as a requested identity. Before approving a CSR, ensure you understand what the signed certificate can do.

## Examples

```bash
# Approve CSR 'csr-sqgzp'
oc adm certificate approve csr-sqgzp
```

## Options

- `--allow-missing-template-keys=true`
  If true, ignore any errors in templates when a field or map key is missing in the template. Only applies to golang and jsonpath output formats.

- `-f, --filename=[]`
  Filename, directory, or URL to files identifying the resource to update

- `--force=false`
  Update the CSR even if it is already approved.

- `-k, --kustomize=''`
  Process the kustomization directory. This flag can't be used together with -f or -R.

- `-o, --output=''`
  Output format. One of: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file).

- `-R, --recursive=false`
  Process the directory used in -f, --filename recursively. Useful when you want to manage related manifests organized within the same directory.

- `--show-managed-fields=false`
  If true, keep the managedFields when printing objects in JSON or YAML format.

- `--template=''`
  Template string or path to template file to use when -o=go-template, -o=go-template-file. The template format is golang templates [http://golang.org/pkg/text/template/#pkg-overview].

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm certificate approve --help` / `gen-oc-help.py` で生成</sub>
