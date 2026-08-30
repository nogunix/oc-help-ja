# `oc adm`

> クラスタを管理するためのツール

[`oc`](oc.md) / `adm`

## Usage

```
oc adm [flags] [options]
```

管理用コマンド

OpenShift クラスタを管理するための操作をここに集めています。

## Subcommands

- [`build-chain`](adm/build-chain.md) — ビルドの入力と依存関係を出力する
- [`catalog`](adm/catalog.md) — OpenShift の OLM カタログを管理するためのツール
- [`certificate`](adm/certificate.md) — 証明書要求を承認または拒否する
- [`copy-to-node`](adm/copy-to-node.md) — 指定したファイルをノードにコピーする
- [`cordon`](adm/cordon.md) — ノードをスケジュール不可にする
- [`create-bootstrap-project-template`](adm/create-bootstrap-project-template.md) — bootstrap プロジェクトテンプレートを作成する
- [`create-error-template`](adm/create-error-template.md) — エラーページテンプレートを作成する
- [`create-login-template`](adm/create-login-template.md) — ログインテンプレートを作成する
- [`create-provider-selection-template`](adm/create-provider-selection-template.md) — プロバイダ選択テンプレートを作成する
- [`drain`](adm/drain.md) — メンテナンスに備えてノードを drain する
- [`groups`](adm/groups.md) — グループを管理する
- [`inspect`](adm/inspect.md) — 指定したリソースのデバッグ用データを収集する
- [`migrate`](adm/migrate.md) — クラスタ内のデータを移行する
- [`must-gather`](adm/must-gather.md) — デバッグ情報を収集するための Pod を新しく起動する
- [`new-project`](adm/new-project.md) — 新しいプロジェクトを作成する
- [`node-image`](adm/node-image.md) — 既存のクラスタにノードを追加する
- [`node-logs`](adm/node-logs.md) — ノードのログを表示・絞り込みする
- [`ocp-certificates`](adm/ocp-certificates.md) — クラスタの証明書を管理するためのツール
- [`policy`](adm/policy.md) — クラスタの認可とセキュリティポリシーを管理する
- [`prune`](adm/prune.md) — サーバーから古いバージョンのリソースを削除する
- [`reboot-machine-config-pool`](adm/reboot-machine-config-pool.md) — 指定した MachineConfigPool の再起動を開始する
- [`release`](adm/release.md) — OpenShift のリリースプロセスを管理するためのツール
- [`restart-kubelet`](adm/restart-kubelet.md) — 指定したノードで kubelet を再起動する
- [`taint`](adm/taint.md) — 1 つ以上のノードの taint を更新する
- [`top`](adm/top.md) — サーバー上のリソースの使用量統計を表示する
- [`uncordon`](adm/uncordon.md) — ノードをスケジュール可能にする
- [`upgrade`](adm/upgrade.md) — クラスタをアップグレードする、またはアップグレードチャネルを調整する
- [`verify-image-signature`](adm/verify-image-signature.md) — イメージ署名に含まれるイメージの identity を検証する
- [`wait-for-node-reboot`](adm/wait-for-node-reboot.md) — `oc adm reboot-machine-config-pool` の実行後、ノードの再起動を待つ
- [`wait-for-stable-cluster`](adm/wait-for-stable-cluster.md) — プラットフォームのオペレータが安定するまで待つ

> 各コマンドの詳細については "oc adm `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm --help` / `gen-oc-help.py` で生成</sub>
