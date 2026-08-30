# `oc registry login`

> Log in to the integrated registry

[`oc`](../oc.md) / [`oc registry`](../registry.md) / `login`

## Usage

```
oc registry login  [flags] [options]
```

Log in to the OpenShift integrated registry.

This logs your local Docker client into the OpenShift integrated registry using the external registry name (if configured by your administrator). If you are logged in to the server using a client certificate the command will report an error because container registries do not generally allow client certificates.

As an advanced option you may specify the credentials to login with using --auth-basic with USER:PASSWORD.

You may specify an alternate file to write credentials to with --to instead of .docker/config.json in your home directory.

To detect the registry hostname the client will attempt to find an image stream in the current namespace or the openshift namespace and use the status fields that indicate the registry hostnames. If no image stream is found or if you do not have permission to view image streams you will have to pass the --registry flag with the desired host name.

You may also pass the --registry flag to login to the integrated registry but with a custom DNS name, or to an external registry. Note that in absence of --auth-basic=USER:PASSWORD, the authentication token from the connected kubeconfig file will be recorded as the auth entry in the credentials file (defaults to Docker config.json) for the passed registry value.

## Examples

```bash
# Log in to the integrated registry
oc registry login

# Log in to different registry using BASIC auth credentials
oc registry login --registry quay.io/myregistry --auth-basic=USER:PASS
```

## Options

- `--auth-basic=''`
  Provide credentials in the form 'user:password' to authenticate (advanced)

- `--insecure=false`
  Bypass HTTPS certificate verification when checking the registry login.

- `--registry=''`
  An alternate domain name and port to use for the registry, defaults to the cluster's configured external hostname.

- `-a, --registry-config=''`
  The location of the file your credentials will be stored in. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json or /run/containers/${UID}/auth.json. Default can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

- `--skip-check=false`
  Skip checking the credentials against the registry.

- `--to=''`
  The location of the file your credentials will be stored in. Alternatively REGISTRY_AUTH_FILE env variable can be also specified. Defaults to ${XDG_RUNTIME_DIR}/containers/auth.json or /run/containers/${UID}/auth.json. Default can be changed via the REGISTRY_AUTH_PREFERENCE env variable (deprecated) to a "docker" value to prioritizes Docker credentials over Podman's.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc registry login --help` / `gen-oc-help.py` で生成</sub>
