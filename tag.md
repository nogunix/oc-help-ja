# `oc tag`

> 既存のイメージにタグを付けてイメージストリームに登録する

[`oc`](oc.md) / `tag`

## Usage

```
oc tag [--source=SOURCETYPE] SOURCE DEST [DEST ...] [flags] [options]
```

tag コマンドを使うと、イメージストリーム内の既存のタグやイメージ、あるいはコンテナイメージの pull spec を、1 つ以上の別のイメージストリームのタグにおける最新イメージとして設定できます。'docker tag' コマンドに似ていますが、こちらはイメージストリームに対して動作します。

外部レジストリが有効な HTTPS 証明書を持っていない場合や HTTP でのみ提供されている場合は、--insecure フラグを指定してください。--scheduled を指定すると、サーバーが定期的にタグの更新を確認し、最新バージョンをインポートします（それによってビルドやデプロイをトリガーできます）。なお --scheduled はコンテナイメージに対してのみ指定できます。

## Examples

```bash
# イメージストリーム 'openshift/ruby' の現在のイメージとタグ '2.0' を、イメージストリーム 'yourproject/ruby' のタグ 'tip' としてタグ付けする
oc tag openshift/ruby:2.0 yourproject/ruby:tip

# 特定のイメージにタグを付ける
oc tag openshift/ruby@sha256:6b646fa6bf5e5e4c7fa41056c27910e679c03ebe7f93e361e6515a9da7e258cc yourproject/ruby:tip

# 外部のコンテナイメージにタグを付ける
oc tag --source=docker openshift/origin-control-plane:latest yourproject/ruby:tip

# 外部のコンテナイメージにタグを付け、そのイメージの pullthrough を要求する
oc tag --source=docker openshift/origin-control-plane:latest yourproject/ruby:tip --reference-policy=local

# 外部のコンテナイメージにタグを付け、完全なマニフェストリストを含める
oc tag --source=docker openshift/origin-control-plane:latest yourproject/ruby:tip --import-mode=PreserveOriginal

# イメージストリームから、指定した spec タグを削除する
oc tag openshift/origin-control-plane:latest -d
```

## Options

- `--alias=false`
  ソースタグが変更されたときに、宛先タグも更新するかどうか。単一のイメージストリームにのみ適用されます。デフォルトは false です。

- `-d, --delete=false`
  指定した spec タグを削除します。

- `--import-mode=''`
  'PreserveOriginal' を指定した場合、タグの完全なマニフェストリストをインポートします。デフォルトは 'Legacy' です。

- `--insecure=false`
  指定したコンテナイメージのインポートに HTTP が必要な場合、または自己署名証明書を使用している場合に true を設定します。デフォルトは false です。

- `--reference=false`
  宛先タグが、引き続きソース側の namespace から pull するかどうか。デフォルトは false です。

- `--reference-policy='source'`
  'local' を指定した場合に、外部イメージの pullthrough を要求できるようにします。デフォルトは 'source' です。

- `--scheduled=false`
  リモートリポジトリからコンテナイメージを定期的にインポートするよう設定します。デフォルトは false です。

- `--source=''`
  ソースの種類に関する省略可能なヒント。有効な値は 'imagestreamtag'、'istag'、'imagestreamimage'、'isimage'、'docker' です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc tag --help` / `gen-oc-help.py` で生成</sub>
