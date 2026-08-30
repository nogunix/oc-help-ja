# `oc create priorityclass`

> 指定した名前で priority class を作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `priorityclass`

## Usage

```
oc create priorityclass NAME --value=VALUE --global-default=BOOL [--dry-run=server|client|none] [options]
```

指定した名前・値・globalDefault・説明で priority class を作成します。

エイリアス: priorityclass, pc

## Examples

```bash
# high-priority という名前の priority class を作成する
oc create priorityclass high-priority --value=1000 --description="high priority"

# グローバルなデフォルト優先度として扱われる default-priority という名前の priority class を作成する
oc create priorityclass default-priority --value=1000 --global-default=true --description="default priority"

# 優先度の低い Pod をプリエンプトできない high-priority という名前の priority class を作成する
oc create priorityclass high-priority --value=1000 --description="high priority" --preemption-policy="Never"
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--description=''`
  description は任意の文字列で、通常はこの priority class をどのような場合に使うべきかの指針を記述します。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--global-default=false`
  global-default は、この PriorityClass をデフォルトの優先度とみなすかどうかを指定します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--preemption-policy='PreemptLowerPriority'`
  preemption-policy は、優先度の低い Pod をプリエンプトする際のポリシーです。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--value=0`
  この priority class の値。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create priorityclass --help` / `gen-oc-help.py` で生成</sub>
