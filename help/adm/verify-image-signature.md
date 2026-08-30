# `oc adm verify-image-signature`

> Verify the image identity contained in the image signature

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `verify-image-signature`

## Usage

```
oc adm verify-image-signature IMAGE --expected-identity=EXPECTED_IDENTITY [--save] [flags] [options]
```

Verifies the image signature of an image imported to internal registry using the local public GPG key.

This command verifies if the image identity contained in the image signature can be trusted by using the public GPG key to verify the signature itself and matching the provided expected identity with the identity (pull spec) of the given image. By default, this command will use the public GPG keyring located in "$GNUPGHOME/.gnupg/pubring.gpg"

By default, this command will not save the result of the verification back to the image object; to do so the user must specify the "--save" flag. Note that to modify the image signature verification status, the user must have permissions to edit an image object (usually an "image-auditor" role).

Note that using the "--save" flag on already verified image together with invalid GPG key or invalid expected identity will cause the saved verification status to be removed and the image will become "unverified".

If this command is outside the cluster, users must specify the "--registry-url" parameter with the public URL of image registry.

To remove all verifications, users can use the "--remove-all" flag.

## Examples

```bash
# Verify the image signature and identity using the local GPG keychain
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 \
--expected-identity=registry.local:5000/foo/bar:v1

# Verify the image signature and identity using the local GPG keychain and save the status
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 \
--expected-identity=registry.local:5000/foo/bar:v1 --save

# Verify the image signature and identity via exposed registry route
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 \
--expected-identity=registry.local:5000/foo/bar:v1 \
--registry-url=docker-registry.foo.com

# Remove all signature verifications from the image
oc adm verify-image-signature sha256:c841e9b64e4579bd56c794bdd7c36e1c257110fd2404bebbb8b613e4935228c4 --remove-all
```

## Options

- `--expected-identity=''`
  An expected image docker reference to verify (required).

- `--insecure=false`
  If set, use the insecure protocol for registry communication.

- `--public-key='pubring.gpg'`
  A path to a public GPG key to be used for verification. (defaults to "pubring.gpg")

- `--registry-url=''`
  The address to use when contacting the registry, instead of using the internal cluster address. This is useful if you can't resolve or reach the internal registry address.

- `--remove-all=false`
  If set, all signature verifications will be removed from the given image.

- `--save=false`
  If true, the result of the verification will be saved to an image object.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm verify-image-signature --help` / `gen-oc-help.py` で生成</sub>
