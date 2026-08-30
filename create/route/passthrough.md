# `oc create route passthrough`

> passthrough TLS 終端を使うルートを作成する

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create route`](../route.md) / `passthrough`

## Usage

```
oc create route passthrough [NAME] --service=SERVICE [flags] [options]
```

生成されるルートが公開する Service を --service フラグで指定します（名前だけ、または type/name の形式）。

## Examples

```bash
# frontend サービスを公開する "my-route" という名前の passthrough ルートを作成する
oc create route passthrough my-route --service=frontend

# frontend サービスを公開する passthrough ルートを作成し、次を指定する
# ホスト名。ルート名を省略した場合は、Service 名が使用されます
oc create route passthrough --service=frontend --hostname=www.example.com
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--hostname=''`
  新しいルートにホスト名を設定する

- `--insecure-policy=''`
  新しいルートに insecure ポリシーを設定する

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--port=''`
  ルートがトラフィックを転送する先の、Service ポートの名前またはコンテナポート番号

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--service=''`
  この新しいルートが公開する Service の名前

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--wildcard-policy=''`
  ホスト名の WildcardPolicy を設定します。デフォルトは "None" です。有効な値は "None" と "Subdomain" です

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create route passthrough --help` / `gen-oc-help.py` で生成</sub>
