# `oc adm prune deployments`

> 完了済みおよび失敗した古いデプロイメント設定を削除する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `deployments`

## Usage

```
oc adm prune deployments [flags] [options]
```

完了済みおよび失敗した古いデプロイメント設定を prune します。

デフォルトでは、prune 操作は dry run として実行され、デプロイメント設定には一切変更を加えません。実際に変更を反映するには --confirm フラグが必要です。

## Examples

```bash
# 各デプロイメント設定について、最後に完了したデプロイ以外をすべて削除する dry run を実行する
oc adm prune deployments --keep-complete=1

# 実際に prune を実行するには、confirm フラグを付ける必要があります
oc adm prune deployments --keep-complete=1 --confirm
```

## Options

- `--confirm=false`
  true の場合、デプロイの prune を実際に実行します。デフォルトは false で、削除対象を表示するだけで実際には削除しません。

- `--keep-complete=5`
  DeploymentConfig ごとに、レプリカ数が 0 でステータスが complete のデプロイをいくつ残すかを指定します。

- `--keep-failed=1`
  DeploymentConfig ごとに、レプリカ数が 0 でステータスが failed のデプロイをいくつ残すかを指定します。

- `--keep-younger-than=1h0m0s`
  prune の候補とみなすデプロイの最小経過時間を指定します。

- `--orphans=false`
  true の場合、対応する DeploymentConfig が既に存在せず、ステータスが complete または failed で、レプリカ数が 0 のデプロイをすべて prune します。

- `--replica-sets=false`
  実験的機能: true にすると、ReplicaSet も prune 処理の対象に含めます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune deployments --help` / `gen-oc-help.py` で生成</sub>
