# `oc new-project`

> 新しいプロジェクトを要求する

[`oc`](oc.md) / `new-project`

## Usage

```
oc new-project NAME [--display-name=DISPLAYNAME] [--description=DESCRIPTION] [flags] [options]
```

自分用の新しいプロジェクトを作成します。

管理者がセルフサービスを許可している場合、このコマンドは新しいプロジェクトを作成し、あなたをそのプロジェクトの管理者に割り当てます。

プロジェクトの作成後、そのプロジェクトが設定上のデフォルトプロジェクトになります。

## Examples

```bash
# 最小限の情報で新しいプロジェクトを作成する
oc new-project web-team-dev

# 表示名と説明を付けて新しいプロジェクトを作成する
oc new-project web-team-dev --display-name="Web Team Development" --description="Development project for the web team."
```

## Options

- `--description=''`
  プロジェクトの説明

- `--display-name=''`
  プロジェクトの表示名

- `--skip-config-write=false`
  true の場合、プロジェクト作成後に、そのプロジェクトを kubeconfig のクラスタエントリとして設定しません

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc new-project --help` / `gen-oc-help.py` で生成</sub>
