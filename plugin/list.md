# `oc plugin list`

> ユーザーの PATH 上にある、参照可能なすべてのプラグイン実行ファイルを一覧する

[`oc`](../oc.md) / [`oc plugin`](../plugin.md) / `list`

## Usage

```
oc plugin list [flags] [options]
```

ユーザーの PATH 上にあるすべてのプラグインファイルを一覧表示します。フルパスなしでプラグインのバイナリ名だけを見るには --name-only フラグを使用します。

利用可能なプラグインファイルの条件: - 実行可能である - ユーザーの PATH 上のいずれかにある - "oc-" で始まる

## Examples

```bash
# 利用可能なすべてのプラグインを一覧する
oc plugin list

# 利用可能なプラグインのバイナリ名のみを、パスなしで一覧する
oc plugin list --name-only
```

## Options

- `--name-only=false`
  true の場合、各プラグインのフルパスではなくバイナリ名のみを表示します

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc plugin list --help` / `gen-oc-help.py` で生成</sub>
