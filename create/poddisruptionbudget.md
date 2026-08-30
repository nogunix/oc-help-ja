# `oc create poddisruptionbudget`

> 指定した名前で pod disruption budget を作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `poddisruptionbudget`

## Usage

```
oc create poddisruptionbudget NAME --selector=SELECTOR --min-available=N [--dry-run=server|client|none] [options]
```

指定した名前・セレクター・必要な最小利用可能 Pod 数で pod disruption budget を作成します。

エイリアス: poddisruptionbudget, pdb

## Examples

```bash
# app=rails ラベルを持つすべての Pod を選択する my-pdb という名前の pod disruption budget を作成する
# 常に少なくとも 1 つが利用可能であることを要求する
oc create poddisruptionbudget my-pdb --selector=app=rails --min-available=1

# app=nginx ラベルを持つすべての Pod を選択する my-pdb という名前の pod disruption budget を作成する
# 選択された Pod のうち、常に少なくとも半数が利用可能であることを要求する
oc create pdb my-pdb --selector=app=nginx --min-available=50%
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--max-unavailable=''`
  この budget が要求する、利用不可能な Pod の最大数または最大割合。

- `--min-available=''`
  この budget が要求する、利用可能な Pod の最小数または最小割合。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--selector=''`
  この budget に使用するラベルセレクター。等価ベースのセレクター要件のみサポートされます。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create poddisruptionbudget --help` / `gen-oc-help.py` で生成</sub>
