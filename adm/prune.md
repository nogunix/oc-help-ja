# `oc adm prune`

> サーバーから古いバージョンのリソースを削除する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `prune`

## Usage

```
oc adm prune [flags] [options]
```

ここにあるコマンドを使うと、管理者はシステム上の古いバージョンのリソースを削除して管理できます。

## Subcommands

- [`auth`](prune/auth.md) — 指定したロール、クラスタロール、ユーザー、グループへの参照を削除します
- [`builds`](prune/builds.md) — 完了済みおよび失敗した古いビルドを削除する
- [`deployments`](prune/deployments.md) — 完了済みおよび失敗した古いデプロイメント設定を削除する
- [`groups`](prune/groups.md) — 外部プロバイダにレコードが存在しない、古い OpenShift グループを削除する
- [`images`](prune/images.md) — 参照されていないイメージを削除する
- [`renderedmachineconfigs`](prune/renderedmachineconfigs.md) — OpenShift クラスタのレンダリング済み MachineConfig を prune します

> 各コマンドの詳細については "oc adm prune `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune --help` / `gen-oc-help.py` で生成</sub>
