# `oc image`

> イメージ管理に便利なコマンド

[`oc`](oc.md) / `image`

## Usage

```
oc image COMMAND [flags] [options]
```

OpenShift 上のイメージを管理する

これらのコマンドは、OpenShift 上のイメージの管理を支援します。

## Subcommands

- [`append`](image/append.md) — イメージにレイヤーを追加してレジストリに push する
- [`extract`](image/extract.md) — イメージからファイルシステムにファイルをコピーする
- [`info`](image/info.md) — イメージの情報を表示する
- [`mirror`](image/mirror.md) — あるリポジトリから別のリポジトリへイメージをミラーする

> 各コマンドの詳細については "oc image `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc image --help` / `gen-oc-help.py` で生成</sub>
