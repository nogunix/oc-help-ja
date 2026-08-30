# `oc config`

> kubeconfig ファイルを変更する

[`oc`](oc.md) / `config`

## Usage

```
oc config SUBCOMMAND [options]
```

"oc config set current-context my-context" のようなサブコマンドで kubeconfig ファイルを変更します。

読み込みの順序は次のルールに従います:

1. --kubeconfig フラグが指定されている場合、そのファイルだけが読み込まれます。このフラグは 1 回しか指定できず、マージは行われません。 2. 環境変数 $KUBECONFIG が設定されている場合、それをパスのリスト（システム標準の区切り規則に従う）として使用します。これらのパスはマージされます。値を変更した場合は、その項目を定義しているファイルが変更されます。値を新規作成した場合は、存在する最初のファイルに作成されます。リスト中のどのファイルも存在しない場合は、リストの最後のファイルが作成されます。 3. いずれでもない場合は ${HOME}/.kube/config が使用され、マージは行われません。

## Subcommands

- [`current-context`](config/current-context.md) — current-context を表示する
- [`delete-cluster`](config/delete-cluster.md) — 指定したクラスタを kubeconfig から削除する
- [`delete-context`](config/delete-context.md) — 指定したコンテキストを kubeconfig から削除する
- [`delete-user`](config/delete-user.md) — 指定したユーザーを kubeconfig から削除する
- [`get-clusters`](config/get-clusters.md) — kubeconfig に定義されたクラスタを表示する
- [`get-contexts`](config/get-contexts.md) — 1 つまたは複数のコンテキストの詳細を表示する
- [`get-users`](config/get-users.md) — kubeconfig に定義されたユーザーを表示する
- [`new-admin-kubeconfig`](config/new-admin-kubeconfig.md) — 新しい admin.kubeconfig を生成し、サーバーに信頼させて表示する
- [`new-kubelet-bootstrap-kubeconfig`](config/new-kubelet-bootstrap-kubeconfig.md) — 新しい kubelet 用 /etc/kubernetes/kubeconfig を生成し、サーバーに信頼させて表示する
- [`refresh-ca-bundle`](config/refresh-ca-bundle.md) — API サーバーに接続して OpenShift の CA バンドルを更新する
- [`rename-context`](config/rename-context.md) — kubeconfig ファイルのコンテキスト名を変更する
- [`set`](config/set.md) — kubeconfig ファイル内の個々の値を設定する
- [`set-cluster`](config/set-cluster.md) — kubeconfig にクラスタエントリを設定する
- [`set-context`](config/set-context.md) — kubeconfig にコンテキストエントリを設定する
- [`set-credentials`](config/set-credentials.md) — kubeconfig にユーザーエントリを設定する
- [`unset`](config/unset.md) — kubeconfig ファイル内の個々の値を解除する
- [`use-context`](config/use-context.md) — kubeconfig ファイルの current-context を設定する
- [`view`](config/view.md) — マージ済みの kubeconfig 設定、または指定した kubeconfig ファイルを表示する

> 各コマンドの詳細については "oc config `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc config --help` / `gen-oc-help.py` で生成</sub>
