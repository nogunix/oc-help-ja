# `oc adm create-provider-selection-template`

> プロバイダ選択テンプレートを作成する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-provider-selection-template`

## Usage

```
oc adm create-provider-selection-template [flags] [options]
```

プロバイダ選択ページをカスタマイズするためのテンプレートを作成する

このコマンドは、ログインプロバイダ選択ページをカスタマイズするための出発点となる基本テンプレートを作成します。出力をファイルに保存し、テンプレートを編集して見た目を変えたり、内容を追加したりしてください。波括弧内のパラメータ値を削除しないよう注意してください。

このテンプレートを使用するには、master の設定で oauthConfig.templates.providerSelection がテンプレートファイルを指すように設定します。例:

        oauthConfig:
        templates:
        providerSelection: templates/provider-selection.html

## Examples

```bash
# プロバイダ選択ページ用のテンプレートを標準出力に出力する
oc adm create-provider-selection-template
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm create-provider-selection-template --help` / `gen-oc-help.py` で生成</sub>
