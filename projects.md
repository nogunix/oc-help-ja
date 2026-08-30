# `oc projects`

> 既存のプロジェクトを表示する

[`oc`](oc.md) / `projects`

## Usage

```
oc projects [flags] [options]
```

現在アクティブなプロジェクトと、サーバー上の既存プロジェクトの情報を表示します。

高度な設定を行う場合や、設定ファイルの内容を管理する場合は 'config' コマンドを使用してください。

## Examples

```bash
# すべてのプロジェクトを一覧する
oc projects
```

## Options

- `-q, --short=false`
  true の場合、プロジェクト名のみを表示します

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc projects --help` / `gen-oc-help.py` で生成</sub>
