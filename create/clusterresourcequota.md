# `oc create clusterresourcequota`

> クラスタリソースクォータを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `clusterresourcequota`

## Usage

```
oc create clusterresourcequota NAME --project-label-selector=key=value [--hard=RESOURCE=QUANTITY]... [flags] [options]
```

特定のリソースを制御するクラスタリソースクォータを作成します。

クラスタリソースクォータオブジェクトは、ラベルセレクターに基づいて複数のプロジェクトにまたがるクォータ制限を定義します。

エイリアス: clusterresourcequota, clusterquota

## Examples

```bash
# Pod 数を 10 に制限するクラスタリソースクォータを作成する
oc create clusterresourcequota limit-bob --project-annotation-selector=openshift.io/requester=user-bob --hard=pods=10
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--hard=[]`
  制限するリソース: RESOURCE=QUANTITY（例: pods=10）

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--project-annotation-selector=''`
  クラスタリソースクォータのプロジェクトアノテーションセレクター

- `--project-label-selector=''`
  クラスタリソースクォータのプロジェクトラベルセレクター

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create clusterresourcequota --help` / `gen-oc-help.py` で生成</sub>
