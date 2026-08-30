# `oc create deployment`

> 指定した名前でデプロイメントを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `deployment`

## Usage

```
oc create deployment NAME --image=image -- [COMMAND] [args...] [options]
```

エイリアス: deployment, deploy

## Examples

```bash
# busybox イメージを実行する my-dep という名前のデプロイメントを作成する
oc create deployment my-dep --image=busybox

# コマンドを指定してデプロイメントを作成する
oc create deployment my-dep --image=busybox -- date

# nginx イメージをレプリカ 3 で実行する my-dep という名前のデプロイメントを作成する
oc create deployment my-dep --image=nginx --replicas=3

# busybox イメージを実行し、ポート 5701 を公開する my-dep という名前のデプロイメントを作成する
oc create deployment my-dep --image=busybox --port=5701

# 複数のコンテナを実行する my-dep という名前のデプロイメントを作成する
oc create deployment my-dep --image=busybox:latest --image=ubuntu:latest --image=nginx
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--image=[]`
  実行するイメージ名。マルチコンテナ Pod にするため、1 つのデプロイメントに複数のイメージを設定できます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--port=-1`
  このデプロイメントが公開する containerPort。

- `-r, --replicas=1`
  作成するレプリカ数。デフォルトは 1 です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create deployment --help` / `gen-oc-help.py` で生成</sub>
