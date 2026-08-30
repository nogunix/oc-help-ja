# `oc create configmap`

> ローカルのファイル、ディレクトリ、またはリテラル値から config map を作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `configmap`

## Usage

```
oc create configmap NAME [--from-file=[key=]source] [--from-literal=key1=value1] [--dry-run=server|client|none] [options]
```

ファイル、ディレクトリ、または指定したリテラル値から config map を作成します。

1 つの config map に、1 つ以上のキー / 値のペアをまとめられます。

ファイルを基に config map を作成する場合、キーはデフォルトでそのファイルの basename、値はデフォルトでファイルの内容になります。basename が無効なキーの場合は、別のキーを指定できます。

ディレクトリを基に config map を作成する場合、ディレクトリ内で basename が有効なキーとなる各ファイルが config map にまとめられます。通常のファイル以外のディレクトリエントリ（サブディレクトリ、シンボリックリンク、デバイス、パイプなど）は無視されます。

エイリアス: configmap, cm

## Examples

```bash
# フォルダ bar を基に my-config という名前の config map を新規作成する
oc create configmap my-config --from-file=path/to/bar

# ディスク上のファイル名ではなく、指定したキーを使って my-config という名前の config map を新規作成する
oc create configmap my-config --from-file=key1=/path/to/bar/file1.txt --from-file=key2=/path/to/bar/file2.txt

# key1=config1 と key2=config2 を持つ my-config という名前の config map を新規作成する
oc create configmap my-config --from-literal=key1=config1 --from-literal=key2=config2

# ファイル内の key=value のペアから my-config という名前の config map を新規作成する
oc create configmap my-config --from-file=path/to/bar

# env ファイルから my-config という名前の config map を新規作成する
oc create configmap my-config --from-env-file=path/to/foo.env --from-env-file=path/to/bar.env
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--append-hash=false`
  config map の名前に、その内容のハッシュを付加します。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--from-env-file=[]`
  configmap を作成するために key=val のペアを読み込むファイルのパスを指定します。

- `--from-file=[]`
  キーとなるファイルは、パスだけを指定するとファイルの basename が configmap のキーになります。キーとパスを組み合わせて指定した場合は、指定したキーが使われます。ディレクトリを指定した場合は、basename が有効な configmap キーとなるディレクトリ内の各ファイルを処理します。

- `--from-literal=[]`
  configmap に登録するキーとリテラル値を指定します（例: mykey=somevalue）

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

<sub>`$ oc create configmap --help` / `gen-oc-help.py` で生成</sub>
