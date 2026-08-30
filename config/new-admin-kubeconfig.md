# `oc config new-admin-kubeconfig`

> 新しい admin.kubeconfig を生成し、サーバーに信頼させて表示する

[`oc`](../oc.md) / [`oc config`](../config.md) / `new-admin-kubeconfig`

## Usage

```
oc config new-admin-kubeconfig [options]
```

鍵はローカルで生成され、ディスクには保存されません。公開鍵側はクラスタに送られ、kube-apiserver がローカルで作成された admin.kubeconfig を信頼できるようになります。

## Examples

```bash
# 新しい admin kubeconfig を生成する
oc config new-admin-kubeconfig
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config new-admin-kubeconfig --help` / `gen-oc-help.py` で生成</sub>
