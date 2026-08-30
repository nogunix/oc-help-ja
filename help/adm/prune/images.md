# `oc adm prune images`

> Remove unreferenced images

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `images`

## Usage

```
oc adm prune images [flags] [options]
```

Remove image stream tags, images, and image layers by age or usage.

This command removes historical image stream tags, unused images, and unreferenced image layers from the integrated registry. By default, all images are considered as candidates. The command can be instructed to consider only images that have been directly pushed to the registry by supplying --all=false flag.

By default, the prune operation performs a dry run making no changes to internal registry. A --confirm flag is needed for changes to be effective. The flag requires a valid route to the integrated container image registry. If this command is run outside of the cluster network, the route needs to be provided using --registry-url.

Only a user with a cluster role system:image-pruner or higher who is logged-in will be able to actually delete the images.

If the registry is secured with a certificate signed by a self-signed root certificate authority other than the one present in current user's config, you may need to specify it using --certificate-authority flag.

Insecure connection is allowed in the following cases unless certificate-authority is specified:

1.  --force-insecure is given
2.  provided registry-url is prefixed with http://
3.  registry url is a private or link-local address
4.  user's config allows for insecure connection (the user logged in to the cluster with --insecure-skip-tls-verify or allowed for insecure connection)

## Examples

```bash
# See what the prune command would delete if only images and their referrers were more than an hour old
# and obsoleted by 3 newer revisions under the same tag were considered
oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m

# To actually perform the prune operation, the confirm flag must be appended
oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m --confirm

# See what the prune command would delete if we are interested in removing images
# exceeding currently set limit ranges ('openshift.io/Image')
oc adm prune images --prune-over-size-limit

# To actually perform the prune operation, the confirm flag must be appended
oc adm prune images --prune-over-size-limit --confirm

# Force the insecure HTTP protocol with the particular registry host name
oc adm prune images --registry-url=http://registry.example.org --confirm

# Force a secure connection with a custom certificate authority to the particular registry host name
oc adm prune images --registry-url=registry.example.org --certificate-authority=/path/to/custom/ca.crt --confirm
```

## Options

- `--all=true`
  Include images that were imported from external registries as candidates for pruning.  If pruned, all the mirrored objects associated with them will also be removed from the integrated registry.

- `--certificate-authority=''`
  The path to a certificate authority bundle to use when communicating with the managed container image registries. Defaults to the certificate authority data from the current user's config file. It cannot be used together with --force-insecure.

- `--confirm=false`
  If true, specify that image pruning should proceed. Defaults to false, displaying what would be deleted but not actually deleting anything. Requires a valid route to the integrated container image registry (see --registry-url).

- `--force-insecure=false`
  If true, allow an insecure connection to the container image registry that is hosted via HTTP or has an invalid HTTPS certificate. Whenever possible, use --certificate-authority instead of this dangerous option.

- `--ignore-invalid-refs=false`
  If true, the pruning process will ignore all errors while parsing image references. This means that the pruning process will ignore the intended connection between the object and the referenced image. As a result an image may be incorrectly deleted as unused.

- `--keep-tag-revisions=3`
  Specify the number of image revisions for a tag in an image stream that will be preserved.

- `--keep-younger-than=1h0m0s`
  Specify the minimum age of an image and its referrers for it to be considered a candidate for pruning.

- `--num-workers=5`
  Specify the number of parallel workers to use when running prune operations.

- `--prune-over-size-limit=false`
  Specify if images which are exceeding LimitRanges (see 'openshift.io/Image'), specified in the same namespace, should be considered for pruning. This flag cannot be combined with --keep-younger-than nor --keep-tag-revisions.

- `--prune-registry=true`
  If false, the prune operation will clean up image API objects, but the none of the associated content in the registry is removed.  Note, if only image API objects are cleaned up through use of this flag, the only means for subsequently cleaning up registry data corresponding to those image API objects is to employ the 'hard prune' administrative task.

- `--registry-url=''`
  The address to use when contacting the registry, instead of using the default value. This is useful if you can't resolve or reach the registry (e.g.; the default is a cluster-internal URL) but you do have an alternative route that works. Particular transport protocol can be enforced using '`<scheme>`://' prefix.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm prune images --help` / `gen-oc-help.py` で生成</sub>
