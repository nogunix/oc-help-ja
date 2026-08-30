# `oc get-token`

> Experimental: Get token from external OIDC issuer as credentials exec plugin

[`oc`](oc.md) / `get-token`

## Usage

```
oc get-token --oidc-client-id=CLIENT_ID --oidc-issuer-url=ISSUER_URL [flags] [options]
```

Experimental: This command is under development and may change without notice. Built-in Credential Exec plugin of the oc.

It supports Auth Code, Auth Code + PKCE in addition to refresh token. get-token caches the ID token and Refresh token after the auth code flow is successfully completed and once ID token expires, command tries to get the new token by using the refresh token flow. Although it is optional, command also supports getting client secret to behave as an confidential client.

## Examples

```bash
# Starts an auth code flow to the issuer URL with the client ID and the given extra scopes
oc get-token --client-id=client-id --issuer-url=test.issuer.url --extra-scopes=email,profile

# Starts an auth code flow to the issuer URL with a different callback address
oc get-token --client-id=client-id --issuer-url=test.issuer.url --callback-address=127.0.0.1:8343
```

## Options

- `--auto-open-browser=false`
  Specify browser is automatically opened or not.

- `--callback-address='127.0.0.1:0'`
  Callback address where external OIDC issuer redirects to after flow is completed. Defaults to 127.0.0.1:0 to pick a random port.

- `--client-id=''`
  Client ID of the user managed by the external OIDC provider

- `--client-secret=''`
  Client Secret of the user managed by the external OIDC provider. Optional.

- `--extra-scopes=[]`
  Extra scopes for the auth request to the external OIDC provider. Optional.

- `--issuer-url=''`
  Issuer URL of the external OIDC provider

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc get-token --help` / `gen-oc-help.py` で生成</sub>
