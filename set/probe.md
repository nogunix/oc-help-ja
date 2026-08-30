# `oc set probe`

> Pod テンプレートのプローブを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `probe`

## Usage

```
oc set probe RESOURCE/NAME --readiness|--liveness [flags] (--get-url=URL|--open-tcp=PORT|-- CMD) [options]
```

Pod または Pod テンプレートの liveness / readiness / startup プローブを設定または削除します。

Pod 内の各コンテナは、一般的なヘルスチェックに使用するプローブを 1 つ以上定義できます。liveness プローブは、コンテナが正常なままかを定期的に確認します。プローブが失敗するとコンテナは再起動されます。readiness プローブは各コンテナの ready フラグを設定 / 解除し、これによってコンテナのポートが Service のエンドポイント一覧に含まれるか、およびデプロイを進められるかが決まります。readiness チェックは、コンテナがリクエストを受け付けたり処理を開始したりできる状態になったことを示すべきです。startup プローブは、liveness プローブの開始前に、コンテナの起動により長い時間を許容します。各コンテナに liveness と readiness の両方のプローブを設定することを強く推奨します。

3 種類のプローブは次のとおりです:

1. Pod の IP に対して TCP ソケットを開く 2. コンテナ上の URL に HTTP GET を実行し、200 OK が返ることを確認する 3. コンテナ内でコマンドを実行し、終了コード 0 が返ることを確認する

起動時間がばらつくコンテナでは initial-delay-seconds に十分大きな値を設定してください。そうしないと、アプリケーションの変化にともなって突然失敗し始めることがあります。

## Examples

```bash
# すべてのコンテナから readiness プローブと liveness プローブの両方を削除する
oc set probe dc/myapp --remove --readiness --liveness

# 'echo ok' を実行する exec アクションを liveness プローブとして設定する
oc set probe dc/myapp --liveness -- echo ok

# 3306 番への TCP ソケット接続を試みる readiness プローブを設定する
oc set probe rc/mysql --readiness --open-tcp=3306

# Pod の IP に対し、ポート 8080・パス /healthz への HTTP startup プローブを設定する
oc set probe dc/webapp --startup --get-url=http://:8080/healthz

# Pod の IP に対し、ポート 8080・パス /healthz への HTTP readiness プローブを設定する
oc set probe dc/webapp --readiness --get-url=http://:8080/healthz

# hostNetwork の Pod に対し、127.0.0.1 への HTTPS 経由の HTTP readiness プローブを設定する
oc set probe dc/router --readiness --get-url=https://127.0.0.1:1936/stats

# すべてのデプロイメントで initial-delay-seconds フィールドだけを設定する
oc set probe dc --all --readiness --initial-delay-seconds=30
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

- `--failure-threshold=0`
  プローブが失敗したとみなすまでの失敗回数

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `--get-url=''`
  HTTP GET を実行する URL（ホストの省略、文字列のポート指定、スキームの省略が可能です）。

- `--initial-delay-seconds=0`
  プローブによる確認を開始するまでの待ち時間（秒）

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--liveness=false`
  このコンテナが動作していることを確認する liveness プローブを設定または削除する

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `--open-tcp=''`
  TCP で接続を試みるポート番号またはポート名。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--period-seconds=0`
  試行の間隔（秒）

- `--readiness=false`
  このコンテナがいつトラフィックを受け付けられるかを示す readiness プローブを設定または削除する

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove=false`
  true の場合、指定したプローブを削除します。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--startup=false`
  このコンテナが動作していることを確認する startup プローブを設定または削除する

- `--success-threshold=0`
  プローブが成功したとみなすために必要な成功回数

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--timeout-seconds=0`
  プローブが失敗したとみなすまでの待ち時間（秒）

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set probe --help` / `gen-oc-help.py` で生成</sub>
