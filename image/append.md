# `oc image append`

> イメージにレイヤーを追加してレジストリに push する

[`oc`](../oc.md) / [`oc image`](../image.md) / `append`

## Usage

```
oc image append [flags] [options]
```

コンテナイメージにレイヤーを追加します。

既存のイメージにレイヤーを追加したり設定を変更したりして、そのイメージをリモートレジストリに push します。継承したレイヤーはローカルに保存されることなく、レジストリからレジストリへストリーミングされます。レジストリへの認証にはデフォルトの docker クレデンシャルが使用されます。

レイヤーはコマンドの引数として指定でき、それぞれ、継承元イメージに重ねるファイルシステムを表す gzip 圧縮された tar アーカイブである必要があります。アーカイブには "whiteout" ファイル（'.wh.' プレフィックス + ファイル名）を含めることができ、これにより下位レイヤーのファイルを隠せます。アーカイブに含まれる、サポート対象のファイルシステム属性はそのまま使用されます。

イメージのメタデータ（コンテナランタイムに渡される設定）は、--image または --meta オプションに JSON 文字列を渡すことで変更できます。--image フラグはコンテナランタイムから見える内容を変更し、--meta オプションはランタイムが使用するイメージの属性を変更します。変更結果は --dry-run で確認できます。--drop-history フラグを付けると、ベースイメージをビルドしたシステムに関する情報をイメージから削除できます。

マニフェストリスト形式のイメージで keep-manifest-list を指定した場合、リスト内のすべてのサブマニフェストに自動的にレイヤーが追加されます。ただし filter-by-os を指定した場合は、マニフェストリストを保持したまま、フィルタに一致したマニフェストにのみ追加されます。keep-manifest-list を指定しない場合は、--filter-by-os で別のイメージを選択しない限り、現在の OS とアーキテクチャに一致するイメージが自動的に選択されます。これらのフラグは通常のイメージには影響しません。

## Examples

```bash
# mysql:latest イメージのエントリポイントを削除する
oc image append --from mysql:latest --to myregistry.com/myimage:latest --image '{"Entrypoint":null}'

# イメージに新しいレイヤーを追加する
oc image append --from mysql:latest --to myregistry.com/myimage:latest layer.tar.gz

# イメージに新しいレイヤーを追加し、結果をディスクに保存する
# 結果は $(pwd)/v2/mysql/blobs,manifests になります
oc image append --from mysql:latest --to file://mysql:local layer.tar.gz

# イメージに新しいレイヤーを追加し、結果をディスク上の指定ディレクトリに保存する
# 結果は $(pwd)/mysql-local/v2/mysql/blobs,manifests になります
oc image append --from mysql:latest --to file://mysql:local --dir mysql-local layer.tar.gz

# ディスク上に保存されているイメージに新しいレイヤーを追加する（~/mysql-local/v2/image が存在する場合）
oc image append --from-dir ~/mysql-local --to myregistry.com/myimage:latest layer.tar.gz

# カレントディレクトリにミラーしたイメージに新しいレイヤーを追加する（$(pwd)/v2/image が存在する場合）
oc image append --from-dir v2 --to myregistry.com/myimage:latest layer.tar.gz

# システムの os/arch とは異なる os/arch 向けに、マルチアーキテクチャイメージへ新しいレイヤーを追加する
# 注: --keep-manifest-list を指定しない場合、マニフェストリスト内でフィルタに最初に一致したイメージが返されます
oc image append --from docker.io/library/busybox:latest --filter-by-os=linux/s390x --to myregistry.com/myimage:latest layer.tar.gz

# keep-manifest-list を指定した場合に、マルチアーキテクチャイメージのすべての os/arch マニフェストへ新しいレイヤーを追加する
oc image append --from docker.io/library/busybox:latest --keep-manifest-list --to myregistry.com/myimage:latest layer.tar.gz

# マニフェストリストを保持したまま、フィルタで指定した os/arch のすべてのマニフェストに対して、マルチアーキテクチャイメージへ新しいレイヤーを追加する
oc image append --from docker.io/library/busybox:latest --filter-by-os=linux/s390x --keep-manifest-list --to myregistry.com/myimage:latest layer.tar.gz
```

## Options

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。--insecure を使用した場合、このフラグは無視されます。

- `--created-at=''`
  このイメージの作成日時。RFC3339 形式、または Unix エポックからのミリ秒で指定します。

- `--dir=''`
  file:// のイメージのコピー先となる、ディスク上のディレクトリ。

- `--drop-history=false`
  そのイメージがどのように作成されたかという履歴に関するフィールドは削除されます。

- `--dry-run=false`
  実行される予定の操作を表示し、書き込み先に何も書き込まずに終了します。

- `--filter-by-os=''`
  複数のバリアントが存在する場合に、どのイメージを対象とするかを制御する正規表現。イメージは '`<platform>`/`<architecture>`[/`<variant>`]' の形式で渡されます。

- `--force=false`
  設定した場合、アップロード済みのレイヤーをスキップせず、すべてのレイヤーのアップロードを試みます。

- `--from=''`
  ベースとして使用するイメージ。空の場合は、新しい scratch イメージが作成されます。

- `--from-dir=''`
  file:// のイメージの読み込み元となる、ディスク上のディレクトリ。--dir より優先されます

- `--image=''`
  出力イメージのデータに適用する JSON パッチ。

- `--insecure=false`
  レジストリへの push / pull を HTTP 経由で行うことを許可します

- `--keep-manifest-list=false`
  イメージがマニフェストリストの一部である場合、リスト内の各イメージに常に追加します。デフォルトでは、--filter-by-os を指定しない限りすべてのイメージに追加します。

- `--max-per-registry=4`
  1 つのレジストリに対して許可する同時リクエスト数。

- `--meta=''`
  イメージのベースメタデータに適用する JSON パッチ（高度な設定）。

- `-a, --registry-config=''`
  レジストリの認証情報のパス。代わりに環境変数 REGISTRY_AUTH_FILE も指定できます。デフォルトは ${XDG_RUNTIME_DIR}/containers/auth.json、/run/containers/${UID}/auth.json、${XDG_CONFIG_HOME}/containers/auth.json、${DOCKER_CONFIG}、~/.docker/config.json、~/.dockercfg の順です。環境変数 REGISTRY_AUTH_PREFERENCE（非推奨）に "docker" を設定すると、Podman より Docker の認証情報を優先するよう順序を変更できます。

- `--skip-verification=false`
  取得したコンテンツの完全性検証をスキップします。推奨されませんが、古いイメージレジストリからイメージをインポートする場合には必要になることがあります。そのレジストリが信頼できると分かっている場合にのみ、検証を回避してください。

- `--to=''`
  レイヤーを追加したイメージをアップロードする先の Docker リポジトリのタグ。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc image append --help` / `gen-oc-help.py` で生成</sub>
