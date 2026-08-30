# `oc adm policy add-scc-to-user`

> ユーザーまたはサービスアカウントに security context constraint を付与する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm policy`](../policy.md) / `add-scc-to-user`

## Usage

```
oc adm policy add-scc-to-user SCC (USER | -z SERVICEACCOUNT) [USER ...] [flags] [options]
```

## Examples

```bash
# user1 と user2 に 'restricted' security context constraint を付与する
oc adm policy add-scc-to-user restricted user1 user2

# 現在の namespace の serviceaccount1 に 'privileged' security context constraint を付与する
oc adm policy add-scc-to-user privileged -z serviceaccount1
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-z, --serviceaccount=[]`
  ユーザーとして使用する、現在の namespace 内のサービスアカウント

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm policy add-scc-to-user --help` / `gen-oc-help.py` で生成</sub>
