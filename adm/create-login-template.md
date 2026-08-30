# `oc adm create-login-template`

> ログインテンプレートを作成する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `create-login-template`

## Usage

```
oc adm create-login-template [flags] [options]
```

ログインページをカスタマイズするためのテンプレートを作成する

このコマンドは、ログインページをカスタマイズするための出発点となる基本テンプレートを作成します。出力をファイルに保存し、テンプレートを編集して見た目を変えたり、内容を追加したりしてください。波括弧内のパラメータ値を削除しないよう注意してください。

このテンプレートを使用するには、master の設定で oauthConfig.templates.login がテンプレートファイルを指すように設定します。例:

        oauthConfig:
        templates:
        login: templates/login.html

## Examples

```bash
# ログインページ用のテンプレートを標準出力に出力する
oc adm create-login-template
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm create-login-template --help` / `gen-oc-help.py` で生成</sub>
