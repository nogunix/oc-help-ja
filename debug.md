# `oc debug`

> デバッグ用に新しい Pod のインスタンスを起動する

[`oc`](oc.md) / `debug`

## Usage

```
oc debug RESOURCE/NAME [ENV1=VAL1 ...] [-c CONTAINER] [flags] [-- COMMAND] [options]
```

実行中のアプリケーションをデバッグするためのコマンドシェルを起動します。

イメージや設定の問題をデバッグする際は、実行中の Pod の構成をそのまま複製し、シェルで調査できると便利です。失敗している Pod は起動しておらず 'rsh' や 'exec' でアクセスできないこともあるため、'debug' コマンドを使うとその構成の複製を簡単に作成できます。

デフォルトの動作は、指定した Pod の最初のコンテナ内でシェルを起動することです。起動される Pod は元の Pod のコピーで、ラベルは取り除かれ、コマンドは Linux コンテナなら '/bin/sh'、Windows コンテナなら 'cmd.exe' に変更され、readiness / liveness チェックは無効化されます。コマンドを実行したいだけの場合は '--' に続けてコマンドを指定します。コマンドを渡した場合、デフォルトでは TTY の割り当ても標準入力の送信も行われません。コンテナや Pod をよくある方法で変更するための他のフラグもサポートされています。

コンテナ実行時によくある問題として、クラスタ上で root ユーザーとして実行することをセキュリティポリシーが禁止している、というものがあります。このコマンドを使うと、Pod を非 root で実行して試したり（--as-user）、非 root の Pod を root で実行したり（--as-root）できます。

Pod 以外の種類のオブジェクトも指定できます。Pod を作成するコントローラーリソース（デプロイメント、ビルド、ジョブなど）、Pod をホストできるオブジェクト（ノードなど）、Pod の作成に使えるリソース（イメージストリームタグなど）が指定できるほか、単に '--image=IMAGE' を渡して、シェルを含むイメージで簡単なシェルセッションを開始することもできます

デバッグ用 Pod は、リモートコマンドが完了するか、ユーザーがシェルを中断した時点で削除されます。

## Examples

```bash
# OpenShift のツールイメージを使って Pod 内でシェルセッションを開始する
oc debug

# 新しい Pod を作成して、現在実行中のデプロイメントをデバッグする
oc debug deploy/test

# 管理者としてノードをデバッグする
oc debug node/master-1

# Windows ノードをデバッグする
# 注: 選択するイメージは、ノードの Windows Server のバージョン (2019、2022) に一致している必要があります
oc debug node/win-worker-1 --image=mcr.microsoft.com/powershell:lts-nanoserver-ltsc2022

# 指定したイメージストリームタグを使って Pod 内でシェルを起動する
oc debug istag/mysql:latest -n openshift

# ジョブを非 root ユーザーとして実行して試す
oc debug job/test --as-user=1000000

# 'second' コンテナで env コマンドを実行して、失敗している特定のコンテナをデバッグする
oc debug daemonset/test -c second -- /bin/env

# デバッグ用に作成される Pod を確認する
oc debug mypod-9xbc -o yaml

# リソースをデバッグするが、デバッグ用 Pod は別の namespace で起動する
# 注: すべてのリソースが、変更なしに --to-namespace でデバッグできるわけではありません。たとえば、
# ボリュームとサービスアカウントは namespace に依存します。デバッグ用 Pod の定義を出力するには '-o yaml' を追加してください
# ディスクに保存します。必要に応じて定義を編集してから 'oc debug -f -' を実行するか、--to-namespace なしで実行してください
oc debug mypod-9xbc --to-namespace testns
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--as-root=false`
  true の場合、コンテナを root ユーザーとして実行しようとします

- `--as-user=-1`
  特定のユーザー UID でコンテナの実行を試みます（注: 管理者によってこのフラグの使用が制限されている場合があります）

- `-c, --container=''`
  コンテナ名。デフォルトは最初のコンテナです

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-f, --filename=[]`
  テンプレートを読み込むファイル名、ディレクトリ、または URL

- `--image=''`
  対象コンテナが使用するイメージを上書きします。

- `--image-stream=''`
  実行するデバッグ用イメージを含むイメージストリーム (namespace/name:tag) を指定します。

- `--keep-annotations=false`
  true の場合、元の Pod のアノテーションを維持します

- `--keep-init-containers=true`
  Pod の init コンテナを実行します。デフォルトは true です。

- `--keep-labels=false`
  true の場合、元の Pod のラベルを維持します

- `--keep-liveness=false`
  true の場合、元の Pod の liveness プローブを維持します

- `--keep-readiness=false`
  true の場合、元の Pod の readiness プローブを維持します

- `--keep-startup=false`
  true の場合、元の startup プローブを維持します

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-I, --no-stdin=false`
  コンテナへの STDIN の受け渡しを行いません。コマンドを指定しなかった場合のデフォルトは true です

- `-T, --no-tty=false`
  擬似端末の割り当てを無効にします

- `--node-name=''`
  実行するノードを指定します。デフォルトでは、Pod は有効な任意のノードで実行されます

- `--one-container=false`
  true の場合、選択したコンテナのみを実行し、それ以外はすべて削除します

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--preserve-pod=false`
  true の場合、debug コマンドの終了後も Pod を削除しません。

- `-q, --quiet=false`
  情報メッセージは表示されません。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--show-labels=false`
  出力時に、すべてのラベルを最後の列として表示します（デフォルトはラベル列を非表示）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--to-namespace=''`
  Pod を作成する namespace を上書きします（--namespace の代わりに使用します）。

- `-t, --tty=false`
  擬似端末の割り当てを強制する

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc debug --help` / `gen-oc-help.py` で生成</sub>
