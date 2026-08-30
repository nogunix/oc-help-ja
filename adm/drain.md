# `oc adm drain`

> メンテナンスに備えてノードを drain する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `drain`

## Usage

```
oc adm drain NODE [options]
```

指定したノードは、新しい Pod が配置されないようスケジュール不可に設定されます。API サーバーが eviction https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ に対応していれば、'drain' は Pod を退避させます。対応していない場合は、通常の DELETE で Pod を削除します。'drain' は、mirror Pod（API サーバー経由では削除できません）を除くすべての Pod を退避または削除します。デーモンセットが管理する Pod がある場合、--ignore-daemonsets を指定しない限り drain は続行しません。また、いずれにせよデーモンセットが管理する Pod は削除しません。スケジュール不可の設定を無視するデーモンセットコントローラーによって、すぐに再作成されてしまうためです。mirror Pod でもなく、レプリケーションコントローラー・レプリカセット・デーモンセット・ステートフルセット・ジョブのいずれにも管理されていない Pod がある場合、--force を使わない限り drain は Pod を一切削除しません。--force は、1 つ以上の Pod の管理元リソースが存在しない場合にも削除を進められるようにします。

'drain' は Pod の正常終了を待ちます。コマンドが完了するまで、そのマシンを操作しないでください。

ノードを再び運用に戻す準備ができたら oc adm uncordon を使用してください。これにより、そのノードは再びスケジュール可能になります。

https://kubernetes.io/images/docs/oc adm_drain.svg Workflowhttps://kubernetes.io/images/docs/oc adm_drain.svg

## Examples

```bash
# レプリケーションコントローラー・レプリカセット・ジョブ・デーモンセット・ステートフルセットのいずれにも管理されていない Pod があっても、ノード "foo" を drain する
oc adm drain foo --force

# 上記と同じだが、レプリケーションコントローラー・レプリカセット・ジョブ・デーモンセット・ステートフルセットのいずれにも管理されていない Pod があれば中断し、猶予期間を 15 分にする
oc adm drain foo --grace-period=900
```

## Options

- `--chunk-size=500`
  大きなリストを一度に返さず、チャンクに分けて返します。0 を指定すると無効になります。

- `--delete-emptydir-data=false`
  emptyDir を使用している Pod（ノードの drain 時に削除されるローカルデータ）があっても続行します。

- `--disable-eviction=false`
  eviction がサポートされている場合でも、drain に delete を強制的に使用します。PodDisruptionBudget のチェックを回避するため、注意して使用してください。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--force=false`
  コントローラーが指定されていない Pod があっても続行します。

- `--grace-period=-1`
  各 Pod の正常終了に与える猶予時間（秒）。負の値の場合は、その Pod に指定されたデフォルト値が使用されます。

- `--ignore-daemonsets=false`
  DaemonSet が管理する Pod を無視します。

- `--pod-selector=''`
  ノード上の Pod を絞り込むためのラベルセレクター

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--skip-wait-for-delete-timeout=0`
  Pod の DeletionTimestamp が N 秒より古い場合、その Pod の待機をスキップします。スキップするには 0 より大きい秒数を指定する必要があります。

- `--timeout=0s`
  諦めるまでの待ち時間。0 は無期限を意味します

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm drain --help` / `gen-oc-help.py` で生成</sub>
