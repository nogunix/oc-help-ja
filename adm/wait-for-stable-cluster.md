# `oc adm wait-for-stable-cluster`

> プラットフォームのオペレータが安定するまで待つ

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `wait-for-stable-cluster`

## Usage

```
oc adm wait-for-stable-cluster [flags] [options]
```

OCP v4 のすべての clusteroperator が Available=true、Progressing=false、Degraded=false を報告するまで待機します。

## Examples

```bash
# すべてのクラスタオペレータが安定するまで待つ
oc adm wait-for-stable-cluster

# オペレータが 5 分間続けて安定を報告したら、安定しているとみなす
oc adm wait-for-stable-cluster --minimum-stable-period 5m
```

## Options

- `--minimum-stable-period=5m0s`
  クラスタが安定しているとみなすための最小継続時間。デフォルトは 5 分です。

- `--timeout=1h0m0s`
  コマンドがタイムアウトするまでの時間。デフォルトは 1 時間です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm wait-for-stable-cluster --help` / `gen-oc-help.py` で生成</sub>
