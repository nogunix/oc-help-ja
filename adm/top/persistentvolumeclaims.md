# `oc adm top persistentvolumeclaims`

> 実験的機能: バインド済みの persistentvolumeclaim の使用量統計を表示します

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm top`](../top.md) / `persistentvolumeclaims`

## Usage

```
oc adm top persistentvolumeclaims [flags] [options]
```

このコマンドは、プラットフォームが管理するバインド済みのすべての persistentvolumeclaim を分析し、現在の使用量統計を表示します。

エイリアス: persistentvolumeclaims, persistentvolumeclaim, pvc

## Examples

```bash
# クラスタ全体で、バインド済みのすべての persistentvolumeclaim の使用量統計を表示する
oc adm top persistentvolumeclaims -A

# 特定の namespace で、バインド済みのすべての persistentvolumeclaim の使用量統計を表示する
oc adm top persistentvolumeclaims -n default

# 指定したバインド済み persistentvolumeclaim の使用量統計を表示する
oc adm top persistentvolumeclaims database-pvc app-pvc -n default
```

## Options

- `-A, --all-namespaces=false`
  指定した場合、すべての namespace の pvc 使用量を一覧します。--namespace を指定していても、現在のコンテキストの namespace は無視されます

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm top persistentvolumeclaims --help` / `gen-oc-help.py` で生成</sub>
