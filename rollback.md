# `oc rollback`

> アプリケーションの一部を以前のデプロイに戻す

[`oc`](oc.md) / `rollback`

## Usage

```
oc rollback (DEPLOYMENTCONFIG | DEPLOYMENT) [flags] [options]
```

アプリケーションを以前のデプロイに戻します。

このコマンドを実行すると、デプロイメント設定が以前のデプロイの内容に合わせて更新されます。デフォルトでは Pod とコンテナの設定のみが変更され、スケーリングやトリガーの設定はそのまま維持されます。なお、環境変数とボリュームはロールバックの対象に含まれるため、最近セキュリティ資格情報を更新した場合、以前のデプロイの値が正しくない可能性があります。

ロールバックした設定に含まれるイメージトリガーは、警告とともに無効化されます。これは、ロールバック直後にトリガーによるデプロイでロールバック内容が置き換えられてしまうのを防ぐためです。トリガーを再度有効にするには 'set triggers' コマンドを使用します。

ロールバックの結果を先に確認したい場合は '--dry-run' を指定すると、ロールバックを実行せず、更新後のデプロイメント設定を人間が読める形で表示します。結果が予想しづらいときに便利です。

## Examples

```bash
# デプロイメント設定を、最後に正常完了したデプロイへロールバックする
oc rollback frontend

# バージョン 3 へのロールバックの結果を確認する。ロールバックは実行しない
oc rollback frontend --to-version=3 --dry-run

# 特定のデプロイへロールバックする
oc rollback frontend-2

# 新しい設定の JSON を oc にパイプで戻して、ロールバックを手動で実行する
oc rollback frontend -o json | oc replace dc/frontend -f -

# ロールバックを実行する代わりに、更新後のデプロイメント設定を JSON 形式で表示する
oc rollback frontend -o json
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--change-scaling-settings=false`
  true の場合、以前のデプロイの replicationController のレプリカ数とセレクターもロールバックに含めます

- `--change-strategy=false`
  true の場合、以前のデプロイのストラテジーもロールバックに含めます

- `--change-triggers=false`
  true の場合、以前のデプロイのトリガーもロールバックに含めます

- `-d, --dry-run=false`
  ロールバックを実行する代わりに、ロールバック後の状態を人間が読める形で表示します

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--to-version=0`
  ロールバック先の設定バージョン。バージョン 0 の指定はバージョンを省略した場合と同じです（バージョンは自動検出されます）。デプロイメントを指定した場合、このオプションは無視されます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollback --help` / `gen-oc-help.py` で生成</sub>
