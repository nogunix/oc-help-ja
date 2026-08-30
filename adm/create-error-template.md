# `oc adm create-error-template`

> エラーページテンプレートを作成する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-error-template`

## Usage

```
oc adm create-error-template [flags] [options]
```

エラーページをカスタマイズするためのテンプレートを作成する

このコマンドは、認証エラーページをカスタマイズするための出発点となる基本テンプレートを作成します。出力をファイルに保存し、テンプレートを編集して見た目を変えたり、内容を追加したりしてください。

このテンプレートを使用するには、master の設定で oauthConfig.templates.error がテンプレートファイルを指すように設定します。例:

        oauthConfig:
        templates:
        error: templates/error.html

## Examples

```bash
# エラーページ用のテンプレートを標準出力に出力する
oc adm create-error-template
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm create-error-template --help` / `gen-oc-help.py` で生成</sub>
