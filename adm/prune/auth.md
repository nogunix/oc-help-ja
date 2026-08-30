# `oc adm prune auth`

> 指定したロール、クラスタロール、ユーザー、グループへの参照を削除します

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `auth`

## Usage

```
oc adm prune auth [flags] [options]
```

指定したロール、クラスタロール、ユーザー、グループへの参照を削除します。それ以外の種類は無視されます。

## Options

- `--all=false`
  namespace 内のすべてのロールを prune します。

- `-f, --filename=[]`
  削除するリソースを含むファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune auth --help` / `gen-oc-help.py` で生成</sub>
