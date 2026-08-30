# `oc adm new-project`

> 新しいプロジェクトを作成する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `new-project`

## Usage

```
oc adm new-project NAME [--display-name=DISPLAYNAME] [--description=DESCRIPTION] [flags] [options]
```

このコマンドでプロジェクトを作成します。任意で、プロジェクトのメタデータ、管理ユーザー（デフォルト以外の管理ロールを使いたい場合はそのロールも）、およびこのプロジェクトの Pod をスケジュールできるノードを制限するノードセレクターを指定できます。

## Examples

```bash
# ノードセレクターを指定して新しいプロジェクトを作成する
oc adm new-project myproject --node-selector='type=user-node,region=east'
```

## Options

- `--admin=''`
  プロジェクト管理者のユーザー名

- `--admin-role='admin'`
  クラスタポリシー上のプロジェクト管理者ロール名

- `--description=''`
  プロジェクトの説明

- `--display-name=''`
  プロジェクトの表示名

- `--node-selector=''`
  指定したラベルセレクターに一致するノードにのみ Pod を配置します。形式: '`<key1>`=`<value1>`, `<key2>`=`<value2>`...'。"" を指定すると、デフォルトではなく任意のノードを意味します。指定しない場合は、クラスタのデフォルトのノードセレクターが使用されます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm new-project --help` / `gen-oc-help.py` で生成</sub>
