# `oc`

> OpenShift クライアント

## Usage

```
oc [flags] [options]
```

このクライアントを使うと、任意の OpenShift または Kubernetes クラスタ上でアプリケーションを開発・ビルド・デプロイ・実行できます。クラスタ管理用のコマンドも 'adm' サブコマンドの下に含まれています。

## Subcommands

### 基本コマンド

- [`login`](login.md) — サーバーにログインする
- [`new-project`](new-project.md) — 新しいプロジェクトを要求する
- [`new-app`](new-app.md) — 新しいアプリケーションを作成する
- [`status`](status.md) — 現在のプロジェクトの概要を表示する
- [`project`](project.md) — 別のプロジェクトに切り替える
- [`projects`](projects.md) — 既存のプロジェクトを表示する
- [`explain`](explain.md) — リソースのドキュメントを取得する

### ビルド / デプロイコマンド

- [`rollout`](rollout.md) — リソースのロールアウトを管理する
- [`rollback`](rollback.md) — アプリケーションの一部を以前のデプロイに戻す
- [`new-build`](new-build.md) — 新しいビルド設定を作成する
- [`start-build`](start-build.md) — 新しいビルドを開始する
- [`cancel-build`](cancel-build.md) — 実行中・保留中・新規のビルドをキャンセルする
- [`import-image`](import-image.md) — コンテナイメージレジストリからイメージをインポートする
- [`tag`](tag.md) — 既存のイメージにタグを付けてイメージストリームに登録する

### アプリケーション管理コマンド

- [`create`](create.md) — ファイルまたは標準入力からリソースを作成する
- [`apply`](apply.md) — ファイル名または標準入力から、リソースに設定を適用する
- [`get`](get.md) — 1 つまたは複数のリソースを表示する
- [`describe`](describe.md) — 特定のリソース、またはリソース群の詳細を表示する
- [`edit`](edit.md) — サーバー上のリソースを編集する
- [`set`](set.md) — オブジェクトの特定の機能を設定するためのコマンド
- [`label`](label.md) — リソースのラベルを更新する
- [`annotate`](annotate.md) — リソースのアノテーションを更新する
- [`expose`](expose.md) — 複製されたアプリケーションを Service または Route として公開する
- [`delete`](delete.md) — ファイル名、標準入力、リソースと名前、またはリソースとラベルセレクターでリソースを削除する
- [`scale`](scale.md) — デプロイメント、レプリカセット、またはレプリケーションコントローラーの新しいサイズを設定する
- [`autoscale`](autoscale.md) — デプロイメント設定、デプロイメント、レプリカセット、ステートフルセット、またはレプリケーションコントローラーをオートスケールする
- [`secrets`](secrets.md) — シークレットを管理する

### トラブルシューティング / デバッグコマンド

- [`logs`](logs.md) — Pod 内のコンテナのログを表示する
- [`rsh`](rsh.md) — コンテナ内でシェルセッションを開始する
- [`rsync`](rsync.md) — ローカルファイルシステムと Pod の間でファイルをコピーする
- [`port-forward`](port-forward.md) — 1 つ以上のローカルポートを Pod に転送する
- [`debug`](debug.md) — デバッグ用に新しい Pod のインスタンスを起動する
- [`exec`](exec.md) — コンテナ内でコマンドを実行する
- [`proxy`](proxy.md) — Kubernetes API サーバーへのプロキシを実行する
- [`attach`](attach.md) — 実行中のコンテナにアタッチする
- [`run`](run.md) — 指定したイメージをクラスタ上で実行する
- [`cp`](cp.md) — コンテナとの間でファイルやディレクトリをコピーする
- [`wait`](wait.md) — 1 つ以上のリソースが特定の条件を満たすまで待機する
- [`events`](events.md) — イベントを一覧する

### 高度なコマンド

- [`adm`](adm.md) — クラスタを管理するためのツール
- [`replace`](replace.md) — ファイル名または標準入力でリソースを置き換える
- [`patch`](patch.md) — リソースのフィールドを更新する
- [`process`](process.md) — テンプレートを処理してリソースのリストにする
- [`extract`](extract.md) — シークレットまたは config map をディスクに取り出す
- [`observe`](observe.md) — リソースの変更を監視して反応する（実験的機能）
- [`policy`](policy.md) — 認可ポリシーを管理する
- [`auth`](auth.md) — 認可の状態を調べる
- [`image`](image.md) — イメージ管理に便利なコマンド
- [`registry`](registry.md) — レジストリを操作するためのコマンド
- [`idle`](idle.md) — スケール可能なリソースをアイドル化する
- [`api-versions`](api-versions.md) — サーバーがサポートしている API バージョンを "group/version" の形式で表示する
- [`api-resources`](api-resources.md) — サーバーがサポートしている API リソースを表示する
- [`cluster-info`](cluster-info.md) — クラスタの情報を表示する
- [`diff`](diff.md) — 稼働中のバージョンと、適用した場合のバージョンの差分を表示する
- [`kustomize`](kustomize.md) — ディレクトリまたは URL から kustomization のターゲットをビルドする

### 設定コマンド

- [`get-token`](get-token.md) — 実験的機能: credentials exec プラグインとして、外部 OIDC 発行者からトークンを取得する
- [`logout`](logout.md) — 現在のサーバーセッションを終了する
- [`config`](config.md) — kubeconfig ファイルを変更する
- [`whoami`](whoami.md) — 現在のセッションの情報を返します。
- [`completion`](completion.md) — 指定したシェル (bash, zsh, fish, powershell) 用のシェル補完コードを出力する

### その他のコマンド

- [`plugin`](plugin.md) — プラグインを扱うためのユーティリティを提供します
- [`version`](version.md) — クライアントとサーバーのバージョン情報を表示する

> 各コマンドの詳細については "oc `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc --help` / `gen-oc-help.py` で生成</sub>
