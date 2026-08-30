# `oc adm ocp-certificates regenerate-machine-config-server-serving-cert`

> OpenShift クラスタの machine config operator の証明書を再生成する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm ocp-certificates`](../ocp-certificates.md) / `regenerate-machine-config-server-serving-cert`

## Usage

```
oc adm ocp-certificates regenerate-machine-config-server-serving-cert [options]
```

OCP v4 クラスタの Machine Config Operator の証明書を再生成します。これは、新しいノードがクラスタに参加しようとする際に MCS の内容を検証するために使用される証明書です。

実験的機能: このコマンドは現在活発に開発中であり、予告なく変更される可能性があります。

## Examples

```bash
# user-data シークレットを変更せずに MCO の証明書を再生成する
oc adm ocp-certificates regenerate-machine-config-server-serving-cert --update-ignition=false

# 新しい MCS 証明書を使うよう user-data シークレットを更新する
oc adm ocp-certificates update-ignition-ca-bundle-for-machine-config-server
```

## Options

- `--update-ignition=true`
  true の場合、machine-api namespace の user-data シークレット (ignition) を自動的に更新します。ノードのスケーリングが MachineSet で行われていない場合は役に立ちません。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm ocp-certificates regenerate-machine-config-server-serving-cert --help` / `gen-oc-help.py` で生成</sub>
