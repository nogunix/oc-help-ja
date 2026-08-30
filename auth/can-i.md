# `oc auth can-i`

> ある操作が許可されるかどうかを確認する

[`oc`](../oc.md) / [`oc auth`](../auth.md) / `can-i`

## Usage

```
oc auth can-i VERB [TYPE | TYPE/NAME | NONRESOURCEURL] [options]
```

VERB は 'get'、'list'、'watch'、'delete' などの Kubernetes API の論理的な verb です。TYPE は Kubernetes のリソースで、短縮形やグループも解決されます。NONRESOURCEURL は "/" で始まる部分 URL です。NAME は特定の Kubernetes リソースの名前です。このコマンドは偽装（impersonation）と組み合わせると便利です。グローバルフラグの --as を参照してください。

## Examples

```bash
# 任意の namespace で Pod を作成できるかどうかを確認する
oc auth can-i create pods --all-namespaces

# 現在の namespace でデプロイメントを一覧できるかどうかを確認する
oc auth can-i list deployments.apps

# namespace "dev" のサービスアカウント "foo" が、namespace "prod" で Pod を一覧できるかどうかを確認する
# グローバルオプション "--as" による偽装（impersonation）の使用が許可されている必要があります
oc auth can-i list pods --as=system:serviceaccount:dev:foo -n prod

# 現在の namespace ですべての操作ができるかどうかを確認する（"*" はすべての意味）
oc auth can-i '*' '*'

# namespace "foo" のジョブ "bar" を取得できるかどうかを確認する
oc auth can-i list jobs.batch/bar -n foo

# Pod のログを読めるかどうかを確認する
oc auth can-i get pods --subresource=log

# URL /logs/ にアクセスできるかどうかを確認する
oc auth can-i get /logs/

# certificates.k8s.io を承認できるかどうかを確認する
oc auth can-i approve certificates.k8s.io

# namespace "foo" で許可されているすべての操作を一覧する
oc auth can-i --list --namespace=foo
```

## Options

- `-A, --all-namespaces=false`
  true の場合、指定した操作をすべての namespace で確認します。

- `--list=false`
  true の場合、許可されているすべての操作を表示します。

- `--no-headers=false`
  true の場合、許可されている操作をヘッダーなしで表示します

- `-q, --quiet=false`
  true の場合、出力を抑制して終了コードだけを返します。

- `--subresource=''`
  pod/log や deployment/scale などのサブリソース

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc auth can-i --help` / `gen-oc-help.py` で生成</sub>
