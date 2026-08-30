# `oc config view`

> マージ済みの kubeconfig 設定、または指定した kubeconfig ファイルを表示する

[`oc`](../oc.md) / [`oc config`](../config.md) / `view`

## Usage

```
oc config view [flags] [options]
```

--output jsonpath={...} を使うと、jsonpath 式で特定の値を抽出できます。

## Examples

```bash
# マージ済みの kubeconfig 設定を表示する
oc config view

# マージ済みの kubeconfig 設定、生の証明書データ、および露出したシークレットを表示する
oc config view --raw

# e2e ユーザーのパスワードを取得する
oc config view -o jsonpath='{.users[?(@.name == "e2e")].user.password}'
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--flatten=false`
  生成される kubeconfig ファイルを、自己完結した内容にフラット化します（可搬性のある kubeconfig ファイルの作成に便利です）

- `--merge=true`
  kubeconfig ファイルの階層全体をマージする

- `--minify=false`
  current-context で使用していない情報を、出力からすべて削除します

- `-o, --output='yaml'`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--raw=false`
  生のバイトデータと機密データを表示します

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config view --help` / `gen-oc-help.py` で生成</sub>
