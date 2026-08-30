# `oc run`

> 指定したイメージをクラスタ上で実行する

[`oc`](oc.md) / `run`

## Usage

```
oc run NAME --image=image [--env="key=value"] [--port=port] [--dry-run=server|client] [--overrides=inline-json] [--command] -- [COMMAND] [args...] [options]
```

指定したイメージを Pod で作成して実行します。

## Examples

```bash
# nginx の Pod を起動する
oc run nginx --image=nginx

# hazelcast の Pod を起動し、コンテナのポート 5701 を公開する
oc run hazelcast --image=hazelcast/hazelcast --port=5701

# hazelcast の Pod を起動し、コンテナに環境変数 "DNS_DOMAIN=cluster" と "POD_NAMESPACE=default" を設定する
oc run hazelcast --image=hazelcast/hazelcast --env="DNS_DOMAIN=cluster" --env="POD_NAMESPACE=default"

# hazelcast の Pod を起動し、コンテナにラベル "app=hazelcast" と "env=prod" を設定する
oc run hazelcast --image=hazelcast/hazelcast --labels="app=hazelcast,env=prod"

# dry run。対応する API オブジェクトを作成せずに出力します
oc run nginx --image=nginx --dry-run=client

# nginx の Pod を起動するが、JSON から読み取った一部の値で spec を上書きする
oc run nginx --image=nginx --overrides='{ "apiVersion": "v1", "spec": { ... } }'

# busybox の Pod を起動してフォアグラウンドに保ち、終了しても再起動しない
oc run -i -t busybox --image=busybox --restart=Never

# デフォルトのコマンドで nginx の Pod を起動するが、そのコマンドにカスタム引数 (arg1 .. argN) を渡す
oc run nginx --image=nginx -- <arg1> <arg2> ... <argN>

# 別のコマンドとカスタム引数を使って nginx の Pod を起動する
oc run nginx --image=nginx --command -- <cmd> <arg1> ... <argN>
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--annotations=[]`
  Pod に適用するアノテーション。

- `--attach=false`
  true の場合、Pod が実行状態になるまで待ってから、'kubectl attach ...' を実行したかのように Pod にアタッチします。デフォルトは false ですが、'-i/--stdin' を指定した場合のデフォルトは true です。'--restart=Never' の場合、コンテナプロセスの終了コードが返されます。

- `--cascade='background'`
  "background"、"orphan"、"foreground" のいずれかを指定します。従属リソース（ReplicationController が作成した Pod など）に対する削除のカスケード方式を選択します。デフォルトは background です。

- `--command=false`
  true で追加の引数がある場合、それらをコンテナの 'args' フィールド（デフォルト）ではなく 'command' フィールドとして使用します。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--env=[]`
  コンテナに設定する環境変数。

- `--expose=false`
  true の場合、その Pod に紐づく ClusterIP Service を作成します。`--port` が必要です。

- `--field-manager='kubectl-run'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの置き換えに使用する。

- `--force=false`
  true の場合、正常な削除処理を行わず、API から直ちにリソースを削除します。リソースによっては即時削除により不整合やデータ損失が生じる可能性があり、確認が必要です。

- `--grace-period=-1`
  リソースの正常終了に与える猶予時間（秒）。負の値の場合は無視されます。即時シャットダウンするには 1 を指定します。0 を指定できるのは --force が true（強制削除）の場合のみです。

- `--image=''`
  実行するコンテナのイメージ。

- `--image-pull-policy=''`
  コンテナのイメージ pull ポリシー。空のままにした場合、クライアントは値を指定せず、サーバー側でデフォルトが適用されます。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-l, --labels=''`
  Pod に適用するラベルのカンマ区切りリスト。以前の値を上書きします。

- `--leave-stdin-open=false`
  Pod がインタラクティブモードまたは stdin 付きで起動されている場合、最初のアタッチが終了しても stdin を開いたままにします。デフォルトでは、最初のアタッチが終了すると stdin は閉じられます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--override-type='merge'`
  生成されたオブジェクトの上書きに使用する方式: json、merge、strategic のいずれか。

- `--overrides=''`
  生成されるオブジェクトを上書きするインライン JSON。空でない場合、生成されたオブジェクトの内容を上書きします。オブジェクトが有効な apiVersion フィールドを持つ必要があります。

- `--pod-running-timeout=1m0s`
  少なくとも 1 つの Pod が実行状態になるまで待つ時間（5s、2m、3h のような 0 より大きい値）

- `--port=''`
  このコンテナが公開するポート。

- `--privileged=false`
  true の場合、コンテナを特権モードで実行します。

- `-q, --quiet=false`
  true の場合、確認メッセージを表示しません。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--restart='Always'`
  この Pod の再起動ポリシー。有効な値は [Always, OnFailure, Never] です。

- `--rm=false`
  true の場合、Pod の終了後にその Pod を削除します。コンテナにアタッチする場合（'--attach' や '-i/--stdin' を使用する場合）のみ有効です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `-i, --stdin=false`
  何もアタッチされていなくても、Pod 内のコンテナの stdin を開いたままにします。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--timeout=0s`
  削除を諦めるまでの待ち時間。0 の場合、オブジェクトのサイズからタイムアウトを決定します

- `-t, --tty=false`
  Pod 内のコンテナに TTY を割り当てます。

- `--wait=false`
  true の場合、リソースが消滅するまで待ってから終了します。finalizer の完了も待ちます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc run --help` / `gen-oc-help.py` で生成</sub>
