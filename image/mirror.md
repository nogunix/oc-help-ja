# `oc image mirror`

> あるリポジトリから別のリポジトリへイメージをミラーする

[`oc`](../oc.md) / [`oc image`](../image.md) / `mirror`

## Usage

```
oc image mirror SRC DST [DST ...] [flags] [options]
```

あるイメージリポジトリから別のリポジトリへイメージをミラーします。

指定した宛先イメージタグに push するソースイメージを、引数のリストとして受け取ります。イメージはローカルに保存されることなく、レジストリからレジストリへストリーミングされます。レジストリへの認証にはデフォルトの docker クレデンシャルが使用されます。

ソース側のタグ引数は省略でき、'*' ワイルドカードを使ってすべての、または一致するタグをミラー対象に選択することもできます。その場合、宛先はリポジトリでなければなりません。

ファイルミラーリングを使う場合、--dir と --from-dir フラグでコンテンツを保存するディスク上の場所を制御します。このディレクトリはコンテナレジストリの HTTP 構造を模しており、レイヤーとデータ (blob) をイメージのメタデータ (マニフェスト) と分けて格納します。--from-dir を指定しない場合は、--dir またはカレントディレクトリが使用されます。

S3 ミラーリングを使う場合、ホストの後の最初の 2 つのセグメントは region とバケットでなければなりません。ミラーリングでは、タグやダイジェストでイメージを pull できるよう必要なメタデータが作成されますが、マニフェストやタグの一覧表示はできません。--s3-source-bucket パラメータ（`<bucket>`/`<path>` の形式）を 1 つ以上指定して、（アップロードする代わりに）blob を探すバケットを指定することもできます。ソースバケットでは "/[store]" というサフィックスもサポートされており、blob の識別子をコンテナイメージレジストリがディスク上で使う形式に変換するため、既存の S3 バックエンドのコンテナイメージレジストリから直接ミラーできます。S3 の認証情報は docker の認証情報ファイルに保存してホスト名で参照させることも、環境変数やファイルという通常の AWS クライアントの場所から読み込ませることもできます。

マニフェストリスト形式のイメージは、--filter-by-os でコピー対象を制限しない限り、そのままコピーされます。このフラグは通常のイメージには影響しません。

## Examples

```bash
# イメージを別のタグにコピーする
oc image mirror myregistry.com/myimage:latest myregistry.com/myimage:stable

# イメージを別のレジストリにコピーする
oc image mirror myregistry.com/myimage:latest docker.io/myrepository/myimage:stable

# mysql で始まるすべてのタグを、コピー先リポジトリにコピーする
oc image mirror myregistry.com/myimage:mysql* docker.io/myrepository/myimage

# イメージをディスクにコピーし、レジストリとして配信できるディレクトリ構造を作成する
oc image mirror myregistry.com/myimage:latest file://myrepository/myimage:latest

# イメージを S3 にコピーする（<bucket>.s3.amazonaws.com/image:latest から pull する）
oc image mirror myregistry.com/myimage:latest s3://s3.amazonaws.com/<region>/<bucket>/image:latest

# タグを設定せずにイメージを S3 にコピーする（@<digest> で pull する）
oc image mirror myregistry.com/myimage:latest s3://s3.amazonaws.com/<region>/<bucket>/image

# イメージを複数の場所にコピーする
oc image mirror myregistry.com/myimage:latest docker.io/myrepository/myimage:stable \
docker.io/myrepository/myimage:dev

# 複数のイメージをコピーする
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
myregistry.com/myimage:new=myregistry.com/other:target

# イメージが 1 つしか見つからない場合でも、マルチアーキテクチャイメージのマニフェストリストをコピーする
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--keep-manifest-list=true

# マルチアーキテクチャイメージの特定の os/arch マニフェストをコピーする
# マルチアーキテクチャイメージで利用可能な os/arch を確認するには 'oc image info myregistry.com/myimage:latest' を実行する
# マルチアーキテクチャイメージの場合、フィルタで絞り込まれたマニフェストだけを含む新しいマニフェストリストのダイジェストが生成される点に注意してください
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--filter-by-os=os/arch

# マルチアーキテクチャイメージのすべての os/arch マニフェストをコピーする
# ミラーされる os/arch マニフェストの一覧を確認するには 'oc image info myregistry.com/myimage:latest' を実行する
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--keep-manifest-list=true

# 上記のコマンドは次と同等です
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--filter-by-os=.*

# マルチアーキテクチャイメージの特定の os/arch マニフェストをコピーする
# マルチアーキテクチャイメージで利用可能な os/arch を確認するには 'oc image info myregistry.com/myimage:latest' を実行する
# プラットフォーム固有のイメージがすべて揃っていない場合、転送先のレジストリがマニフェストリストを拒否することがあります
# スパースレジストリのサポートが有効なレジストリを使用する必要があります
oc image mirror myregistry.com/myimage:latest=myregistry.com/other:test \
--filter-by-os=linux/386 \
--keep-manifest-list=true
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--continue-on-error=false`
  エラーが発生しても処理を続行し、できる限り多くをミラーします。

- `--dir=''`
  file:// のイメージのコピー先となる、ディスク上のディレクトリ。

- `--dry-run=false`
  実行される予定の操作を表示し、書き込み先に何も書き込まずに終了します。

- `-f, --filename=[]`
  SRC=DST または SRC DST [DST ...] のマッピングを読み込むファイル（1 つ以上）。

- `--filter-by-os=''`
  複数のバリアントが存在する場合に、どのイメージを対象とするかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。

- `--force=false`
  リモートリポジトリに存在する場合でも、すべてのレイヤーとマニフェストの書き込みを試みます。

- `--from-dir=''`
  file:// のイメージの読み込み元となる、ディスク上のディレクトリ。--dir より優先されます

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--keep-manifest-list=false`
  常にマニフェストリストをミラーします。デフォルトでは、--filter-by-os を指定しない限り、ミラーリングを実行しているプラットフォームのアーキテクチャ固有のイメージだけをミラーします。

- `--max-per-registry=6`
  1 つのレジストリに対して許可する同時リクエスト数。

- `--max-registry=4`
  同時に接続するレジストリの数。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--s3-source-bucket=[]`
  アップロード済みの blob が存在する可能性がある S3 上のバケット / パスのリスト。末尾に [store] を付けると、コンテナイメージレジストリのパス規約を使用します。

- `--skip-missing=false`
  入力イメージが見つからない場合はスキップします。

- `--skip-mount=false`
  レイヤーをクロスマウントせず、常に push します

- `--skip-multiple-scopes=false`
  レジストリによっては、ログイン時に複数のスコープを渡すことに対応していません。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc image mirror --help` / `gen-oc-help.py` で生成</sub>
