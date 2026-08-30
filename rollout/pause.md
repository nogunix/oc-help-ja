# `oc rollout pause`

> 指定したリソースを一時停止状態にする

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `pause`

## Usage

```
oc rollout pause RESOURCE [options]
```

一時停止中のリソースは、コントローラーによる調整（reconcile）が行われません。一時停止したリソースを再開するには "oc rollout resume" を使用します。現在、一時停止に対応しているのはデプロイメントのみです。

## Examples

```bash
# nginx デプロイメントを一時停止状態にする
# デプロイメントの現在の状態はそのまま機能し続けます。新しい更新は
# デプロイメントが一時停止している間は、そのデプロイメントへの変更は反映されません
oc rollout pause deployment/nginx
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--field-manager='kubectl-rollout'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollout pause --help` / `gen-oc-help.py` で生成</sub>
