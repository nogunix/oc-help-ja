# `oc secrets`

> シークレットを管理する

[`oc`](oc.md) / `secrets`

## Usage

```
oc secrets [flags] [options]
```

プロジェクト内のシークレットを管理する

シークレットは、イメージ内に含めるべきでない機密情報を保存するために使用します。コンテナイメージレジストリなど、他の内部システムへの認証に使う鍵の保管によく使われます。

エイリアス: secrets, secret

## Subcommands

- [`link`](secrets/link.md) — サービスアカウントにシークレットを紐づける
- [`unlink`](secrets/unlink.md) — サービスアカウントからシークレットを切り離す

> 各コマンドの詳細については "oc secrets `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc secrets --help` / `gen-oc-help.py` で生成</sub>
