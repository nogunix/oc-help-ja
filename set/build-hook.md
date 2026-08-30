# `oc set build-hook`

> ビルド設定のビルドフックを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `build-hook`

## Usage

```
oc set build-hook BUILDCONFIG --post-commit [--command] [--script] -- CMD [flags] [options]
```

ビルド設定のビルドフックを設定または削除します。

ビルドフックを使うと、ビルド処理に独自の動作を差し込めます。

post-commit ビルドフックは、ビルドがイメージをコミットした後、そのイメージがレジストリに push される前に実行されます。レジストリで利用可能になる前にイメージ上でテストを実行して検証したり、push 前に実行しておきたい任意の処理に使用できます。ビルドフックのコマンドは、ビルドされたばかりのイメージから起動した新しいコンテナ内で実行されます。ビルドフックが実行するコマンドやスクリプトが 0 以外の終了コードを返した場合、そのイメージはレジストリに push されません。

ビルドフックのコマンドは、シェルスクリプトとして（--script 引数）、イメージの新しいエントリポイントコマンドとして（--command 引数）、またはイメージのエントリポイントへの引数の並びとして（デフォルト）指定できます。

## Examples

```bash
# ビルド設定の post-commit フックを削除する
oc set build-hook bc/mybuild --post-commit --remove

# 新しいエントリポイントでテストスイートを実行する post-commit フックを設定する
oc set build-hook bc/mybuild --post-commit --command -- /bin/bash -c /var/lib/test-image.sh

# シェルスクリプトを実行する post-commit フックを設定する
oc set build-hook bc/mybuild --post-commit --script="/var/lib/test-image.sh param1 param2 && /var/lib/done.sh"
```

## Options

- `--all=false`
  true の場合、namespace 内のすべてのビルド設定を選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--command=false`
  true の場合、フック用コンテナのエントリポイントを、指定したコマンドに設定します

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--post-commit=false`
  true の場合、ビルド設定に post-commit ビルドフックを設定します

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove=false`
  true の場合、ビルドフックを削除します。

- `--script=''`
  build-hook で実行するスクリプトを指定する

- `-l, --selector=''`
  ビルド設定を絞り込むためのセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set build-hook --help` / `gen-oc-help.py` で生成</sub>
