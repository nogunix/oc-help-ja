# `oc create service`

> 指定したサブコマンドを使って Service を作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `service`

## Usage

```
oc create service [flags] [options]
```

エイリアス: service, svc

## Subcommands

- [`clusterip`](service/clusterip.md) — ClusterIP Service を作成する
- [`externalname`](service/externalname.md) — ExternalName Service を作成する
- [`loadbalancer`](service/loadbalancer.md) — LoadBalancer Service を作成する
- [`nodeport`](service/nodeport.md) — NodePort Service を作成する

> 各コマンドの詳細については "oc create service `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create service --help` / `gen-oc-help.py` で生成</sub>
