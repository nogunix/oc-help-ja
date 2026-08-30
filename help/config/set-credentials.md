# `oc config set-credentials`

> Set a user entry in kubeconfig

[`oc`](../oc.md) / [`oc config`](../config.md) / `set-credentials`

## Usage

```
oc config set-credentials NAME [--client-certificate=path/to/certfile] [--client-key=path/to/keyfile] [--token=bearer_token] [--username=basic_user] [--password=basic_password] [--auth-provider=provider_name] [--auth-provider-arg=key=value] [--exec-command=exec_command] [--exec-api-version=exec_api_version] [--exec-arg=arg] [--exec-env=key=value] [options]
```

Specifying a name that already exists will merge new fields on top of existing values.

        Client-certificate flags:
        --client-certificate=certfile --client-key=keyfile

        Bearer token flags:
        --token=bearer_token

        Basic auth flags:
        --username=basic_user --password=basic_password

Bearer token and basic auth are mutually exclusive.

## Examples

```bash
# Set only the "client-key" field on the "cluster-admin"
# entry, without touching other values
oc config set-credentials cluster-admin --client-key=~/.kube/admin.key

# Set basic auth for the "cluster-admin" entry
oc config set-credentials cluster-admin --username=admin --password=uXFGweU9l35qcif

# Embed client certificate data in the "cluster-admin" entry
oc config set-credentials cluster-admin --client-certificate=~/.kube/admin.crt --embed-certs=true

# Enable the Google Compute Platform auth provider for the "cluster-admin" entry
oc config set-credentials cluster-admin --auth-provider=gcp

# Enable the OpenID Connect auth provider for the "cluster-admin" entry with additional arguments
oc config set-credentials cluster-admin --auth-provider=oidc --auth-provider-arg=client-id=foo --auth-provider-arg=client-secret=bar

# Remove the "client-secret" config value for the OpenID Connect auth provider for the "cluster-admin" entry
oc config set-credentials cluster-admin --auth-provider=oidc --auth-provider-arg=client-secret-

# Enable new exec auth plugin for the "cluster-admin" entry
oc config set-credentials cluster-admin --exec-command=/path/to/the/executable --exec-api-version=client.authentication.k8s.io/v1beta1

# Enable new exec auth plugin for the "cluster-admin" entry with interactive mode
oc config set-credentials cluster-admin --exec-command=/path/to/the/executable --exec-api-version=client.authentication.k8s.io/v1beta1 --exec-interactive-mode=Never

# Define new exec auth plugin arguments for the "cluster-admin" entry
oc config set-credentials cluster-admin --exec-arg=arg1 --exec-arg=arg2

# Create or update exec auth plugin environment variables for the "cluster-admin" entry
oc config set-credentials cluster-admin --exec-env=key1=val1 --exec-env=key2=val2

# Remove exec auth plugin environment variables for the "cluster-admin" entry
oc config set-credentials cluster-admin --exec-env=var-to-remove-
```

## Options

- `--auth-provider=''`
  Auth provider for the user entry in kubeconfig

- `--auth-provider-arg=[]`
  'key=value' arguments for the auth provider

- `--client-certificate=''`
  Path to client-certificate file for the user entry in kubeconfig

- `--client-key=''`
  Path to client-key file for the user entry in kubeconfig

- `--embed-certs=false`
  Embed client cert/key for the user entry in kubeconfig

- `--exec-api-version=''`
  API version of the exec credential plugin for the user entry in kubeconfig

- `--exec-arg=[]`
  New arguments for the exec credential plugin command for the user entry in kubeconfig

- `--exec-command=''`
  Command for the exec credential plugin for the user entry in kubeconfig

- `--exec-env=[]`
  'key=value' environment values for the exec credential plugin

- `--exec-interactive-mode=''`
  InteractiveMode of the exec credentials plugin for the user entry in kubeconfig

- `--exec-provide-cluster-info=false`
  ProvideClusterInfo of the exec credentials plugin for the user entry in kubeconfig

- `--password=''`
  password for the user entry in kubeconfig

- `--token=''`
  token for the user entry in kubeconfig

- `--username=''`
  username for the user entry in kubeconfig

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config set-credentials --help` / `gen-oc-help.py` で生成</sub>
