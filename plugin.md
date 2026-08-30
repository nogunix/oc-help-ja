# `oc plugin`

> プラグインを扱うためのユーティリティを提供します

[`oc`](oc.md) / `plugin`

## Usage

```
oc plugin [flags] [options]
```

プラグインは、メインのコマンドライン配布物には含まれない拡張機能を提供します。独自プラグインの書き方については、ドキュメントとサンプルを参照してください。

プラグインを見つけてインストールする最も簡単な方法は、Kubernetes のサブプロジェクトである krew [krew.sigs.k8s.io] を使うことです。krew のインストールについては https://krew.sigs.k8s.io/docs/user-guide/setup/install を参照してください

## Subcommands

- [`list`](plugin/list.md) — ユーザーの PATH 上にある、参照可能なすべてのプラグイン実行ファイルを一覧する

## Examples

```bash
# 利用可能なすべてのプラグインを一覧する
oc plugin list

# 利用可能なプラグインのバイナリ名のみを、パスなしで一覧する
oc plugin list --name-only
```

> 各コマンドの詳細については "oc plugin `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc plugin --help` / `gen-oc-help.py` で生成</sub>
