# `oc events`

> イベントを一覧する

[`oc`](oc.md) / `events`

## Usage

```
oc events [(-o|--output=)json|yaml|kyaml|name|go-template|go-template-file|template|templatefile|jsonpath|jsonpath-as-json|jsonpath-file] [--for TYPE/NAME] [--watch] [--types=Normal,Warning] [options]
```

イベントを表示します。

イベントに関する重要な情報を表形式で表示します。イベントは、特定の namespace、すべての namespace、または指定したリソースに関するものだけに絞り込んで取得できます。

## Examples

```bash
# default namespace の最近のイベントを一覧する
oc events

# すべての namespace の最近のイベントを一覧する
oc events --all-namespaces

# 指定した Pod の最近のイベントを一覧し、その後も新しいイベントを待って順に表示する
oc events --for pod/web-pod-13je7 --watch

# 最近のイベントを YAML 形式で一覧する
oc events -oyaml

# タイプが 'Warning' または 'Normal' の最近のイベントのみを一覧する
oc events --types=Warning,Normal
```

## Options

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--chunk-size=500`
  大きなリストを一度に返さず、チャンクに分けて返します。0 を指定すると無効になります。

- `--for=''`
  指定したリソースに関連するイベントのみに絞り込みます。

- `--no-headers=false`
  デフォルトの出力形式を使う場合に、ヘッダーを表示しません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--types=[]`
  指定したタイプのイベントのみを出力します。

- `-w, --watch=false`
  指定したイベントを一覧表示した後、以降のイベントを監視し続けます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc events --help` / `gen-oc-help.py` で生成</sub>
