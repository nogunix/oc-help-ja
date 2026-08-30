# `oc config refresh-ca-bundle`

> API サーバーに接続して OpenShift の CA バンドルを更新する

[`oc`](../oc.md) / [`oc config`](../config.md) / `refresh-ca-bundle`

## Usage

```
oc config refresh-ca-bundle [NAME] [options]
```

OpenShift クラスタから内容を読み取って CA バンドルを更新します。

## Examples

```bash
# 現在のコンテキストのクラスタについて、CA バンドルを更新する
oc config refresh-ca-bundle

# kubeconfig 内の e2e という名前のクラスタについて、CA バンドルを更新する
oc config refresh-ca-bundle e2e

# 現在の OpenShift クラスタの API サーバーの CA バンドルを表示する
oc config refresh-ca-bundle --dry-run
```

## Options

- `--dry-run=false`
  CA バンドルを表示するだけで、kubeconfig には一切変更を加えません

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config refresh-ca-bundle --help` / `gen-oc-help.py` で生成</sub>
