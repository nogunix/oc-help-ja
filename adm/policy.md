# `oc adm policy`

> クラスタの認可とセキュリティポリシーを管理する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `policy`

## Usage

```
oc adm policy [flags] [options]
```

クラスタ上のポリシーを管理する

これらのコマンドを使うと、ユーザーに適用されるロールとポリシーを割り当てて管理できます。reconcile 系のコマンドでは、システムのポリシーを最新のデフォルトポリシーにリセット・更新できます。

ロールとバインディングの詳細については、次のリソースに対して 'get' および 'describe' コマンドを使用してください: 'clusterroles'、'clusterrolebindings'、'roles'、'rolebindings'、'scc'。

## Subcommands

- [`add-cluster-role-to-group`](policy/add-cluster-role-to-group.md) — クラスタ内のすべてのプロジェクトを対象に、グループにロールを付与する
- [`add-cluster-role-to-user`](policy/add-cluster-role-to-user.md) — クラスタ内のすべてのプロジェクトを対象に、ユーザーにロールを付与する
- [`add-role-to-group`](policy/add-role-to-group.md) — プロジェクトを対象に、グループにロールを付与する
- [`add-role-to-user`](policy/add-role-to-user.md) — 現在のプロジェクトを対象に、ユーザーまたはサービスアカウントにロールを付与する
- [`add-scc-to-group`](policy/add-scc-to-group.md) — グループに security context constraint を付与する
- [`add-scc-to-user`](policy/add-scc-to-user.md) — ユーザーまたはサービスアカウントに security context constraint を付与する
- [`remove-cluster-role-from-group`](policy/remove-cluster-role-from-group.md) — クラスタ内のすべてのプロジェクトを対象に、グループからロールを削除する
- [`remove-cluster-role-from-user`](policy/remove-cluster-role-from-user.md) — クラスタ内のすべてのプロジェクトを対象に、ユーザーからロールを削除する
- [`remove-group`](policy/remove-group.md) — プロジェクトからグループを削除する
- [`remove-role-from-group`](policy/remove-role-from-group.md) — プロジェクトを対象に、グループからロールを削除する
- [`remove-role-from-user`](policy/remove-role-from-user.md) — プロジェクトを対象に、ユーザーからロールを削除する
- [`remove-scc-from-group`](policy/remove-scc-from-group.md) — security context constraint からグループを削除する
- [`remove-scc-from-user`](policy/remove-scc-from-user.md) — security context constraint からユーザーを削除する
- [`remove-user`](policy/remove-user.md) — プロジェクトからユーザーを削除する
- [`scc-review`](policy/scc-review.md) — どのサービスアカウントが Pod を作成できるかを確認する
- [`scc-subject-review`](policy/scc-subject-review.md) — ユーザーまたはサービスアカウントが Pod を作成できるかどうかを確認する
- [`who-can`](policy/who-can.md) — あるリソースに対して指定した操作を実行できるのは誰かを一覧する

> 各コマンドの詳細については "oc adm policy `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm policy --help` / `gen-oc-help.py` で生成</sub>
