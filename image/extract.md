# `oc image extract`

> イメージからファイルシステムにファイルをコピーする

[`oc`](../oc.md) / [`oc image`](../image.md) / `extract`

## Usage

```
oc image extract [flags] [options]
```

イメージの内容をディスクに取り出します。

イメージ全体または一部をファイルシステムにダウンロードします。コンテナランタイムエンジンを動かすことなく、イメージの内容にアクセスできます。

--path フラグを指定しない限り、イメージの内容はカレントディレクトリに取り出されます。

取り出すイメージは引数として渡します。--path フラグでは、コピー元からコピー先ディレクトリへのマッピングを複数定義できます。コピー元にはファイル、ディレクトリ（'/' で終わる）、またはディレクトリ内のファイルパターンを指定できます。コピー先は取り出し先のディレクトリです。コピー元とコピー先の両方を指定する必要があります。

指定したイメージが複数のオペレーティングシステムに対応している場合、現在の OS に一致するイメージが選択されます。それ以外の場合は、--filter-by-os で目的のイメージを選択する必要があります。

イメージ文字列の末尾にレイヤーセレクターを付けてイメージをさらに絞り込み、イメージ内の特定のレイヤーだけを取り出すこともできます。サポートされるセレクターは次のとおりです:

[`<index>`] - 指定したインデックス（0 始まり）のレイヤーを選択 [`<from_index>`,`<to_index>`] - インデックスの範囲でレイヤーを選択（終端は含まない） [~`<prefix>`] - ダイジェストのプレフィックスが一致するレイヤーを選択（一致しなければエラー）

負のインデックスはリストの末尾から数えます。たとえば [-1] は最後のレイヤーを選択します。

## Examples

```bash
# busybox イメージをカレントディレクトリに取り出す
oc image extract docker.io/library/busybox:latest

# busybox イメージを、指定したディレクトリ（存在している必要あり）に取り出す
oc image extract docker.io/library/busybox:latest --path /:/tmp/busybox

# linux/s390x プラットフォーム向けの busybox イメージを、カレントディレクトリに取り出す
# 注: extract ではワイルドカードによる絞り込みはサポートされません。取り出す os/arch を 1 つ指定してください
oc image extract docker.io/library/busybox:latest --filter-by-os=linux/s390x

# イメージから 1 つのファイルをカレントディレクトリに取り出す
oc image extract docker.io/library/centos:7 --path /bin/bash:.

# イメージの /etc/yum.repos.d/ フォルダからすべての .repo ファイルをカレントディレクトリに取り出す
oc image extract docker.io/library/centos:7 --path /etc/yum.repos.d/*.repo:.

# イメージの /etc/yum.repos.d/ フォルダからすべての .repo ファイルを、指定したディレクトリ（存在している必要あり）に取り出す
# 結果として、ローカルシステム上に /tmp/yum.repos.d/*.repo ができます
oc image extract docker.io/library/centos:7 --path /etc/yum.repos.d/*.repo:/tmp/yum.repos.d

# ディスクに保存されたイメージをカレントディレクトリに取り出す（$(pwd)/v2/busybox/blobs,manifests が存在する場合）
# カレントディレクトリが空でないため --confirm が必要です
oc image extract file://busybox:local --confirm

# $(pwd)/v2 以外のディレクトリにディスク保存されたイメージを、カレントディレクトリに取り出す
# カレントディレクトリが空でないため --confirm が必要です（$(pwd)/busybox-mirror-dir/v2/busybox が存在します）
oc image extract file://busybox:local --dir busybox-mirror-dir --confirm

# $(pwd)/v2 以外のディレクトリにディスク保存されたイメージを、指定したディレクトリ（存在している必要あり）に取り出す
oc image extract file://busybox:local --dir busybox-mirror-dir --path /:/tmp/busybox

# イメージの最後のレイヤーを取り出す
oc image extract docker.io/library/centos:7[-1]

# イメージの最初の 3 レイヤーを取り出す
oc image extract docker.io/library/centos:7[:3]

# イメージの最後の 3 レイヤーを取り出す
oc image extract docker.io/library/centos:7[-3:]
```

## Options

- `--all-layers=false`
  dry-run モードでは、下位のレイヤーから上位へ順に処理し、重複するファイルも省略しません。

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--confirm=false`
  空でないディレクトリへの取り出しを許可する場合に指定します。

- `--dir=''`
  file:// のイメージの取り出し元となる、ディスク上のディレクトリ。

- `--dry-run=false`
  実行される予定の操作を表示し、何も書き込まずに終了します。

- `--file=[]`
  指定したファイルをカレントディレクトリに取り出します。

- `--filter-by-os=''`
  複数のバリアントが存在する場合に、どのイメージを対象とするかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。

- `--idms-file=''`
  ImageDigestMirrorSet ファイルのパス。指定した場合、このファイルの情報を使ってイメージの代替の場所を探します。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--only-files=false`
  イメージからは通常のファイルとディレクトリのみを取り出します。

- `--path=[]`
  イメージの一部だけを取り出す、またはイメージの内容を取り出すディスク上のディレクトリを指定します。SRC:DST の形式で、SRC はイメージ内のパス、DST はローカルのディレクトリです。指定しない場合は、すべてをカレントディレクトリに取り出します。

- `-p, --preserve-ownership=false`
  取り出したファイルのパーミッションを維持します。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc image extract --help` / `gen-oc-help.py` で生成</sub>
