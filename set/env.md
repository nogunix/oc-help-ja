# `oc set env`

> Pod テンプレートの環境変数を更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `env`

## Usage

```
oc set env RESOURCE/NAME KEY_1=VAL_1 ... KEY_N=VAL_N [flags] [options]
```

Pod テンプレートまたはビルド設定の環境変数を更新します。

1 つ以上の Pod、Pod テンプレート、またはビルド設定に定義された環境変数を一覧表示します。1 つ以上の Pod テンプレート（レプリケーションコントローラーやデプロイメント設定の内部）またはビルド設定について、コンテナの環境変数定義を追加・更新・削除します。指定した Pod や Pod テンプレートのすべてのコンテナ、またはワイルドカードに一致するコンテナの環境変数定義を表示・変更できます。

"--env -" を指定した場合、標準入力から標準的な env 構文で環境変数を読み込めます。

## Examples

```bash
# デプロイメント設定 'myapp' に新しい環境変数を設定して更新する
oc set env dc/myapp STORAGE_DIR=/local

# ビルド設定 'sample-build' に定義された環境変数を一覧する
oc set env bc/sample-build --list

# すべての Pod に定義された環境変数を一覧する
oc set env pods --all --list

# 変更後のビルド設定を YAML で出力する
oc set env bc/sample-build STORAGE_DIR=/data -o yaml

# プロジェクト内のすべてのレプリケーションコントローラーの全コンテナに ENV=prod を設定する
oc set env rc --all ENV=prod

# シークレットから環境変数をインポートする
oc set env --from=secret/mysecret dc/myapp

# config map から、プレフィックスを付けて環境変数をインポートする
oc set env --from=configmap/myconfigmap --prefix=MYSQL_ dc/myapp

# すべてのデプロイメント設定について、コンテナ 'c1' から環境変数 ENV を削除する
oc set env dc --all --containers="c1" ENV-

# ディスク上のデプロイメント設定の定義から環境変数 ENV を削除し、
# サーバー上のデプロイメント設定を更新する
oc set env -f dc.json ENV-

# ローカルシェルの環境変数の一部を、サーバー上のデプロイメント設定に設定する
oc set env | grep RAILS_ | oc env -e - dc/myapp
```

## Options

- `--all=false`
  true の場合、指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-c, --containers='*'`
  変更対象とする、選択した Pod テンプレート内のコンテナ名。ワイルドカードを使用できます

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-e, --env=[]`
  各コンテナに設定する環境変数を、キーと値のペアで指定します。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `--from=''`
  環境変数の注入元となるリソースの名前

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--list=false`
  true の場合、環境変数とその変更を標準的な形式で表示します

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--overwrite=true`
  true の場合、環境変数の上書きを許可します。そうでない場合、既存の環境変数を上書きする更新は拒否されます。

- `--prefix=''`
  変数名に付けるプレフィックス

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--resolve=false`
  true の場合、変数を一覧する際にシークレットや configmap への参照も表示します

- `--resource-version=''`
  空でない場合、これがそのオブジェクトの現在の resource-version と一致するときにのみ、ラベルの更新が成功します。単一のリソースを指定した場合のみ有効です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set env --help` / `gen-oc-help.py` で生成</sub>
