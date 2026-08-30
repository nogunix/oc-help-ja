# `oc create imagestreamtag`

> 新しいイメージストリームタグを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `imagestreamtag`

## Usage

```
oc create imagestreamtag NAME [flags] [options]
```

イメージストリームタグを使うと、他のレジストリのイメージを追跡・タグ付け・インポートできます。また、イメージを push できる、アクセス制御された宛先も定義します。1 つのイメージストリームタグは多数の異なるレジストリのイメージを参照でき、それらのイメージが Pod・デプロイメント・ビルドからどう参照されるかを制御できます。

--resolve-local を指定すると、Pod が名前でイメージを参照した際に、そのイメージストリームがソースとして使用されます。たとえばストリーム 'mysql' がローカル名を解決する設定になっている場合、'mysql:latest' を指す Pod は、そのイメージストリームの "latest" タグが指すイメージを使用します。

エイリアス: imagestreamtag, istag

## Examples

```bash
# リモートレジストリのイメージを基に、新しいイメージストリームタグを作成する
oc create imagestreamtag mysql:latest --from-image=myregistry.local/mysql/mysql:5.0
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-A, --annotation=[]`
  このイメージストリームタグにアノテーションを設定します。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--from=''`
  指定したイメージストリームタグまたはイメージストリームイメージをソースとして使用します: [`<namespace>`/]name[:`<tag>`|@`<id>`]

- `--from-image=''`
  指定したリモートイメージを、このタグで使用します。

- `--insecure=false`
  HTTPS で完全に保護されていないレジストリからのインポートを許可します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--reference=false`
  true の場合、そのイメージストリームタグが参照されるたびに、タグの値が使用されます。

- `--reference-policy=''`
  'Local' に設定した場合、参照されるイメージは統合レジストリから pull されます。reference が true の場合は無視されます。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--scheduled=false`
  設定した場合、このイメージのリモート側のソースを定期的にチェックしてインポートします。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create imagestreamtag --help` / `gen-oc-help.py` で生成</sub>
