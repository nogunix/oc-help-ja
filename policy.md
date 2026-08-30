# `oc policy`

> 認可ポリシーを管理する

[`oc`](oc.md) / `policy`

## Usage

```
oc policy [flags] [options]
```

## Subcommands

- [`add-role-to-group`](policy/add-role-to-group.md) — プロジェクトを対象に、グループにロールを付与する
- [`add-role-to-user`](policy/add-role-to-user.md) — 現在のプロジェクトを対象に、ユーザーまたはサービスアカウントにロールを付与する
- [`remove-group`](policy/remove-group.md) — プロジェクトからグループを削除する
- [`remove-role-from-group`](policy/remove-role-from-group.md) — プロジェクトを対象に、グループからロールを削除する
- [`remove-role-from-user`](policy/remove-role-from-user.md) — プロジェクトを対象に、ユーザーからロールを削除する
- [`remove-user`](policy/remove-user.md) — プロジェクトからユーザーを削除する
- [`scc-review`](policy/scc-review.md) — どのサービスアカウントが Pod を作成できるかを確認する
- [`scc-subject-review`](policy/scc-subject-review.md) — ユーザーまたはサービスアカウントが Pod を作成できるかどうかを確認する
- [`who-can`](policy/who-can.md) — あるリソースに対して指定した操作を実行できるのは誰かを一覧する

> 各コマンドの詳細については "oc policy `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc policy --help` / `gen-oc-help.py` で生成</sub>
