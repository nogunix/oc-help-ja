# `oc create secret generic`

> ローカルのファイル、ディレクトリ、またはリテラル値からシークレットを作成する

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create secret`](../secret.md) / `generic`

## Usage

```
oc create secret generic NAME [--type=string] [--from-file=[key=]source] [--from-literal=key1=value1] [--dry-run=server|client|none] [options]
```

ファイル、ディレクトリ、または指定したリテラル値からシークレットを作成します。

1 つのシークレットに、1 つ以上のキー / 値のペアをまとめられます。

ファイルを基にシークレットを作成する場合、キーはデフォルトでそのファイルの basename、値はデフォルトでファイルの内容になります。basename が無効なキーの場合や、自分でキーを決めたい場合は、別のキーを指定できます。

ディレクトリを基にシークレットを作成する場合、ディレクトリ内で basename が有効なキーとなる各ファイルがシークレットにまとめられます。通常のファイル以外のディレクトリエントリ（サブディレクトリ、シンボリックリンク、デバイス、パイプなど）は無視されます。

## Examples

```bash
# フォルダ bar 内の各ファイルをキーとして、my-secret という名前のシークレットを新規作成する
oc create secret generic my-secret --from-file=path/to/bar

# ディスク上の名前ではなく、指定したキーを使って my-secret という名前のシークレットを新規作成する
oc create secret generic my-secret --from-file=ssh-privatekey=path/to/id_rsa --from-file=ssh-publickey=path/to/id_rsa.pub

# key1=supersecret と key2=topsecret を持つ my-secret という名前のシークレットを新規作成する
oc create secret generic my-secret --from-literal=key1=supersecret --from-literal=key2=topsecret

# ファイルとリテラル値を組み合わせて my-secret という名前のシークレットを新規作成する
oc create secret generic my-secret --from-file=ssh-privatekey=path/to/id_rsa --from-literal=passphrase=topsecret

# env ファイルから my-secret という名前のシークレットを新規作成する
oc create secret generic my-secret --from-env-file=path/to/foo.env --from-env-file=path/to/bar.env
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--append-hash=false`
  シークレットの名前に、その内容のハッシュを付加します。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--from-env-file=[]`
  シークレットを作成するために key=val のペアを読み込むファイルのパスを指定します。

- `--from-file=[]`
  キーとなるファイルは、パスだけを指定するとデフォルトの名前が付けられます。名前とパスを組み合わせて指定した場合は、指定した名前が使われます。ディレクトリを指定した場合は、有効なシークレットキーとなるディレクトリ内の各ファイルを処理します。

- `--from-literal=[]`
  シークレットに登録するキーとリテラル値を指定します（例: mykey=somevalue）

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--type=''`
  作成するシークレットのタイプ

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create secret generic --help` / `gen-oc-help.py` で生成</sub>
