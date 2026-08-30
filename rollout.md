# `oc rollout`

> リソースのロールアウトを管理する

[`oc`](oc.md) / `rollout`

## Usage

```
oc rollout SUBCOMMAND [flags] [options]
```

1 つ以上のリソースのロールアウトを管理します。有効なリソースタイプ:

- deployments
- daemonsets
- statefulsets
- deploymentConfigs（非推奨）

## Subcommands

- [`cancel`](rollout/cancel.md) — 進行中のデプロイをキャンセルする
- [`history`](rollout/history.md) — ロールアウトの履歴を表示する
- [`latest`](rollout/latest.md) — トリガーの最新の状態を使って、デプロイメント設定の新しいロールアウトを開始する
- [`pause`](rollout/pause.md) — 指定したリソースを一時停止状態にする
- [`restart`](rollout/restart.md) — リソースを再起動する
- [`resume`](rollout/resume.md) — 一時停止中のリソースを再開する
- [`retry`](rollout/retry.md) — 最後に失敗したロールアウトを再試行する
- [`status`](rollout/status.md) — ロールアウトの状況を表示する
- [`undo`](rollout/undo.md) — 以前のロールアウトに戻す

## Examples

```bash
# 以前のデプロイへロールバックする
oc rollout undo deployment/abc

# デーモンセットのロールアウト状況を確認する
oc rollout status daemonset/foo

# デプロイメントを再起動する
oc rollout restart deployment/abc

# 'app=nginx' ラベルを持つデプロイメントを再起動する
oc rollout restart deployment --selector=app=nginx
```

> 各コマンドの詳細については "oc rollout `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollout --help` / `gen-oc-help.py` で生成</sub>
