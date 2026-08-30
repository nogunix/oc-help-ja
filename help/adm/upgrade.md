# `oc adm upgrade`

> Upgrade a cluster or adjust the upgrade channel

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `upgrade`

## Usage

```
oc adm upgrade --to=VERSION [flags] [options]
```

Check on upgrade status or upgrade the cluster to a newer version

This command assists with cluster upgrades. If no arguments are passed the command will retrieve the current version info and display whether an upgrade is in progress or whether any errors might prevent an upgrade, as well as show the suggested updates available to the cluster. Information about compatible updates is periodically retrieved from the update server and cached on the cluster - these are updates that are known to be supported as upgrades from the current version.

Passing --to=VERSION or --to-image=IMAGE will upgrade the cluster to one of the available updates or report an error if no such version exists. The cluster will then upgrade itself and report status that is available via "oc get clusterversion" and "oc describe clusterversion".

Passing --to-multi-arch will upgrade the cluster from a single-architecture to a multi-architecture cluster at the current version.

If there are no versions available, or a bug in the cluster version operator prevents updates from being retrieved, --to-image may be combined with the more powerful and dangerous --allow-explicit-upgrade. This instructs the cluster to upgrade to the contents of the specified release image, regardless of whether that upgrade is known to be recommended for the current version. While rolling back to a previous patch (z stream) version (4.1.2 -> 4.1.1) may be safe, upgrading more than one minor version ahead (4.1 -> 4.3) or downgrading one minor version (4.2 -> 4.1) is likely to cause data corruption or to completely break a cluster.

There are two layers of upgrade guards: client-side and cluster-side.

Client-side guards include checks for whether the cluster is already being upgraded, or if the cluster is reporting a failure.  It is usually best to give these conditions time to resolve, or to actively work to resolve them.  But if you decide to trigger the update regardless of these concerns, use --allow-upgrade-with-warnings.

Cluster-side guards include checks for release verification and upgradeable conditions. You can push through them with --force, which is passed through to ClusterVersion's spec.desiredUpdate.force, but only do that if:

- you are testing unsigned release images in short-lived test clusters or
- you are working around a known bug in the cluster-version operator and you have verified the authenticity of the provided image yourself.

The provided image will run with full administrative access to the cluster. Do not use --force with images that come from unknown or potentially malicious sources.

## Subcommands

- [`channel`](upgrade/channel.md) — Set or clear the update channel
- [`recommend`](upgrade/recommend.md) — Displays cluster update recommendations.
- [`status`](upgrade/status.md) — Display the status of the current cluster version update or multi-arch migration

## Examples

```bash
# View the update status and available cluster updates
oc adm upgrade

# Update to the latest version
oc adm upgrade --to-latest=true
```

## Options

- `--allow-explicit-upgrade=false`
  Upgrade even if the upgrade target is not listed in the available versions list.

- `--allow-not-recommended=false`
  Allows upgrade to a version when it is supported but not recommended for updates.

- `--allow-upgrade-with-warnings=false`
  Upgrade regardless of client-side guard failures, such as upgrades in progress or failing clusters.

- `--clear=false`
  If an upgrade has been requested but not yet downloaded, cancel the update. This has no effect once the update has started.

- `--force=false`
  Upgrade regardless of cluster-side guard failures, such as release verification or upgradeable conditions. Only use this if you are testing unsigned release images or you are working around a known bug in the cluster-version operator and you have verified the authenticity of the provided image yourself.

- `--include-not-recommended=false`
  Display additional updates which are not recommended based on your cluster configuration.

- `--to=''`
  Specify the version to upgrade to. The version must be on the list of available updates.

- `--to-image=''`
  Provide a release image to upgrade to.

- `--to-latest=false`
  Use the latest (highest Semantic Version) available version.

- `--to-multi-arch=false`
  Upgrade current version to multi architecture.

> Use "oc adm upgrade `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm upgrade --help` / `gen-oc-help.py` で生成</sub>
