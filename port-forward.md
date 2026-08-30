# `oc port-forward`

> 1 つ以上のローカルポートを Pod に転送する

[`oc`](oc.md) / `port-forward`

## Usage

```
oc port-forward TYPE/NAME [options] [LOCAL_PORT:]REMOTE_PORT [...[LOCAL_PORT_N:]REMOTE_PORT_N]
```

Pod を選択するには deployment/mydeployment のように type/name を指定します。type を省略した場合のデフォルトは 'pod' です。

条件に一致する Pod が複数ある場合、Pod は自動的に選択されます。転送セッションは、選択された Pod が終了した時点で終わるため、転送を再開するにはコマンドを再実行する必要があります。

## Examples

```bash
# ローカルのポート 5000 と 6000 で待ち受け、Pod のポート 5000 と 6000 との間でデータを転送する
oc port-forward pod/mypod 5000 6000

# ローカルのポート 5000 と 6000 で待ち受け、そのデプロイメントが選択した Pod のポート 5000 と 6000 との間でデータを転送する
oc port-forward deployment/mydeployment 5000 6000

# ローカルのポート 8443 で待ち受け、その Service が選択した Pod 内の、"https" という名前のポートの targetPort に転送する
oc port-forward service/myservice 8443:https

# ローカルのポート 8888 で待ち受け、Pod の 5000 番に転送する
oc port-forward pod/mypod 8888:5000

# すべてのアドレスのポート 8888 で待ち受け、Pod の 5000 番に転送する
oc port-forward --address 0.0.0.0 pod/mypod 8888:5000

# localhost と指定した IP のポート 8888 で待ち受け、Pod の 5000 番に転送する
oc port-forward --address localhost,10.19.21.23 pod/mypod 8888:5000

# ローカルのランダムなポートで待ち受け、Pod の 5000 番に転送する
oc port-forward pod/mypod :5000
```

## Options

- `--address=[localhost]`
  待ち受けるアドレス（カンマ区切り）。値として指定できるのは IP アドレスまたは localhost のみです。localhost を指定した場合、kubectl は 127.0.0.1 と ::1 の両方へのバインドを試み、どちらもバインドできなければ失敗します。

- `--pod-running-timeout=1m0s`
  少なくとも 1 つの Pod が実行状態になるまで待つ時間（5s、2m、3h のような 0 より大きい値）

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc port-forward --help` / `gen-oc-help.py` で生成</sub>
