# `oc apply`

> ファイル名または標準入力から、リソースに設定を適用する

[`oc`](oc.md) / `apply`

## Usage

```
oc apply (-f FILENAME | -k DIRECTORY) [options]
```

ファイル名または標準入力から、リソースに設定を適用します。リソース名の指定が必要です。リソースがまだ存在しない場合は作成されます。'apply' を使う場合は、最初のリソース作成も必ず 'apply' か 'create --save-config' で行ってください。

JSON と YAML 形式を受け付けます。

アルファ版に関する注意: --prune の機能はまだ完成していません。現在の状態を理解している場合を除き、使用しないでください。https://issues.k8s.io/34274 を参照してください。

## Subcommands

- [`edit-last-applied`](apply/edit-last-applied.md) — リソース / オブジェクトの最新の last-applied-configuration アノテーションを編集する
- [`set-last-applied`](apply/set-last-applied.md) — 稼働中のオブジェクトの last-applied-configuration アノテーションを、ファイルの内容に合わせて設定する
- [`view-last-applied`](apply/view-last-applied.md) — リソース / オブジェクトの最新の last-applied-configuration アノテーションを表示する

## Examples

```bash
# pod.json の設定を Pod に適用する
oc apply -f ./pod.json

# kustomization.yaml を含むディレクトリからリソースを適用する（例: dir/kustomization.yaml）
oc apply -k dir/

# 標準入力に渡した JSON を Pod に適用する
cat pod.json | oc apply -f -

# '.json' で終わるすべてのファイルから設定を適用する
oc apply -f '*.json'

# 注: --prune はまだアルファ版です
# ラベル app=nginx に一致する manifest.yaml の設定を適用し、ファイルに含まれずラベル app=nginx に一致する他のリソースをすべて削除する
oc apply --prune -f manifest.yaml -l app=nginx

# manifest.yaml の設定を適用し、ファイルに含まれていない他の config map をすべて削除する
oc apply --prune -f manifest.yaml --all --prune-allowlist=core/v1/ConfigMap
```

## Options

- `--all=false`
  指定したリソースタイプについて、namespace 内のすべてのリソースを選択します。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--cascade='background'`
  "background"、"orphan"、"foreground" のいずれかを指定します。従属リソース（ReplicationController が作成した Pod など）に対する削除のカスケード方式を選択します。デフォルトは background です。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-client-side-apply'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  適用する設定が書かれたファイル。

- `--force=false`
  true の場合、正常な削除処理を行わず、API から直ちにリソースを削除します。リソースによっては即時削除により不整合やデータ損失が生じる可能性があり、確認が必要です。

- `--force-conflicts=false`
  true の場合、サーバーサイド apply は競合があっても変更を強制適用します。

- `--grace-period=-1`
  リソースの正常終了に与える猶予時間（秒）。負の値の場合は無視されます。即時シャットダウンするには 1 を指定します。0 を指定できるのは --force が true（強制削除）の場合のみです。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--openapi-patch=true`
  true の場合、openapi が利用可能で、かつ対象リソースが openapi 仕様に見つかる場合は openapi を使って差分を計算します。それ以外の場合は、組み込みの型定義にフォールバックします。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--overwrite=true`
  変更後の設定の値を使って、変更後の設定と稼働中の設定の競合を自動的に解決します

- `--prune=false`
  設定ファイルに現れず、かつ apply または create --save-config で作成されたリソースオブジェクトを自動的に削除します。-l または --all と併用してください。

- `--prune-allowlist=[]`
  --prune のデフォルトの許可リストを <group/version/kind> で上書きします

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--server-side=false`
  true の場合、apply はクライアントではなくサーバー側で実行されます。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--subresource=''`
  指定した場合、apply は対象オブジェクトのサブリソースに対して動作します。--server-side を使用する場合にのみ指定できます。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--timeout=0s`
  削除を諦めるまでの待ち時間。0 の場合、オブジェクトのサイズからタイムアウトを決定します

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--wait=false`
  true の場合、リソースが消滅するまで待ってから終了します。finalizer の完了も待ちます。

> 各コマンドの詳細については "oc apply `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc apply --help` / `gen-oc-help.py` で生成</sub>
