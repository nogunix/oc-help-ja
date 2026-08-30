# `oc adm`

> Tools for managing a cluster

[`oc`](oc.md) / `adm`

## Usage

```
oc adm [flags] [options]
```

Administrative Commands

Actions for administering an OpenShift cluster are exposed here.

## Subcommands

- [`build-chain`](adm/build-chain.md) — Output the inputs and dependencies of your builds
- [`catalog`](adm/catalog.md) — Tools for managing the OpenShift OLM Catalogs
- [`certificate`](adm/certificate.md) — Approve or reject certificate requests
- [`copy-to-node`](adm/copy-to-node.md) — Copy specified files to the node
- [`cordon`](adm/cordon.md) — Mark node as unschedulable
- [`create-bootstrap-project-template`](adm/create-bootstrap-project-template.md) — Create a bootstrap project template
- [`create-error-template`](adm/create-error-template.md) — Create an error page template
- [`create-login-template`](adm/create-login-template.md) — Create a login template
- [`create-provider-selection-template`](adm/create-provider-selection-template.md) — Create a provider selection template
- [`drain`](adm/drain.md) — Drain node in preparation for maintenance
- [`groups`](adm/groups.md) — Manage groups
- [`inspect`](adm/inspect.md) — Collect debugging data for a given resource
- [`migrate`](adm/migrate.md) — Migrate data in the cluster
- [`must-gather`](adm/must-gather.md) — Launch a new instance of a pod for gathering debug information
- [`new-project`](adm/new-project.md) — Create a new project
- [`node-image`](adm/node-image.md) — Add nodes to an existing cluster
- [`node-logs`](adm/node-logs.md) — Display and filter node logs
- [`ocp-certificates`](adm/ocp-certificates.md) — Tools for managing a cluster's certificates
- [`policy`](adm/policy.md) — Manage cluster authorization and security policy
- [`prune`](adm/prune.md) — Remove older versions of resources from the server
- [`reboot-machine-config-pool`](adm/reboot-machine-config-pool.md) — Initiate reboot of the specified MachineConfigPool
- [`release`](adm/release.md) — Tools for managing the OpenShift release process
- [`restart-kubelet`](adm/restart-kubelet.md) — Restart kubelet on the specified nodes
- [`taint`](adm/taint.md) — Update the taints on one or more nodes
- [`top`](adm/top.md) — Show usage statistics of resources on the server
- [`uncordon`](adm/uncordon.md) — Mark node as schedulable
- [`upgrade`](adm/upgrade.md) — Upgrade a cluster or adjust the upgrade channel
- [`verify-image-signature`](adm/verify-image-signature.md) — Verify the image identity contained in the image signature
- [`wait-for-node-reboot`](adm/wait-for-node-reboot.md) — Wait for nodes to reboot after running `oc adm reboot-machine-config-pool`
- [`wait-for-stable-cluster`](adm/wait-for-stable-cluster.md) — Wait for the platform operators to become stable

> Use "oc adm `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm --help` / `gen-oc-help.py` で生成</sub>
