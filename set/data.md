# `oc set data`

> config map またはシークレット内のデータを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `data`

## Usage

```
oc set data RESOURCE/NAME [KEY=VALUE|KEY- ...] [--from-file=file|dir|key=path] [flags] [options]
```

シークレットと config map のデータキーを追加・更新・削除します。

シークレットと config map を使うと、Pod に渡したり他の Kubernetes リソースから読み込んだりできるキーと値を保存できます。このコマンドでは、引数やファイルからそれらのオブジェクトのキーを設定・削除できます。ファイルやディレクトリの内容を読み込むには --from-file フラグを使い、値を設定するには KEY=VALUE、キーを削除するには KEY- の形式でコマンドライン引数を渡します。

--local と --dry-run フラグを使って、サーバーに送信する前にオブジェクトを変更する一連の処理の一部として、このコマンドを使うこともできます。これにより、ローカルのリソースにキーを追加できます。

## Examples

```bash
# シークレットのキー 'password' を設定する
oc set data secret/foo password=this_is_secret

# シークレットからキー 'password' を削除する
oc set data secret/foo password-

# ディスク上のファイルから config map のキー 'haproxy.conf' を更新する
oc set data configmap/bar --from-file=../haproxy.conf

# ディレクトリの内容でシークレットを更新する（ファイルごとに 1 つのキー）
oc set data secret/foo --from-file=secret-dir
```

## Options

- `--all=false`
  true の場合、指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `--from-file=[]`
  ファイルは、パスだけを指定するとファイルの basename がキーになります。キーとパスを組み合わせて指定した場合は、指定したキーが使われます。ディレクトリを指定した場合は、basename が有効なシークレットキーとなるディレクトリ内の各ファイルを処理します。

- `--from-literal=[]`
  設定するキーとリテラル値を指定します（例: mykey=somevalue）

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set data --help` / `gen-oc-help.py` で生成</sub>
