# `oc auth reconcile`

> RBAC のロール、ロールバインディング、クラスタロール、クラスタロールバインディングの各オブジェクトのルールを reconcile します

[`oc`](../oc.md) / [`oc auth`](../auth.md) / `reconcile`

## Usage

```
oc auth reconcile -f FILENAME [options]
```

存在しないオブジェクトは作成されます。namespace スコープのオブジェクトについては、必要であればそれを含む namespace も作成されます。

既存のロールは、入力オブジェクトに含まれる権限を含むように更新され、--remove-extra-permissions を指定した場合は余分な権限が削除されます。

既存のバインディングは、入力オブジェクトに含まれるサブジェクトを含むように更新され、--remove-extra-subjects を指定した場合は余分なサブジェクトが削除されます。

RBAC リソースについては、ルールとサブジェクトの意味を理解したうえでマージが行われるため、'apply' よりこちらが推奨されます。

## Examples

```bash
# ファイルから RBAC リソースを reconcile する
oc auth reconcile -f my-rbac-rules.yaml
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-f, --filename=[]`
  reconcile 対象のリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove-extra-permissions=false`
  true の場合、ロールに追加された余分な権限を削除します

- `--remove-extra-subjects=false`
  true の場合、ロールバインディングに追加された余分なサブジェクトを削除します

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc auth reconcile --help` / `gen-oc-help.py` で生成</sub>
