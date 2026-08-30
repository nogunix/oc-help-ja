# `oc edit`

> サーバー上のリソースを編集する

[`oc`](oc.md) / `edit`

## Usage

```
oc edit (RESOURCE/NAME | -f FILENAME) [options]
```

デフォルトのエディタでリソースを編集します。

edit コマンドを使うと、コマンドラインツールで取得できる任意の API リソースを直接編集できます。環境変数 KUBE_EDITOR または EDITOR で定義されたエディタが開き、いずれも未設定の場合は Linux なら 'vi'、Windows なら 'notepad' が使われます。エディタを開く際は、まず環境変数 'SHELL' で定義されたシェルを使おうとします。未定義の場合は、Linux なら '/bin/bash'、Windows なら 'cmd' というデフォルトのシェルが使われます。

複数のオブジェクトを編集できますが、変更は 1 つずつ適用されます。ファイル名もコマンドライン引数として受け付けますが、指定するファイルは、以前に保存されたリソースの内容である必要があります。

編集は、リソースの取得に使われた API バージョンで行われます。特定の API バージョンで編集するには、リソース・バージョン・グループを完全修飾で指定してください。

デフォルトの形式は YAML です。JSON で編集するには "-o json" を指定します。

--windows-line-endings フラグで Windows の改行コードを強制できます。指定しない場合は、お使いの OS のデフォルトが使用されます。

更新中にエラーが発生した場合、未適用の変更内容を含む一時ファイルがディスク上に作成されます。リソース更新時に最もよくあるエラーは、別のエディタがサーバー上のそのリソースを変更していた場合です。その場合は、新しいバージョンのリソースに対して変更を適用し直すか、一時保存されたコピーを最新のリソースバージョンに合わせて更新する必要があります。

## Examples

```bash
# 'registry' という名前の Service を編集する
oc edit svc/registry

# 別のエディタを使う
KUBE_EDITOR="nano" oc edit svc/registry

# v1 API 形式を使い、ジョブ 'myjob' を JSON で編集する
oc edit job.v1.batch/myjob -o json

# デプロイメント 'mydeployment' を YAML で編集し、変更後の設定をそのアノテーションに保存する
oc edit deployment/mydeployment -o yaml --save-config

# デプロイメント 'mydeployment' の 'status' サブリソースを編集する
oc edit deployment mydeployment --subresource='status'
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--field-manager='kubectl-edit'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--output-patch=false`
  リソースを編集した場合、そのパッチを出力します。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--subresource=''`
  指定した場合、edit は対象オブジェクトのサブリソースに対して動作します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

- `--windows-line-endings=false`
  デフォルトは、実行中のプラットフォームの標準的な改行コードです。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc edit --help` / `gen-oc-help.py` で生成</sub>
