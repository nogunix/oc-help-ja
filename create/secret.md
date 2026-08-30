# `oc create secret`

> 指定したサブコマンドを使ってシークレットを作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `secret`

## Usage

```
oc create secret (docker-registry | generic | tls) [options]
```

指定したタイプでシークレットを作成します。

docker-registry タイプのシークレットは、コンテナレジストリへのアクセスに使用します。

generic タイプのシークレットは、Opaque シークレットタイプを表します。

tls タイプのシークレットは、TLS 証明書とそれに対応する鍵を保持します。

## Subcommands

- [`docker-registry`](secret/docker-registry.md) — Docker レジストリで使用するシークレットを作成する
- [`generic`](secret/generic.md) — ローカルのファイル、ディレクトリ、またはリテラル値からシークレットを作成する
- [`tls`](secret/tls.md) — TLS シークレットを作成する

> 各コマンドの詳細については "oc create secret `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create secret --help` / `gen-oc-help.py` で生成</sub>
