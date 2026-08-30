# `oc adm taint`

> 1 つ以上のノードの taint を更新する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `taint`

## Usage

```
oc adm taint NODE NAME KEY_1=VAL_1:TAINT_EFFECT_1 ... KEY_N=VAL_N:TAINT_EFFECT_N [options]
```

- taint はキー・値・effect で構成されます。ここでは引数として key=value:effect の形式で指定します。
- キーは英字または数字で始まる必要があり、英字・数字・ハイフン・ドット・アンダースコアを最大 253 文字まで含められます。
- キーの先頭には、example.com/my-app のように DNS サブドメインのプレフィックスと 1 つの '/' を付けることもできます。
- 値は省略可能です。指定する場合は英字または数字で始まる必要があり、英字・数字・ハイフン・ドット・アンダースコアを最大 63 文字まで含められます。
- effect は NoSchedule、PreferNoSchedule、NoExecute のいずれかである必要があります。
- 現在、taint を適用できるのはノードに対してのみです。

## Examples

```bash
# ノード 'foo' を、キー 'dedicated'、値 'special-user'、effect 'NoSchedule' の taint で更新する
# 同じキーと effect の taint が既に存在する場合、その値は指定した値に置き換えられます
oc adm taint nodes foo dedicated=special-user:NoSchedule

# ノード 'foo' から、キー 'dedicated' かつ effect 'NoSchedule' の taint があれば削除する
oc adm taint nodes foo dedicated:NoSchedule-

# ノード 'foo' から、キーが 'dedicated' の taint をすべて削除する
oc adm taint nodes foo dedicated-

# myLabel=X というラベルを持つノードに、キー 'dedicated' の taint を追加する
oc adm taint node -l myLabel=X  dedicated=foo:PreferNoSchedule

# ノード 'foo' に、キー 'bar' で値なしの taint を追加する
oc adm taint nodes foo bar:NoSchedule
```

## Options

- `--all=false`
  クラスタ内のすべてのノードを選択する

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-taint'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--overwrite=false`
  true の場合、taint の上書きを許可します。そうでない場合、既存の taint を上書きする更新は拒否されます。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm taint --help` / `gen-oc-help.py` で生成</sub>
