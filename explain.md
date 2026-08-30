# `oc explain`

> リソースのドキュメントを取得する

[`oc`](oc.md) / `explain`

## Usage

```
oc explain TYPE [--recursive=FALSE|TRUE] [--api-version=api-version-group] [-o|--output=plaintext|plaintext-openapiv2] [options]
```

各種リソースのフィールドと構造を説明します。

このコマンドは、サポートされている各 API リソースに紐づくフィールドを説明します。フィールドは、次のような単純な JSONPath の識別子で指定します:

        <type>.<fieldName>[.<fieldName>]
各フィールドの情報は、OpenAPI 形式でサーバーから取得されます。

サポートされているリソースの完全な一覧は "oc api-resources" で確認できます。

## Examples

```bash
# リソースとそのフィールドのドキュメントを取得する
oc explain pods

# リソース内のすべてのフィールドを取得する
oc explain pods --recursive

# サポートされている API バージョンでの deployment の説明を取得する
oc explain deployments --api-version=apps/v1

# リソースの特定フィールドのドキュメントを取得する
oc explain pods.spec.containers

# リソースのドキュメントを別の形式で取得する
oc explain deployment --output=plaintext-openapiv2
```

## Options

- `--api-version=''`
  特定の API バージョン（API グループ / バージョン）についての説明を取得する

- `-o, --output='plaintext'`
  スキーマの出力形式 (plaintext, plaintext-openapiv2)

- `--recursive=false`
  フィールドのさらに下のフィールドを表示する（現時点では 1 階層のみ）

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc explain --help` / `gen-oc-help.py` で生成</sub>
