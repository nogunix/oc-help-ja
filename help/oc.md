# `oc`

> OpenShift Client

## Usage

```
oc [flags] [options]
```

This client helps you develop, build, deploy, and run your applications on any
OpenShift or Kubernetes cluster. It also includes the administrative
commands for managing a cluster under the 'adm' subcommand.

## Subcommands

### Basic Commands

- [`login`](login.md) — Log in to a server
- [`new-project`](new-project.md) — Request a new project
- [`new-app`](new-app.md) — Create a new application
- [`status`](status.md) — Show an overview of the current project
- [`project`](project.md) — Switch to another project
- [`projects`](projects.md) — Display existing projects
- [`explain`](explain.md) — Get documentation for a resource

### Build and Deploy Commands

- [`rollout`](rollout.md) — Manage the rollout of a resource
- [`rollback`](rollback.md) — Revert part of an application back to a previous deployment
- [`new-build`](new-build.md) — Create a new build configuration
- [`start-build`](start-build.md) — Start a new build
- [`cancel-build`](cancel-build.md) — Cancel running, pending, or new builds
- [`import-image`](import-image.md) — Import images from a container image registry
- [`tag`](tag.md) — Tag existing images into image streams

### Application Management Commands

- [`create`](create.md) — Create a resource from a file or from stdin
- [`apply`](apply.md) — Apply a configuration to a resource by file name or stdin
- [`get`](get.md) — Display one or many resources
- [`describe`](describe.md) — Show details of a specific resource or group of resources
- [`edit`](edit.md) — Edit a resource on the server
- [`set`](set.md) — Commands that help set specific features on objects
- [`label`](label.md) — Update the labels on a resource
- [`annotate`](annotate.md) — Update the annotations on a resource
- [`expose`](expose.md) — Expose a replicated application as a service or route
- [`delete`](delete.md) — Delete resources by file names, stdin, resources and names, or by resources and label selector
- [`scale`](scale.md) — Set a new size for a deployment, replica set, or replication controller
- [`autoscale`](autoscale.md) — Autoscale a deployment config, deployment, replica set, stateful set, or replication controller
- [`secrets`](secrets.md) — Manage secrets

### Troubleshooting and Debugging Commands

- [`logs`](logs.md) — Print the logs for a container in a pod
- [`rsh`](rsh.md) — Start a shell session in a container
- [`rsync`](rsync.md) — Copy files between a local file system and a pod
- [`port-forward`](port-forward.md) — Forward one or more local ports to a pod
- [`debug`](debug.md) — Launch a new instance of a pod for debugging
- [`exec`](exec.md) — Execute a command in a container
- [`proxy`](proxy.md) — Run a proxy to the Kubernetes API server
- [`attach`](attach.md) — Attach to a running container
- [`run`](run.md) — Run a particular image on the cluster
- [`cp`](cp.md) — Copy files and directories to and from containers
- [`wait`](wait.md) — Wait for a specific condition on one or many resources
- [`events`](events.md) — List events

### Advanced Commands

- [`adm`](adm.md) — Tools for managing a cluster
- [`replace`](replace.md) — Replace a resource by file name or stdin
- [`patch`](patch.md) — Update fields of a resource
- [`process`](process.md) — Process a template into list of resources
- [`extract`](extract.md) — Extract secrets or config maps to disk
- [`observe`](observe.md) — Observe changes to resources and react to them (experimental)
- [`policy`](policy.md) — Manage authorization policy
- [`auth`](auth.md) — Inspect authorization
- [`image`](image.md) — Useful commands for managing images
- [`registry`](registry.md) — Commands for working with the registry
- [`idle`](idle.md) — Idle scalable resources
- [`api-versions`](api-versions.md) — Print the supported API versions on the server, in the form of "group/version"
- [`api-resources`](api-resources.md) — Print the supported API resources on the server
- [`cluster-info`](cluster-info.md) — Display cluster information
- [`diff`](diff.md) — Diff the live version against a would-be applied version
- [`kustomize`](kustomize.md) — Build a kustomization target from a directory or URL

### Settings Commands

- [`get-token`](get-token.md) — Experimental: Get token from external OIDC issuer as credentials exec plugin
- [`logout`](logout.md) — End the current server session
- [`config`](config.md) — Modify kubeconfig files
- [`whoami`](whoami.md) — Return information about the current session
- [`completion`](completion.md) — Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

### Other Commands

- [`plugin`](plugin.md) — Provides utilities for interacting with plugins
- [`version`](version.md) — Print the client and server version information

> Use "oc `<command>` --help" for more information about a given command.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc --help` / `gen-oc-help.py` で生成</sub>
