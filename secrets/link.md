# `oc secrets link`

> サービスアカウントにシークレットを紐づける

[`oc`](../oc.md) / [`oc secrets`](../secrets.md) / `link`

## Usage

```
oc secrets link serviceaccounts-name secret-name [another-secret-name]... [flags] [options]
```

シークレットを紐づけると、サービスアカウントは一部の認証でそのシークレットを自動的に使用できるようになります。

## Examples

```bash
# サービスアカウントに image pull secret を追加し、Pod イメージの pull で自動的に使用させる
oc secrets link serviceaccount-name pull-secret --for=pull

# サービスアカウントに image pull secret を追加し、ビルドイメージの pull と push の両方で自動的に使用させる
oc secrets link builder builder-image-secret --for=pull,mount
```

## Options

- `--for=[mount]`
  紐づけるシークレットの種類: mount または pull

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc secrets link --help` / `gen-oc-help.py` で生成</sub>
