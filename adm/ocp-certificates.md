# `oc adm ocp-certificates`

> クラスタの証明書を管理するためのツール

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `ocp-certificates`

## Usage

```
oc adm ocp-certificates [flags] [options]
```

OCP 証明書コマンド

OpenShift プラットフォームの証明書を管理するための操作をここに集めています。

## Subcommands

- [`monitor-certificates`](ocp-certificates/monitor-certificates.md) — プラットフォームの証明書を監視する
- [`regenerate-leaf`](ocp-certificates/regenerate-leaf.md) — OpenShift クラスタのクライアント証明書とサービング証明書を再生成する
- [`regenerate-machine-config-server-serving-cert`](ocp-certificates/regenerate-machine-config-server-serving-cert.md) — OpenShift クラスタの machine config operator の証明書を再生成する
- [`regenerate-top-level`](ocp-certificates/regenerate-top-level.md) — OpenShift クラスタのトップレベル証明書を再生成する
- [`remove-old-trust`](ocp-certificates/remove-old-trust.md) — OpenShift クラスタで、プラットフォームの信頼バンドルを表す ConfigMap から古い CA を削除する
- [`update-ignition-ca-bundle-for-machine-config-server`](ocp-certificates/update-ignition-ca-bundle-for-machine-config-server.md) — OpenShift クラスタの user-data シークレットを、更新された MCO 証明書を使うよう更新する

> 各コマンドの詳細については "oc adm ocp-certificates `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm ocp-certificates --help` / `gen-oc-help.py` で生成</sub>
