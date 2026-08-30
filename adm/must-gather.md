# `oc adm must-gather`

> デバッグ情報を収集するための Pod を新しく起動する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `must-gather`

## Usage

```
oc adm must-gather [flags] [options]
```

デバッグ情報を収集するための Pod を起動します。

このコマンドは、クラスタ上の一時的な namespace で Pod を起動してデバッグ情報を収集し、収集した情報をダウンロードします。

## Examples

```bash
# デフォルトのプラグインイメージとコマンドで情報を収集し、./must-gather.local.<rand> に書き出す
oc adm must-gather

# コピー先として特定のローカルフォルダを指定して情報を収集する
oc adm must-gather --dest-dir=/local/directory

# 監査情報を収集する
oc adm must-gather -- /usr/bin/gather_audit_logs

# 複数のプラグインイメージを使って情報を収集する
oc adm must-gather --image=quay.io/kubevirt/must-gather --image=quay.io/openshift/origin-must-gather

# 特定のイメージストリームプラグインを使って情報を収集する
oc adm must-gather --image-stream=openshift/must-gather:latest

# 特定のイメージ、コマンド、Pod ディレクトリを指定して情報を収集する
oc adm must-gather --image=my/image:tag --source-dir=/pod/directory -- myspecial-command.sh
```

## Options

- `--all-images=false`
  operators.openshift.io/must-gather-image アノテーションが付いた、クラスタ上のすべてのオペレータについて、デフォルトイメージで must-gather を収集する

- `--dest-dir=''`
  収集したデータを書き出す、ローカルマシン上のディレクトリを指定します。

- `--host-network=false`
  must-gather の Pod を hostNetwork: true で実行する（ホストレベルのデータを取得する必要がある特定のコマンドとイメージを使う場合に関係します）

- `--image=[]`
  実行する must-gather プラグインのイメージを指定します。指定しない場合は、OpenShift のデフォルトの must-gather イメージが使用されます。

- `--image-stream=[]`
  実行する must-gather プラグインイメージを含むイメージストリーム (namespace/name:tag) を指定します。

- `--node-name=''`
  使用するノードを指定します。デフォルトではランダムな master が使用されます

- `--node-selector=''`
  使用するノードセレクターを指定します（クラスタ内の複数ノードから同時にデータを取得する必要がある、特定のコマンドとイメージを使う場合にのみ関係します）

- `--run-namespace=''`
  must-gather の Pod を実行する、既存の特権 namespace。指定しない場合は一時的な namespace が生成されます。

- `--since=0s`
  5s、2m、3h のような相対時間より新しいログのみを返します。デフォルトはすべてのログです。プラグインでのサポートは推奨されていますが必須ではありません。since-time と since は同時に指定できません。

- `--since-time=''`
  指定した日時 (RFC3339) 以降のログのみを返します。デフォルトはすべてのログです。プラグインでのサポートは推奨されていますが必須ではありません。since-time と since は同時に指定できません。must-gather イメージ内のすべてのコマンドに適用されるとは限りません（RFC3339 に準拠しないコマンドがある、利用が限定的である、などの理由によります）。

- `--source-dir='/must-gather/'`
  収集したデータをコピーする元となる、Pod 上のディレクトリを指定します。

- `--timeout='10m'`
  データ収集の完了を待つ時間（5s、2m、3h のような 0 より大きい値）。デフォルトは 10 分です。注: このタイムアウトはデータ収集フェーズにのみ適用されます。収集完了後、ローカルへのコピーは終わるまで続行されます。

- `--volume-percentage=70`
  must-gather の Pod に割り当てられたボリュームのうち、使用してよい最大の割合を指定します。この上限を超えると、must-gather は収集を停止しますが、収集済みのデータのコピーは行います。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm must-gather --help` / `gen-oc-help.py` で生成</sub>
