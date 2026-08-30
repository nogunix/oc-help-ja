# `oc create token`

> サービスアカウントのトークンを要求する

[`oc`](../oc.md) / [`oc create`](../create.md) / `token`

## Usage

```
oc create token SERVICE_ACCOUNT_NAME [options]
```

## Examples

```bash
# 現在の namespace のサービスアカウント "myapp" として kube-apiserver に認証するためのトークンを要求する
oc create token myapp

# 任意の namespace のサービスアカウントについてトークンを要求する
oc create token myapp --namespace myns

# 任意の有効期限を指定してトークンを要求する
oc create token myapp --duration 10m

# 任意の audience を指定してトークンを要求する
oc create token myapp --audience https://example.com

# Secret オブジェクトのインスタンスに紐づいたトークンを要求する
oc create token myapp --bound-object-kind Secret --bound-object-name mysecret

# 特定の UID を持つ Secret オブジェクトのインスタンスに紐づいたトークンを要求する
oc create token myapp --bound-object-kind Secret --bound-object-name mysecret --bound-object-uid 0d4691ed-659b-4935-a832-355f77ee47cc
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--audience=[]`
  要求するトークンの audience。指定しない場合は、Kubernetes API サーバーで使用するトークンを要求します。複数回指定すると、複数の audience で有効なトークンを要求できます。

- `--bound-object-kind=''`
  トークンを紐づけるオブジェクトの種類。サポートされる種類は Node、Pod、Secret です。指定する場合は --bound-object-name も指定する必要があります。

- `--bound-object-name=''`
  トークンを紐づけるオブジェクトの名前。そのオブジェクトが削除されるとトークンは失効します。--bound-object-kind が必要です。

- `--bound-object-uid=''`
  トークンを紐づけるオブジェクトの UID。--bound-object-kind と --bound-object-name が必要です。指定しない場合は、既存のオブジェクトの UID が使用されます。

- `--duration=0s`
  発行するトークンの希望有効期間。指定しない場合や 0 を指定した場合、有効期間はサーバーが自動的に決定します。サーバーは、これより長い、または短い有効期間のトークンを返すことがあります。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create token --help` / `gen-oc-help.py` で生成</sub>
