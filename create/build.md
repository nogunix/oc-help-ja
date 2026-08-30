# `oc create build`

> 新しいビルドを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `build`

## Usage

```
oc create build NAME [flags] [options]
```

ビルドは、ソースコードまたは Dockerfile からコンテナイメージを作成します。ビルドは Git からソースコードを取得することも、ソースを取得する Dockerfile を受け取ることもできます。

## Examples

```bash
# 新しいビルドを作成する
oc create build myapp
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--build-loglevel=0`
  ビルドのログレベルを設定します (0-10、デフォルトは 0)。

- `--context-dir=''`
  ビルドのルートとして使用する、リポジトリ内の相対パス。

- `--dockerfile-contents=''`
  ビルドする Dockerfile の内容。

- `--dockerfile-path=''`
  リポジトリのコンテキスト内で、Dockerfile が置かれている相対パス。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--env=[]`
  ビルドストラテジーに環境変数を追加します。

- `--from-image=''`
  イメージビルドのベースとして使用するコンテナイメージの pull spec。

- `--image-optimization-policy=''`
  個々のレイヤーを作成するかどうかを制御します。SkipLayers、SkipLayersAndWarn、None のいずれかです。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--source-git=''`
  Git リポジトリの URL または Git spec リンク。

- `--source-revision=''`
  ソースリポジトリ内のコミット、ブランチ、またはタグ。

- `--strategy=''`
  使用するビルドストラテジー: Docker、Source、Custom のいずれか。他の引数から自動的に決まる場合もあります。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--to-image=''`
  出力イメージの push 先。

- `--to-image-stream=''`
  出力イメージの push 先となるイメージストリームタグ。[NAMESPACE/]STREAM:TAG の形式を受け付けます

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create build --help` / `gen-oc-help.py` で生成</sub>
