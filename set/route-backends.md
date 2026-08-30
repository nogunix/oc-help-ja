# `oc set route-backends`

> ルートのバックエンドを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `route-backends`

## Usage

```
oc set route-backends ROUTENAME [--zero|--equal] [--adjust] SERVICE=WEIGHT[%] [...] [flags] [options]
```

ルートのバックエンドを設定・調整します。

ルートは 1 つ以上のバックエンド Service を持つことができ、各 Service にどれだけトラフィックを流すかは重みで制御します。トラフィックは、各バックエンドの重みの合計に比例して割り当てられます。重み 0 のバックエンドにはトラフィックが流れません。すべての重みが 0 の場合、そのルートはどのバックエンドにもトラフィックを送りません。

バックエンドを設定する際、最初のバックエンドがプライマリとなり、それ以外は代替とみなされます。例:

        $ oc set route-backends web prod=99 canary=1
プライマリのバックエンドを重み 99 の Service "prod" に、最初の代替バックエンドを重み 1 の Service "canary" に設定します。つまり、トラフィックの 99%% が Service "prod" に送られます。

--adjust フラグを使うと、個々の Service の重みを、その Service 自身またはプライマリのバックエンドに対する相対値で変更できます。パーセンテージを指定した場合、プライマリ（プライマリを指定した場合は最初の代替）を基準にバックエンドが調整されます。他のバックエンドがある場合、その重みは変更後の値に比例して保たれます。

すべてのルーターが複数バックエンドや重み付けバックエンドに対応しているわけではありません。

## Examples

```bash
# ルート 'web' のバックエンドを表示する
oc set route-backends web

# ルート 'web' に 2 つのバックエンド Service を設定し、トラフィックの 2/3 を 'a' に流す
oc set route-backends web a=2 b=1

# b に流すトラフィックの割合を、a に対する相対値で 10%% 増やす
oc set route-backends web --adjust b=+10%%

# b に流すトラフィックの割合を、a に流れるトラフィックの 10%% に設定する
oc set route-backends web --adjust b=10%%

# b の重みを 10 に設定する
oc set route-backends web --adjust b=10

# すべてのバックエンドの重みを 0 に設定する
oc set route-backends web --zero
```

## Options

- `--adjust=false`
  単一のバックエンドの重みを、絶対値または相対値で調整します。プライマリのバックエンドを選択していて、代替バックエンドが複数ある場合はエラーになります。

- `--all=false`
  true の場合、指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--equal=false`
  true の場合、すべてのバックエンドの重みを 100 に設定します。

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

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--zero=false`
  true の場合、すべてのバックエンドの重みを 0 に設定します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set route-backends --help` / `gen-oc-help.py` で生成</sub>
