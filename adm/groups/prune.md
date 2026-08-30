# `oc adm groups prune`

> 外部プロバイダにレコードが存在しない、古い OpenShift グループを削除する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm groups`](../groups.md) / `prune`

## Usage

```
oc adm groups prune [WHITELIST] [--whitelist=WHITELIST-FILE] [--blacklist=BLACKLIST-FILE] --sync-config=CONFIG-SOURCE [flags] [options]
```

外部プロバイダにレコードが存在しない OpenShift グループを prune します。

外部プロバイダの情報を使って OpenShift のグループレコードを prune するには、まず prune したいグループを決めます。たとえば、以前に同期されて OpenShift に保存されている現在のグループから、すべて、または一部を選択できます。リテラルのホワイトリスト、ホワイトリストファイル、ブラックリストファイルは任意に組み合わせられます。外部レコードストアからどのようにデータを取得するかを記述するため、対象グループの同期に使用した同期設定ファイルのパスが必要です。デフォルトの動作は、外部レコードが存在しない OpenShift グループをすべて表示するだけです。実際に prune 処理を実行して結果を反映するには --confirm フラグを使用してください。

## Examples

```bash
# 孤立したグループをすべて prune する
oc adm groups prune --sync-config=/path/to/ldap-sync-config.yaml --confirm

# 拒否リストファイルに載っているものを除いて、孤立したグループをすべて prune する
oc adm groups prune --blacklist=/path/to/denylist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm

# 許可リストファイルで指定した特定のグループのうち、孤立したものをすべて prune する
oc adm groups prune --whitelist=/path/to/allowlist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm

# リストで指定した特定のグループのうち、孤立したものをすべて prune する
oc adm groups prune groups/group_name groups/other_name --sync-config=/path/to/ldap-sync-config.yaml --confirm
```

## Options

- `--blacklist=''`
  グループのブラックリストファイルのパス

- `--confirm=false`
  true の場合は OpenShift のグループを変更し、false の場合はグループを表示します

- `--sync-config=''`
  同期設定ファイルのパス

- `--whitelist=''`
  グループのホワイトリストファイルのパス

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm groups prune --help` / `gen-oc-help.py` で生成</sub>
