# `oc create secret tls`

> TLS シークレットを作成する

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create secret`](../secret.md) / `tls`

## Usage

```
oc create secret tls NAME --cert=path/to/cert/file --key=path/to/key/file [--dry-run=server|client|none] [options]
```

指定した公開鍵 / 秘密鍵のペアから TLS シークレットを作成します。

公開鍵 / 秘密鍵のペアが事前に存在している必要があります。公開鍵証明書は .PEM 形式で、指定した秘密鍵と対応している必要があります。

## Examples

```bash
# 指定した鍵ペアから tls-secret という名前の TLS シークレットを新規作成する
oc create secret tls tls-secret --cert=path/to/tls.crt --key=path/to/tls.key
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--append-hash=false`
  シークレットの名前に、その内容のハッシュを付加します。

- `--cert=''`
  PEM エンコードされた公開鍵証明書のパス。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--key=''`
  指定した証明書に対応する秘密鍵のパス。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create secret tls --help` / `gen-oc-help.py` で生成</sub>
