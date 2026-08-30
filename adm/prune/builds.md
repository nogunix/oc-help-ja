# `oc adm prune builds`

> 完了済みおよび失敗した古いビルドを削除する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `builds`

## Usage

```
oc adm prune builds [flags] [options]
```

完了済みおよび失敗した古いビルドを prune します。

デフォルトでは、prune 操作は dry run として実行され、内部レジストリには一切変更を加えません。実際に変更を反映するには --confirm フラグが必要です。

## Examples

```bash
# 完了済みおよび失敗した古いビルドを削除する dry run を実行する。さらに以下も含める
# 対応するビルド設定が既に存在しないすべてのビルド
oc adm prune builds --orphans

# 実際に prune を実行するには、confirm フラグを付ける必要があります
oc adm prune builds --orphans --confirm
```

## Options

- `--confirm=false`
  true の場合、ビルドの prune を実際に実行します。デフォルトは false で、削除対象を表示するだけで実際には削除しません。

- `--keep-complete=5`
  BuildConfig ごとに、ステータスが complete のビルドをいくつ残すかを指定します。

- `--keep-failed=1`
  BuildConfig ごとに、ステータスが failed、error、cancelled のビルドをいくつ残すかを指定します。

- `--keep-younger-than=1h0m0s`
  prune の候補とみなす Build の最小経過時間を指定します。

- `--orphans=false`
  true の場合、対応する BuildConfig が既に存在せず、ステータスが complete、failed、error、cancelled のいずれかであるビルドをすべて prune します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune builds --help` / `gen-oc-help.py` で生成</sub>
