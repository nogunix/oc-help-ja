# `oc login`

> Log in to a server

[`oc`](oc.md) / `login`

## Usage

```
oc login [URL] [flags] [options]
```

Log in to your server and save login for subsequent use.

First-time users of the client should run this command to connect to a server, establish an authenticated session, and save connection to the configuration file. The default configuration will be saved to your home directory under ".kube/config".

The information required to login -- like username and password, a session token, or the server details -- can be provided through flags. If not provided, the command will prompt for user input as needed. It is also possible to login through a web browser by providing the respective flag.

## Examples

```bash
# Log in interactively
oc login --username=myuser

# Log in to the given server with the given certificate authority file
oc login localhost:8443 --certificate-authority=/path/to/cert.crt

# Log in to the given server with the given credentials (will not prompt interactively)
oc login localhost:8443 --username=myuser --password=mypass

# Log in to the given server through a browser
oc login localhost:8443 --web --callback-port 8280

# Log in to the given server through a browser without opening it automatically (print URL only)
oc login localhost:8443 --web --auto-open-browser=false --callback-port 8280

# Log in to the external OIDC issuer through Auth Code + PKCE by starting a local server listening on port 8080
oc login localhost:8443 --exec-plugin=oc-oidc --client-id=client-id --extra-scopes=email,profile --callback-port=8080
```

## Options

- `--auto-open-browser=false`
  Experimental: Automatically open browser for login. When used with --web, defaults to true. When used with --exec-plugin for external OIDC, defaults to false.

- `-c, --callback-port=0`
  Port for the callback server when using --web. Defaults to a random open port

- `--client-id=''`
  Experimental: Client ID for external OIDC issuer. Only supports Auth Code + PKCE. Required.

- `--client-secret=''`
  Experimental: Client secret for external OIDC issuer. Optional.

- `--exec-plugin=''`
  Experimental: Specify credentials exec plugin type to be used to authenticate external OIDC issuer. Currently only 'oc-oidc' is supported

- `--extra-scopes=[]`
  Experimental: Extra scopes for external OIDC issuer. Optional.

- `--issuer-url=''`
  Experimental: Issuer url for external issuer. Required.

- `--oidc-certificate-authority=''`
  Experimental: The path to a certificate authority bundle to use when communicating with external OIDC issuer.

- `-p, --password=''`
  Password for server

- `-u, --username=''`
  Username for server

- `-w, --web=false`
  Login with web browser. Starts a local HTTP callback server to perform the OAuth2 Authorization Code Grant flow. Use with caution on multi-user systems, as the server's port will be open to all users.

- `--certificate-authority=''`
  Path to a cert file for the certificate authority

- `--insecure-skip-tls-verify=false`
  If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure

- `--token=''`
  Bearer token for authentication to the API server

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc login --help` / `gen-oc-help.py` で生成</sub>
