# `oc adm groups`

> グループを管理する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `groups`

## Usage

```
oc adm groups [flags] [options]
```

クラスタ内のグループを管理する

グループはユーザーの集合で、ポリシーを記述する際に使用できます。

## Subcommands

- [`add-users`](groups/add-users.md) — グループにユーザーを追加する
- [`new`](groups/new.md) — 新しいグループを作成する
- [`prune`](groups/prune.md) — 外部プロバイダにレコードが存在しない、古い OpenShift グループを削除する
- [`remove-users`](groups/remove-users.md) — グループからユーザーを削除する
- [`sync`](groups/sync.md) — OpenShift のグループを外部プロバイダのレコードと同期する

> 各コマンドの詳細については "oc adm groups `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm groups --help` / `gen-oc-help.py` で生成</sub>
