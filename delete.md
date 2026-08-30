# `oc delete`

> ファイル名、標準入力、リソースと名前、またはリソースとラベルセレクターでリソースを削除する

[`oc`](oc.md) / `delete`

## Usage

```
oc delete ([-f FILENAME] | [-k DIRECTORY] | TYPE [(NAME | -l label | --all)]) [options]
```

JSON と YAML 形式を受け付けます。指定できる引数の種類は 1 つだけです（ファイル名、リソースと名前、またはリソースとラベルセレクター）。

Pod など一部のリソースは、正常な削除に対応しています。これらのリソースには、強制終了されるまでの既定の待ち時間（猶予期間）が定義されていますが、--grace-period フラグで上書きしたり、--now を指定して猶予期間を 1 にしたりできます。これらのリソースはクラスタ内の実体を表すことが多いため、削除がすぐに反映されるとは限りません。Pod が動作しているノードが停止している、または API サーバーに到達できない場合、終了までに猶予期間よりはるかに長い時間がかかることがあります。リソースを強制削除するには --force フラグを指定する必要があります。注: 正常な削除に対応しているのは一部のリソースのみです。対応していない場合、--grace-period フラグは無視されます。

重要: Pod の強制削除では、その Pod のプロセスが終了したことの確認を待ちません。そのため、ノードが削除を検知して正常な削除処理を完了するまで、プロセスが動き続ける可能性があります。プロセスが共有ストレージを使っていたり、リモート API と通信して Pod 名で自身を識別していたりする場合、強制削除によって同じ識別子を使うプロセスが複数のマシンで同時に動作し、データの破損や不整合を招くおそれがあります。Pod が確実に終了していると分かっている場合、またはアプリケーションが同じ Pod の複数同時実行を許容できる場合にのみ、強制削除してください。また、Pod を強制削除すると、ノードがリソースを解放し切る前にスケジューラが新しい Pod をそのノードに配置し、その Pod が直ちに退避される可能性があります。

delete コマンドはリソースバージョンのチェックを行いません。そのため、削除を実行したのとまさに同じタイミングで誰かがそのリソースを更新した場合、その更新はリソースごと失われます。

CustomResourceDefinition を削除した後、ディスカバリキャッシュが無効化されるまで最大 6 時間かかることがあります。待ちたくない場合は "oc api-resources" を実行してディスカバリキャッシュを更新してください。

## Examples

```bash
# pod.json で指定された type と name を使って Pod を削除する
oc delete -f ./pod.json

# kustomization.yaml を含むディレクトリからリソースを削除する（例: dir/kustomization.yaml）
oc delete -k dir

# '.json' で終わるすべてのファイルからリソースを削除する
oc delete -f '*.json'

# 標準入力に渡した JSON 内の type と name を基に Pod を削除する
cat pod.json | oc delete -f -

# "baz" と "foo" という同じ名前を持つ Pod と Service を削除する
oc delete pod,service baz foo

# ラベル name=myLabel を持つ Pod と Service を削除する
oc delete pods,services -l name=myLabel

# 遅延を最小限にして Pod を削除する
oc delete pod foo --now

# 停止したノード上の Pod を強制削除する
oc delete pod foo --force

# すべての Pod を削除する
oc delete pods --all

# ユーザーが削除を確認した場合のみ、すべての Pod を削除する
oc delete pods --all --interactive
```

## Options

- `--all=false`
  指定したリソースタイプの namespace 内で、すべてのリソースを削除します。

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace を対象に、要求されたオブジェクトを一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます。

- `--cascade='background'`
  "background"、"orphan"、"foreground" のいずれかを指定します。従属リソース（ReplicationController が作成した Pod など）に対する削除のカスケード方式を選択します。デフォルトは background です。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-selector=''`
  絞り込みに使うセレクター（フィールドクエリ）。'='、'=='、'!=' をサポートします（例: --field-selector key1=value1,key2=value2）。サーバーがタイプごとにサポートするフィールドクエリの数には制限があります。

- `-f, --filename=[]`
  削除するリソースを含む。

- `--force=false`
  true の場合、正常な削除処理を行わず、API から直ちにリソースを削除します。リソースによっては即時削除により不整合やデータ損失が生じる可能性があり、確認が必要です。

- `--grace-period=-1`
  リソースの正常終了に与える猶予時間（秒）。負の値の場合は無視されます。即時シャットダウンするには 1 を指定します。0 を指定できるのは --force が true（強制削除）の場合のみです。

- `--ignore-not-found=false`
  "リソースが見つからない" 場合も削除成功として扱います。--all を指定した場合のデフォルトは "true" です。

- `-i, --interactive=false`
  true の場合、ユーザーが確認したときにのみリソースを削除します。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--now=false`
  true の場合、リソースに対して即時シャットダウンのシグナルを送ります（--grace-period=1 と同じ）。

- `-o, --output=''`
  出力モード。より短い出力 (resource/name) にするには "-o name" を使用します。

- `--raw=''`
  サーバーに DELETE する生の URI。kubeconfig ファイルで指定されたトランスポートを使用します。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--timeout=0s`
  削除を諦めるまでの待ち時間。0 の場合、オブジェクトのサイズからタイムアウトを決定します

- `--wait=true`
  true の場合、リソースが消滅するまで待ってから終了します。finalizer の完了も待ちます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc delete --help` / `gen-oc-help.py` で生成</sub>
