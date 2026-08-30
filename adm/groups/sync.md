# `oc adm groups sync`

> OpenShift のグループを外部プロバイダのレコードと同期する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm groups`](../groups.md) / `sync`

## Usage

```
oc adm groups sync [--type=TYPE] [WHITELIST] [--whitelist=WHITELIST-FILE] --sync-config=CONFIG-FILE [--confirm] [flags] [options]
```

外部プロバイダの情報と OpenShift のグループレコードを同期するには、まずどのグループを同期するか、およびそれらのレコードがどこにあるかを決めます。たとえば、以前に同期されて OpenShift に保存されている現在のグループから、あるいは LDAP サーバー上に保存されているグループから、すべてまたは一部を選択できます。外部レコードストアからどのようにデータを取得し、OpenShift のレコードに移行するかを記述するため、同期設定ファイルのパスが必要です。デフォルトの動作は dry-run で、OpenShift のレコードは変更しません。'--confirm' を指定すると、LDAP クエリテンプレートが返した LDAP サーバー上のすべてのグループを同期します。

## Examples

```bash
# すべてのグループを LDAP サーバーと同期する
oc adm groups sync --sync-config=/path/to/ldap-sync-config.yaml --confirm

# ブラックリストファイルに載っているものを除いて、すべてのグループを LDAP サーバーと同期する
oc adm groups sync --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm

# 許可リストファイルで指定した特定のグループを、LDAP サーバーと同期する
oc adm groups sync --whitelist=/path/to/allowlist.txt --sync-config=/path/to/sync-config.yaml --confirm

# 以前に同期済みのすべての OpenShift グループを、LDAP サーバーと同期する
oc adm groups sync --type=openshift --sync-config=/path/to/ldap-sync-config.yaml --confirm

# 指定した OpenShift グループのうち、以前に LDAP サーバーと同期済みのものを同期する
oc adm groups sync groups/group1 groups/group2 groups/group3 --sync-config=/path/to/sync-config.yaml --confirm
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--blacklist=''`
  グループのブラックリストファイルのパス

- `--confirm=false`
  true の場合は OpenShift のグループを変更し、false の場合は dry-run の結果を表示します

- `-o, --output='yaml'`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--sync-config=''`
  同期設定ファイルのパス

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--type='ldap'`
  ホワイトリスト / ブラックリストのエントリがどちらのグループを指すか: ldap、openshift

- `--whitelist=''`
  グループのホワイトリストファイルのパス

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm groups sync --help` / `gen-oc-help.py` で生成</sub>
