# `oc replace`

> ファイル名または標準入力でリソースを置き換える

[`oc`](oc.md) / `replace`

## Usage

```
oc replace -f FILENAME [options]
```

JSON と YAML 形式を受け付けます。既存のリソースを置き換える場合は、リソースの spec 全体を指定する必要があります。これは次の方法で取得できます:

        $ oc get TYPE NAME -o yaml

## Examples

```bash
# pod.json のデータを使って Pod を置き換える
oc replace -f ./pod.json

# 標準入力に渡した JSON を基に Pod を置き換える
cat pod.json | oc replace -f -

# 単一コンテナの Pod のイメージバージョン（タグ）を v4 に更新する
oc get pod mypod -o yaml | sed 's/\(image: myimage\):.*$/\1:v4/' | oc replace -f -

# 強制的に置き換える（リソースを削除してから再作成する）
oc replace --force -f ./pod.json
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--cascade='background'`
  "background"、"orphan"、"foreground" のいずれかを指定します。従属リソース（ReplicationController が作成した Pod など）に対する削除のカスケード方式を選択します。デフォルトは background です。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-replace'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  置き換える設定が書かれたファイル。

- `--force=false`
  true の場合、正常な削除処理を行わず、API から直ちにリソースを削除します。リソースによっては即時削除により不整合やデータ損失が生じる可能性があり、確認が必要です。

- `--grace-period=-1`
  リソースの正常終了に与える猶予時間（秒）。負の値の場合は無視されます。即時シャットダウンするには 1 を指定します。0 を指定できるのは --force が true（強制削除）の場合のみです。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--raw=''`
  サーバーに PUT する生の URI。kubeconfig ファイルで指定されたトランスポートを使用します。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--subresource=''`
  指定した場合、replace は対象オブジェクトのサブリソースに対して動作します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--timeout=0s`
  削除を諦めるまでの待ち時間。0 の場合、オブジェクトのサイズからタイムアウトを決定します

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--wait=false`
  true の場合、リソースが消滅するまで待ってから終了します。finalizer の完了も待ちます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc replace --help` / `gen-oc-help.py` で生成</sub>
