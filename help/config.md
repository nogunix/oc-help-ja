# `oc config`

> Modify kubeconfig files

[`oc`](oc.md) / `config`

## Usage

```
oc config SUBCOMMAND [options]
```

Modify kubeconfig files using subcommands like "oc config set current-context my-context".

The loading order follows these rules:

1.  If the --kubeconfig flag is set, then only that file is loaded. The flag may only be set once and no merging takes place.
2.  If $KUBECONFIG environment variable is set, then it is used as a list of paths (normal path delimiting rules for your system). These paths are merged. When a value is modified, it is modified in the file that defines the stanza. When a value is created, it is created in the first file that exists. If no files in the chain exist, then it creates the last file in the list.
3.  Otherwise, ${HOME}/.kube/config is used and no merging takes place.

## Subcommands

- [`current-context`](config/current-context.md) — Display the current-context
- [`delete-cluster`](config/delete-cluster.md) — Delete the specified cluster from the kubeconfig
- [`delete-context`](config/delete-context.md) — Delete the specified context from the kubeconfig
- [`delete-user`](config/delete-user.md) — Delete the specified user from the kubeconfig
- [`get-clusters`](config/get-clusters.md) — Display clusters defined in the kubeconfig
- [`get-contexts`](config/get-contexts.md) — Describe one or many contexts
- [`get-users`](config/get-users.md) — Display users defined in the kubeconfig
- [`new-admin-kubeconfig`](config/new-admin-kubeconfig.md) — Generate, make the server trust, and display a new admin.kubeconfig
- [`new-kubelet-bootstrap-kubeconfig`](config/new-kubelet-bootstrap-kubeconfig.md) — Generate, make the server trust, and display a new kubelet /etc/kubernetes/kubeconfig
- [`refresh-ca-bundle`](config/refresh-ca-bundle.md) — Update the OpenShift CA bundle by contacting the API server
- [`rename-context`](config/rename-context.md) — Rename a context from the kubeconfig file
- [`set`](config/set.md) — Set an individual value in a kubeconfig file
- [`set-cluster`](config/set-cluster.md) — Set a cluster entry in kubeconfig
- [`set-context`](config/set-context.md) — Set a context entry in kubeconfig
- [`set-credentials`](config/set-credentials.md) — Set a user entry in kubeconfig
- [`unset`](config/unset.md) — Unset an individual value in a kubeconfig file
- [`use-context`](config/use-context.md) — Set the current-context in a kubeconfig file
- [`view`](config/view.md) — Display merged kubeconfig settings or a specified kubeconfig file

> Use "oc config `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc config --help` / `gen-oc-help.py` で生成</sub>
