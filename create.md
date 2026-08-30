# `oc create`

> ファイルまたは標準入力からリソースを作成する

[`oc`](oc.md) / `create`

## Usage

```
oc create -f FILENAME [options]
```

JSON と YAML 形式を受け付けます。

## Subcommands

- [`build`](create/build.md) — 新しいビルドを作成する
- [`clusterresourcequota`](create/clusterresourcequota.md) — クラスタリソースクォータを作成する
- [`clusterrole`](create/clusterrole.md) — クラスタロールを作成する
- [`clusterrolebinding`](create/clusterrolebinding.md) — 特定のクラスタロールに対するクラスタロールバインディングを作成する
- [`configmap`](create/configmap.md) — ローカルのファイル、ディレクトリ、またはリテラル値から config map を作成する
- [`cronjob`](create/cronjob.md) — 指定した名前で cron job を作成する
- [`deployment`](create/deployment.md) — 指定した名前でデプロイメントを作成する
- [`deploymentconfig`](create/deploymentconfig.md) — 指定したイメージを使用するデプロイメント設定を、デフォルト設定で作成する
- [`identity`](create/identity.md) — identity を手動で作成する（自動作成が無効な場合のみ必要）
- [`imagestream`](create/imagestream.md) — 空のイメージストリームを新規作成する
- [`imagestreamtag`](create/imagestreamtag.md) — 新しいイメージストリームタグを作成する
- [`ingress`](create/ingress.md) — 指定した名前で Ingress を作成する
- [`job`](create/job.md) — 指定した名前でジョブを作成する
- [`namespace`](create/namespace.md) — 指定した名前で namespace を作成する
- [`poddisruptionbudget`](create/poddisruptionbudget.md) — 指定した名前で pod disruption budget を作成する
- [`priorityclass`](create/priorityclass.md) — 指定した名前で priority class を作成する
- [`quota`](create/quota.md) — 指定した名前でクォータを作成する
- [`role`](create/role.md) — ルールを 1 つだけ持つロールを作成する
- [`rolebinding`](create/rolebinding.md) — 特定のロールまたはクラスタロールに対するロールバインディングを作成する
- [`route`](create/route.md) — セキュアな Route を通じてコンテナを外部に公開する
- [`secret`](create/secret.md) — 指定したサブコマンドを使ってシークレットを作成する
- [`service`](create/service.md) — 指定したサブコマンドを使って Service を作成する
- [`serviceaccount`](create/serviceaccount.md) — 指定した名前でサービスアカウントを作成する
- [`token`](create/token.md) — サービスアカウントのトークンを要求する
- [`user`](create/user.md) — ユーザーを手動で作成する（自動作成が無効な場合のみ必要）
- [`useridentitymapping`](create/useridentitymapping.md) — identity をユーザーに手動でマッピングする

## Examples

```bash
# pod.json のデータを使って Pod を作成する
oc create -f ./pod.json

# 標準入力に渡した JSON を基に Pod を作成する
cat pod.json | oc create -f -

# registry.yaml のデータを JSON で編集し、編集後のデータでリソースを作成する
oc create -f registry.yaml --edit -o json
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--edit=false`
  作成前に API リソースを編集する

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの作成に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--raw=''`
  サーバーに POST する生の URI。kubeconfig ファイルで指定されたトランスポートを使用します。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--windows-line-endings=false`
  --edit=true の場合のみ意味を持ちます。デフォルトは、実行中のプラットフォームの標準的な改行コードです。

> 各コマンドの詳細については "oc create `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create --help` / `gen-oc-help.py` で生成</sub>
