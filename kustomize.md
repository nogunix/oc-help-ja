# `oc kustomize`

> ディレクトリまたは URL から kustomization のターゲットをビルドする

[`oc`](oc.md) / `kustomize`

## Usage

```
oc kustomize DIR [flags] [options]
```

'kustomization.yaml' ファイルを使って KRM リソース群をビルドします。DIR 引数には 'kustomization.yaml' を含むディレクトリのパス、またはリポジトリルートからの同様のパスをサフィックスとして付けた git リポジトリ URL を指定します。DIR を省略した場合は '.' とみなされます。

## Examples

```bash
# カレントディレクトリをビルドする
oc kustomize

# 共有設定ディレクトリをビルドする
oc kustomize /home/config/production

# github からビルドする
oc kustomize https://github.com/kubernetes-sigs/kustomize.git/examples/helloWorld?ref=v1.0.6
```

## Options

- `--as-current-user=false`
  コンテナ内で関数を実行する際に、コマンド実行者の uid と gid を使用します

- `--enable-alpha-plugins=false`
  kustomize のプラグインを有効にします

- `--enable-helm=false`
  Helm チャート inflator ジェネレータの使用を有効にします。

- `-e, --env=[]`
  関数が使用する環境変数の一覧

- `--helm-api-versions=[]`
  Helm が Capabilities.APIVersions に使用する Kubernetes の API バージョン

- `--helm-command='helm'`
  helm コマンド（実行ファイルのパス）

- `--helm-debug=false`
  Helm チャート inflator ジェネレータのデバッグ出力を有効にします。

- `--helm-kube-version=''`
  Helm が Capabilities.KubeVersion に使用する Kubernetes のバージョン

- `--load-restrictor='LoadRestrictionsRootOnly'`
  'LoadRestrictionsNone' に設定した場合、ローカルの kustomization がルート外のファイルを読み込めるようになります。ただし、これは kustomization の再配置可能性を損ないます。

- `--mount=[]`
  ファイルシステムから読み込むストレージオプションの一覧

- `--network=false`
  ネットワークアクセスを宣言している関数について、それを有効にします

- `--network-name='bridge'`
  コンテナを実行する docker ネットワーク

- `-o, --output=''`
  指定した場合、出力をこのパスに書き出します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc kustomize --help` / `gen-oc-help.py` で生成</sub>
