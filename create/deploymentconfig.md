# `oc create deploymentconfig`

> 指定したイメージを使用するデプロイメント設定を、デフォルト設定で作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `deploymentconfig`

## Usage

```
oc create deploymentconfig NAME --image=IMAGE -- [COMMAND] [args...] [flags] [options]
```

指定したイメージを使用するデプロイメント設定を作成します。

デプロイメント設定は Pod のテンプレートを定義し、新しいイメージや設定変更のデプロイを管理します。

エイリアス: deploymentconfig, dc

## Examples

```bash
# my-nginx という名前の nginx デプロイメント設定を作成する
oc create deploymentconfig my-nginx --image=nginx
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--image=''`
  実行するコンテナのイメージ。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create deploymentconfig --help` / `gen-oc-help.py` で生成</sub>
