# `oc set build-secret`

> ビルド設定のビルドシークレットを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `build-secret`

## Usage

```
oc set build-secret BUILDCONFIG SECRETNAME [flags] [options]
```

ビルド設定のビルドシークレットを設定または削除します。

ビルド設定は、プライベートレジストリとのイメージの push / pull や、プライベートなソースリポジトリへのアクセスのために、シークレットを参照できます。

設定するシークレットの種類を --push、--pull、--source のいずれかのフラグで指定します。シークレットの参照は --remove フラグで削除できます。

--selector フラグでラベルセレクターを指定して、シークレットを設定または削除する対象のビルド設定を選択できます。あるいは --all フラグで namespace 内のすべてのビルド設定を選択できます。

## Examples

```bash
# ビルド設定の push シークレットを削除する
oc set build-secret --push --remove bc/mybuild

# ビルド設定に pull シークレットを設定する
oc set build-secret --pull bc/mybuild mysecret

# ビルド設定に push シークレットと pull シークレットを設定する
oc set build-secret --push --pull bc/mybuild mysecret

# セレクターに一致する一連のビルド設定に、source シークレットを設定する
oc set build-secret --source -l app=myapp gitsecret
```

## Options

- `--all=false`
  true の場合、namespace 内のすべてのビルド設定を選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set build-secret は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--pull=false`
  true の場合、ビルド設定に pull シークレットを設定します

- `--push=false`
  true の場合、ビルド設定に push シークレットを設定します

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove=false`
  true の場合、ビルドシークレットを削除します。

- `-l, --selector=''`
  ビルド設定を絞り込むためのセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--source=false`
  true の場合、ビルド設定に source シークレットを設定します

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set build-secret --help` / `gen-oc-help.py` で生成</sub>
