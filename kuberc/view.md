# `oc kuberc view`

> Display the current kuberc configuration

[`oc`](../oc.md) / [`oc kuberc`](../kuberc.md) / `view`

## Usage

```
oc kuberc view [options]
```

Display the contents of the kuberc file in the specified output format.

## Examples

```bash
# View kuberc configuration in YAML format (default)
oc kuberc view

# View kuberc configuration in JSON format
oc kuberc view --output json

# View a specific kuberc file
oc kuberc view --kuberc /path/to/kuberc
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--kuberc=''`
  Path to the kuberc file to use for preferences. This can be disabled by exporting KUBECTL_KUBERC=false feature gate or turning off the feature KUBERC=off.

- `-o, --output='yaml'`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc kuberc view --help` / `gen-oc-help.py` で生成</sub>
