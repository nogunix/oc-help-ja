# `oc create user`

> ユーザーを手動で作成する（自動作成が無効な場合のみ必要）

[`oc`](../oc.md) / [`oc create`](../create.md) / `user`

## Usage

```
oc create user NAME [flags] [options]
```

このコマンドを使うと、user オブジェクトを作成できます。

通常、ユーザーはログイン時に自動的に作成されます。（"lookup" マッピング方式を使うなどして）自動作成を無効にしている場合は、ユーザーを手動で作成する必要があります。

作成したユーザーでログインできるようにするには、対応する identity オブジェクトと user identity mapping オブジェクトも作成する必要があります。

## Examples

```bash
# ユーザー名 "ajones"、表示名 "Adam Jones" のユーザーを作成する
oc create user ajones --full-name="Adam Jones"
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--full-name=''`
  ユーザーの表示名

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

<sub>`$ oc create user --help` / `gen-oc-help.py` で生成</sub>
