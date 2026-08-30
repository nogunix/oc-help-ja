# `oc api-resources`

> サーバーがサポートしている API リソースを表示する

[`oc`](oc.md) / `api-resources`

## Usage

```
oc api-resources [flags] [options]
```

## Examples

```bash
# サポートされている API リソースを表示する
oc api-resources

# サポートされている API リソースを、より多くの情報付きで表示する
oc api-resources -o wide

# サポートされている API リソースを、指定した列でソートして表示する
oc api-resources --sort-by=name

# サポートされている namespace スコープのリソースを表示する
oc api-resources --namespaced=true

# サポートされている、namespace に属さないリソースを表示する
oc api-resources --namespaced=false

# 特定の APIGroup に属する、サポートされている API リソースを表示する
oc api-resources --api-group=rbac.authorization.k8s.io
```

## Options

- `--api-group=''`
  指定した API グループのリソースに限定します。

- `--cached=false`
  利用可能であれば、キャッシュされたリソース一覧を使用します。

- `--categories=[]`
  指定したカテゴリに属するリソースに限定します。

- `--namespaced=true`
  false の場合は namespace に属さないリソースを返します。それ以外の場合は、デフォルトで namespace に属するリソースを返します。

- `--no-headers=false`
  デフォルトまたは custom-column の出力形式を使う場合に、ヘッダーを表示しません（デフォルトは表示）。

- `-o, --output=''`
  出力形式。(json, yaml, kyaml, name, wide) のいずれかを指定します。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--sort-by=''`
  空でない場合、指定したフィールドでリソースの一覧をソートします。フィールドには 'name' または 'kind' を指定できます。

- `--verbs=[]`
  指定した verb をサポートするリソースに限定します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc api-resources --help` / `gen-oc-help.py` で生成</sub>
