# `oc adm upgrade recommend`

> クラスタ更新の推奨情報を表示します。

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm upgrade`](../upgrade.md) / `recommend`

## Usage

```
oc adm upgrade recommend [flags] [options]
```

このサブコマンドは読み取り専用で、クラスタの状態には影響しません。更新を要求するには 'oc adm upgrade' サブコマンドを使用してください。

デフォルトでは、このコマンドは最近のアップグレード候補リリースを表示します。特定のターゲットリリースに関する情報を表示するには '--version VERSION' を、古いリリースを含む既知のすべてのターゲットを表示するには '--show-outdated-releases' を使用します。

## Options

- `--accept=[]`
  許容できる問題の名前をカンマ区切りで指定します。--version と併用した場合、許容していない問題があると終了コードが 0 以外になります。

- `--quiet=false`
  --quiet が true で --version を指定した場合、許容していない問題の名前のみを表示します。

- `--show-outdated-releases=false`
  より古いリリースも追加で表示します。これらのリリースには、より新しいリリースで修正済みの既知の問題が残っている可能性があります。ただし、いずれの更新にも現在のリリースには含まれていない修正が入っています。

- `--version=''`
  表示する対象リリースをバージョンで指定します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm upgrade recommend --help` / `gen-oc-help.py` で生成</sub>
