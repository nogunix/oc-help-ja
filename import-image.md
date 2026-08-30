# `oc import-image`

> コンテナイメージレジストリからイメージをインポートする

[`oc`](oc.md) / `import-image`

## Usage

```
oc import-image IMAGESTREAM[:TAG] [flags] [options]
```

コンテナイメージレジストリ内のタグから、最新のイメージ情報をインポートします。

イメージストリームを使うと、ビルドやアプリケーションにどのイメージを展開するかを制御できます。このコマンドは、リモートリポジトリからイメージの最新バージョンを取得し、以前の値と異なる場合にイメージストリームタグを更新します。複数回実行しても重複したエントリは作成されません。イメージのインポートでは、イメージのメタデータのみがコピーされ、イメージの中身はコピーされません。

イメージストリームタグを変更したい場合や、より高度なオプションを使いたい場合は 'tag' コマンドを参照してください。

## Examples

```bash
# latest タグを新しいイメージストリームにインポートする
oc import-image mystream --from=registry.io/repo/image:latest --confirm

# 既存のイメージストリームの latest タグについて、インポート済みデータを更新する
oc import-image mystream

# 既存のイメージストリームの stable タグについて、インポート済みデータを更新する
oc import-image mystream:stable

# 既存のイメージストリームのすべてのタグについて、インポート済みデータを更新する
oc import-image mystream --all

# マニフェストリストを指すタグについて、完全なマニフェストリストを含むようインポート済みデータを更新する
oc import-image mystream --import-mode=PreserveOriginal

# すべてのタグを新しいイメージストリームにインポートする
oc import-image mystream --from=registry.io/repo/image --all --confirm

# カスタムのタイムアウトを指定して、すべてのタグを新しいイメージストリームにインポートする
oc --request-timeout=5m import-image mystream --from=registry.io/repo/image --all --confirm
```

## Options

- `--all=false`
  true の場合、作成時、または --from を指定した場合に、指定したソースからすべてのタグをインポートします

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--confirm=false`
  true の場合、イメージストリームのインポート元の設定・変更を許可します

- `--dry-run=false`
  イメージストリームを作成・更新することなく、イメージの情報を取得します。

- `--from=''`
  イメージのインポート元となるコンテナイメージリポジトリ

- `--import-mode='Legacy'`
  'PreserveOriginal' を指定した場合、タグの完全なマニフェストリストをインポートします。デフォルトは 'Legacy' です。

- `--insecure=false`
  true の場合、無効な HTTPS 証明書を持つ、または HTTP でホストされているレジストリからのインポートを許可します。このフラグは insecure アノテーションより優先されます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--reference-policy='source'`
  'local' を指定した場合に、外部イメージの pullthrough を要求できるようにします。デフォルトは 'source' です。

- `--scheduled=false`
  インポートした各コンテナイメージを、リモートリポジトリから定期的にインポートするよう設定します。デフォルトは false です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc import-image --help` / `gen-oc-help.py` で生成</sub>
