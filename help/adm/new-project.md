# `oc adm new-project`

> Create a new project

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `new-project`

## Usage

```
oc adm new-project NAME [--display-name=DISPLAYNAME] [--description=DESCRIPTION] [flags] [options]
```

Use this command to create a project. You may optionally specify metadata about the project, an admin user (and role, if you want to use a non-default admin role), and a node selector to restrict which nodes pods in this project can be scheduled to.

## Examples

```bash
# Create a new project using a node selector
oc adm new-project myproject --node-selector='type=user-node,region=east'
```

## Options

- `--admin=''`
  Project admin username

- `--admin-role='admin'`
  Project admin role name in the cluster policy

- `--description=''`
  Project description

- `--display-name=''`
  Project display name

- `--node-selector=''`
  Restrict pods onto nodes matching given label selector. Format: '`<key1>`=`<value1>`, `<key2>`=`<value2>`...'. Specifying "" means any node, not default. If unspecified, cluster default node selector will be used.

> Use "oc options" for a list of global command-line options (applies to all commands).

---

<sub>`$ oc adm new-project --help` / `gen-oc-help.py` で生成</sub>
