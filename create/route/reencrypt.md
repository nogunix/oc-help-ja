# `oc create route reencrypt`

> reencrypt TLS 終端を使うルートを作成する

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create route`](../route.md) / `reencrypt`

## Usage

```
oc create route reencrypt [NAME] --service=SERVICE [flags] [options]
```

生成されるルートが公開する Service を --service フラグで指定します（名前だけ、または type/name の形式）。--dest-ca-cert フラグで宛先の CA 証明書を指定することもできます。--dest-ca-cert を省略した場合、ルートは service CA を使用します。つまり、その Service は serving cert signer が発行したサービング証明書を使用している必要があります。

## Examples

```bash
# frontend サービスを公開する "my-route" という名前のルートを作成する
oc create route reencrypt my-route --service=frontend --dest-ca-cert cert.cert

# frontend サービスを公開する reencrypt ルートを作成し、
# ルート名はデフォルトで Service 名になり、宛先の CA 証明書は
# デフォルトで service CA を使う
oc create route reencrypt --service=frontend
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--ca-cert=''`
  CA 証明書ファイルのパス。

- `--cert=''`
  証明書ファイルのパス。

- `--dest-ca-cert=''`
  ルーターから宛先への接続を保護するために使用する CA 証明書ファイルのパス。デフォルトは Service CA です。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--hostname=''`
  新しいルートにホスト名を設定する

- `--insecure-policy=''`
  新しいルートに insecure ポリシーを設定する

- `--key=''`
  鍵ファイルのパス。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--path=''`
  ルーターが監視し、Service へトラフィックを転送するパス。

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

<sub>`$ oc create route reencrypt --help` / `gen-oc-help.py` で生成</sub>
