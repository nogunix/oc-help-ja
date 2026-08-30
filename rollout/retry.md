# `oc rollout retry`

> 最後に失敗したロールアウトを再試行する

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `retry`

## Usage

```
oc rollout retry (TYPE NAME | TYPE/NAME) [flags] [options]
```

ロールアウトが失敗した場合、（一時的なエラーであれば）再試行することもできます。中には決して成功しないロールアウトもあり、その場合は rollout latest で再デプロイを強制できます。デプロイメント設定が過去に一度でもロールアウトを正常完了していれば、新たなロールアウトが失敗した際には自動的にロールバックされます。ただし、その内容をアプリケーションに残すには、問題のあるデプロイメント設定自体を修正する必要があります。

## Examples

```bash
# 'frontend' を基にした、最後に失敗したデプロイを再試行する
# 最後に失敗したデプロイについて、deployer Pod とすべてのフック Pod が削除されます
oc rollout retry dc/frontend
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollout retry --help` / `gen-oc-help.py` で生成</sub>
