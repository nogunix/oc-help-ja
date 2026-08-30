# `oc rollout latest`

> トリガーの最新の状態を使って、デプロイメント設定の新しいロールアウトを開始する

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `latest`

## Usage

```
oc rollout latest DEPLOYMENTCONFIG [flags] [options]
```

このコマンドは、手動でロールアウトを実行する場合に適しています。新しいロールアウトの実行を完全に制御したい場合は、"oc set triggers --manual" でデプロイメント設定のすべてのトリガーを無効にしたうえで、新しいデプロイ処理を実行したいタイミングでこのコマンドを使い、イメージ変更トリガーが指すクラスタ内の最新イメージを取り込んでください。

## Examples

```bash
# イメージ変更トリガーに定義された最新のイメージを基に、新しいロールアウトを開始する
oc rollout latest dc/nginx

# ロールアウトされたデプロイメント設定を表示する
oc rollout latest dc/nginx -o json
```

## Options

- `--again=false`
  true の場合、トリガーからの状態更新を行わずに、現在の Pod テンプレートをデプロイします

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollout latest --help` / `gen-oc-help.py` で生成</sub>
