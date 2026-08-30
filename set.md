# `oc set`

> オブジェクトの特定の機能を設定するためのコマンド

[`oc`](oc.md) / `set`

## Usage

```
oc set COMMAND [flags] [options]
```

アプリケーションのリソースを設定する

これらのコマンドは、既存のアプリケーションリソースへの変更を支援します。

## Subcommands

- [`build-hook`](set/build-hook.md) — ビルド設定のビルドフックを更新する
- [`build-secret`](set/build-secret.md) — ビルド設定のビルドシークレットを更新する
- [`data`](set/data.md) — config map またはシークレット内のデータを更新する
- [`deployment-hook`](set/deployment-hook.md) — デプロイメント設定のデプロイメントフックを更新する
- [`env`](set/env.md) — Pod テンプレートの環境変数を更新する
- [`image`](set/image.md) — Pod テンプレートのイメージを更新する
- [`image-lookup`](set/image-lookup.md) — アプリケーションのデプロイ時にイメージをどう解決するかを変更する
- [`probe`](set/probe.md) — Pod テンプレートのプローブを更新する
- [`resources`](set/resources.md) — Pod テンプレートを持つオブジェクトのリソース requests / limits を更新する
- [`route-backends`](set/route-backends.md) — ルートのバックエンドを更新する
- [`selector`](set/selector.md) — リソースにセレクターを設定する
- [`serviceaccount`](set/serviceaccount.md) — リソースのサービスアカウントを更新する
- [`subject`](set/subject.md) — ロールバインディングまたはクラスタロールバインディング内のユーザー、グループ、サービスアカウントを更新する
- [`triggers`](set/triggers.md) — 1 つ以上のオブジェクトのトリガーを更新する
- [`volumes`](set/volumes.md) — Pod テンプレートのボリュームを更新する

> 各コマンドの詳細については "oc set `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set --help` / `gen-oc-help.py` で生成</sub>
