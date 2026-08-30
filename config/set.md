# `oc config set`

> kubeconfig ファイル内の個々の値を設定する

[`oc`](../oc.md) / [`oc config`](../config.md) / `set`

## Usage

```
oc config set PROPERTY_NAME PROPERTY_VALUE [options]
```

PROPERTY_NAME はドット区切りの名前で、各要素は属性名またはマップのキーを表します。マップのキーにドットを含めることはできません。

PROPERTY_VALUE は設定したい新しい値です。'certificate-authority-data' のようなバイナリのフィールドは、--set-raw-bytes フラグを使わない限り base64 エンコードされた文字列を想定します。

既に存在する属性名を指定した場合、既存の値の上に新しいフィールドがマージされます。

## Examples

```bash
# my-cluster クラスタの server フィールドを https://1.2.3.4 に設定する
oc config set clusters.my-cluster.server https://1.2.3.4

# my-cluster クラスタの certificate-authority-data フィールドを設定する
oc config set clusters.my-cluster.certificate-authority-data $(echo "cert_data_here" | base64 -i -)

# my-context コンテキストの cluster フィールドを my-cluster に設定する
oc config set contexts.my-context.cluster my-cluster

# --set-raw-bytes オプションを使って、cluster-admin ユーザーの client-key-data フィールドを設定する
oc config set users.cluster-admin.client-key-data cert_data_here --set-raw-bytes=true
```

## Options

- `--set-raw-bytes=false`
  []byte 型の PROPERTY_VALUE を書き込む際、base64 デコードせずに、指定した文字列をそのまま書き込みます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config set --help` / `gen-oc-help.py` で生成</sub>
