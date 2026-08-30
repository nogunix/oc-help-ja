# `oc cluster-info`

> クラスタの情報を表示する

[`oc`](oc.md) / `cluster-info`

## Usage

```
oc cluster-info [flags] [options]
```

コントロールプレーンと、ラベル kubernetes.io/cluster-service=true を持つサービスのアドレスを表示します。クラスタの問題をさらに調査・診断するには 'oc cluster-info dump' を使用してください。

## Subcommands

- [`dump`](cluster-info/dump.md) — デバッグと診断に必要な情報をダンプする

## Examples

```bash
# コントロールプレーンとクラスタサービスのアドレスを表示する
oc cluster-info
```

> 各コマンドの詳細については "oc cluster-info `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc cluster-info --help` / `gen-oc-help.py` で生成</sub>
