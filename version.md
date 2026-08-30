# `oc version`

> クライアントとサーバーのバージョン情報を表示する

[`oc`](oc.md) / `version`

## Usage

```
oc version [flags] [options]
```

現在のコンテキストについて、クライアントとサーバーのバージョン情報を表示する

## Examples

```bash
# 現在のコンテキストの OpenShift クライアント、kube-apiserver、openshift-apiserver のバージョン情報を表示する
oc version

# 現在のコンテキストの OpenShift クライアント、kube-apiserver、openshift-apiserver のバージョン番号を JSON 形式で表示する
oc version --output json

# 現在のコンテキストの OpenShift クライアントのバージョン情報を表示する
oc version --client
```

## Options

- `--client=false`
  クライアントのバージョンのみ表示します（サーバーへの接続は不要）。

- `-o, --output=''`
  'yaml' または 'json' のいずれか。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc version --help` / `gen-oc-help.py` で生成</sub>
