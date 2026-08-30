# `oc adm top`

> サーバー上のリソースの使用量統計を表示する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `top`

## Usage

```
oc adm top [flags] [options]
```

このコマンドは、プラットフォームが管理するリソースを分析し、現在の使用量統計を表示します。

## Subcommands

- [`images`](top/images.md) — イメージの使用量統計を表示する
- [`imagestreams`](top/imagestreams.md) — イメージストリームの使用量統計を表示する
- [`node`](top/node.md) — ノードのリソース使用量 (CPU / メモリ) を表示する
- [`persistentvolumeclaims`](top/persistentvolumeclaims.md) — 実験的機能: バインド済みの persistentvolumeclaim の使用量統計を表示します
- [`pod`](top/pod.md) — Pod のリソース使用量 (CPU / メモリ) を表示する

> 各コマンドの詳細については "oc adm top `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm top --help` / `gen-oc-help.py` で生成</sub>
