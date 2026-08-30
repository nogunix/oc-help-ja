# `oc rollout cancel`

> 進行中のデプロイをキャンセルする

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `cancel`

## Usage

```
oc rollout cancel (TYPE NAME | TYPE/NAME) [flags] [options]
```

このコマンドを実行すると、進行中のデプロイがキャンセルされます。ただしこれはベストエフォートの操作であり、完了までに時間がかかる場合があります。キャンセルが効く前に、デプロイが部分的または完全に完了してしまうこともあります。その場合は、それを示すイベントが発行されます。

## Examples

```bash
# 'nginx' を基にした進行中のデプロイをキャンセルする
oc rollout cancel dc/nginx
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

<sub>`$ oc rollout cancel --help` / `gen-oc-help.py` で生成</sub>
