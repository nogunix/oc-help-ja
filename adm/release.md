# `oc adm release`

> OpenShift のリリースプロセスを管理するためのツール

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `release`

このツールは、クラスタを更新できるイメージをビルドするために OpenShift のリリース作業で使用されます。

これらのサブコマンドを使うと、リリースの情報を確認したり、管理操作を実行したり、リリースの内容を調べたり、リリースの内容をイメージレジストリ間でミラーしたりできます。

## Subcommands

- [`extract`](release/extract.md) — 更新ペイロードの内容をディスクに取り出す
- [`info`](release/info.md) — リリースの情報を表示する
- [`new`](release/new.md) — 新しい OpenShift リリースを作成する

> 各コマンドの詳細については "oc adm release `<command>` --help" を使用してください。

---

<sub>`$ oc adm release --help` / `gen-oc-help.py` で生成</sub>
