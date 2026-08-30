# `oc adm migrate template-instances`

> テンプレートインスタンスが最新の group-version-kind を指すよう更新する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm migrate`](../migrate.md) / `template-instances`

## Usage

```
oc adm migrate template-instances [flags] [options]
```

テンプレートインスタンスが新しい API グループを参照するよう移行します。

このコマンドは、特定の group-version-kind を参照しているテンプレートインスタンスをすべて探し出し、別の等価な group-version-kind を参照するように更新します。

次の変換が行われます:

- .Build --> build.openshift.io/v1.Build
- .BuildConfig --> build.openshift.io/v1.BuildConfig
- .DeploymentConfig --> apps.openshift.io/v1.DeploymentConfig
- .Route --> route.openshift.io/v1.Route
- v1.Build --> build.openshift.io/v1.Build
- v1.BuildConfig --> build.openshift.io/v1.BuildConfig
- v1.DeploymentConfig --> apps.openshift.io/v1.DeploymentConfig
- v1.Route --> route.openshift.io/v1.Route

## Examples

```bash
# すべてのオブジェクトの更新を dry-run で実行する
oc adm migrate template-instances

# 実際に更新を実行するには、confirm フラグを付ける必要があります
oc adm migrate template-instances --confirm
```

## Options

- `-A, --all-namespaces=true`
  すべての namespace のオブジェクトを移行します。デフォルトは true です。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--confirm=false`
  true の場合、要求されたすべてのオブジェクトを移行します。デフォルトは false です。

- `-f, --filename=[]`
  使用する docker-compose.yml のファイル名、ディレクトリ、または URL

- `--from-key=''`
  指定した場合、キー（namespace/name または name）がこの値以上の項目のみを移行します

- `--include=[templateinstance]`
  移行するリソースタイプ。--filename を指定した場合、このフラグは上書きされます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--to-key=''`
  指定した場合、キー（namespace/name または name）がこの値より小さい項目のみを移行します

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm migrate template-instances --help` / `gen-oc-help.py` で生成</sub>
