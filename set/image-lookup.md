# `oc set image-lookup`

> アプリケーションのデプロイ時にイメージをどう解決するかを変更する

[`oc`](../oc.md) / [`oc set`](../set.md) / `image-lookup`

## Usage

```
oc set image-lookup STREAMNAME [...] [flags] [options]
```

Pod やその他のオブジェクトからイメージストリームを使用する。

イメージストリームを使うと、イメージへのタグ付け、他のレジストリの変更追跡、イメージへのアクセス制御の一元化が簡単になります。ローカル名前解決を使うと、レジストリの完全な URL を指定しなくても、Pod・デプロイメント・レプリカセットなどイメージを参照するリソースのイメージ供給元としてイメージストリームを使えます。'mysql' という名前のイメージストリームでローカル名前解決が有効な場合、'mysql:latest'（または任意のタグ）を参照する Pod などのリソースは、上流のレジストリではなく、そのイメージストリームタグが指す場所から pull します。

ローカル名前解決を有効にしたら、オブジェクトの image フィールドでそのイメージストリームタグを参照するだけで済みます。例:

        $ oc import-image mysql:latest --confirm
        $ oc set image-lookup mysql
        $ oc run mysql --image=mysql
DockerHub から最新の MySQL イメージをインポートし、そのイメージストリームがプロジェクト内で "mysql" という名前を扱うように設定したうえで、インポートしたイメージを指すデプロイを起動します。

このコマンドで、あるリソース上のすべてのイメージについてイメージ解決を強制することもできます。オブジェクトにアノテーションが付与され、イメージストリーム側で lookup が有効かどうかに関係なく、一致するすべてのイメージについて現在の namespace のイメージストリームタグが参照されるようになります。

        $ oc run mysql --image=myregistry:5000/test/mysql:v1
        $ oc tag --source=docker myregistry:5000/test/mysql:v1 mysql:v1
        $ oc set image-lookup deploy/mysql
これにより、インポートされた mysql:v1 タグを指すデプロイがトリガーされるはずです。

## Examples

```bash
# すべてのイメージストリームと、それがローカル名を解決するかどうかを表示する
oc set image-lookup

# イメージストリーム mysql でローカル名前解決を使う
oc set image-lookup mysql

# ローカル名前解決を使うようデプロイメントに強制する
oc set image-lookup deploy/mysql

# デプロイメントのイメージ解決設定の現在の状態を表示する
oc set image-lookup deploy/mysql --list

# イメージストリーム mysql のローカル名前解決を無効にする
oc set image-lookup mysql --enabled=false

# すべてのイメージストリームでローカル名前解決を有効にする
oc set image-lookup --all
```

## Options

- `--all=false`
  true の場合、指定したリソースタイプについて、namespace 内のすべてのリソースを選択します。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--enabled=true`
  この namespace 内でタグ付きイメージを解決するよう、イメージストリームに印を付けます。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--list=false`
  指定したリソースの現在の状態を表示します。

- `--local=false`
  true の場合、操作はローカルで実行されます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set image-lookup --help` / `gen-oc-help.py` で生成</sub>
