# `oc auth whoami`

> 実験的機能: 自分自身のサブジェクト属性を確認する

[`oc`](../oc.md) / [`oc auth`](../auth.md) / `whoami`

## Usage

```
oc auth whoami [options]
```

実験的機能: 自分が誰か、およびその属性（グループ、extra）を確認します。

        This command is helpful to get yourself aware of the current user attributes,
        especially when dynamic authentication, e.g., token webhook, auth proxy, or OIDC provider,
        is enabled in the Kubernetes cluster.

## Examples

```bash
# 自分のサブジェクト属性を取得する
oc auth whoami

# 自分のサブジェクト属性を JSON 形式で取得する
oc auth whoami -o json
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc auth whoami --help` / `gen-oc-help.py` で生成</sub>
