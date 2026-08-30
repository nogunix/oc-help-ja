# `oc adm prune images`

> 参照されていないイメージを削除する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm prune`](../prune.md) / `images`

## Usage

```
oc adm prune images [flags] [options]
```

イメージストリームタグ、イメージ、イメージレイヤーを、経過時間や使用状況に基づいて削除します。

このコマンドは、過去のイメージストリームタグ、未使用のイメージ、参照されていないイメージレイヤーを統合レジストリから削除します。デフォルトでは、すべてのイメージが候補とみなされます。--all=false フラグを指定すると、レジストリに直接 push されたイメージのみを対象にできます。

デフォルトでは、prune 操作は dry run として実行され、内部レジストリには一切変更を加えません。実際に変更を反映するには --confirm フラグが必要です。このフラグには、統合コンテナイメージレジストリへの有効なルートが必要です。クラスタネットワークの外でこのコマンドを実行する場合は、--registry-url でルートを指定する必要があります。

実際にイメージを削除できるのは、クラスタロール system:image-pruner 以上を持つログイン済みユーザーだけです。

レジストリが、現在のユーザーの設定にあるものとは別の自己署名ルート認証局で署名された証明書で保護されている場合、--certificate-authority フラグでその認証局を指定する必要があります。

certificate-authority を指定しない場合、次のケースでは非セキュアな接続が許可されます:

1. --force-insecure が指定されている 2. 指定された registry-url が http:// で始まっている 3. レジストリ URL がプライベートアドレスまたはリンクローカルアドレスである 4. ユーザーの設定が非セキュアな接続を許可している（--insecure-skip-tls-verify を付けてクラスタにログインした、または非セキュアな接続を許可した場合）

## Examples

```bash
# イメージとその参照元が 1 時間以上前のものだけを対象にした場合に、prune コマンドが何を削除するかを確認する
# 同じタグの下で、より新しい 3 つのリビジョンによって古くなったものが対象になる
oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m

# 実際に prune を実行するには、confirm フラグを付ける必要があります
oc adm prune images --keep-tag-revisions=3 --keep-younger-than=60m --confirm

# イメージの削除を対象とした場合に、prune コマンドが何を削除するかを確認する
# 現在設定されている limit range ('openshift.io/Image') を超えているもの
oc adm prune images --prune-over-size-limit

# 実際に prune を実行するには、confirm フラグを付ける必要があります
oc adm prune images --prune-over-size-limit --confirm

# 特定のレジストリホスト名に対して、非セキュアな HTTP プロトコルを強制する
oc adm prune images --registry-url=http://registry.example.org --confirm

# 特定のレジストリホスト名に対して、カスタム認証局を使ったセキュアな接続を強制する
oc adm prune images --registry-url=registry.example.org --certificate-authority=/path/to/custom/ca.crt --confirm
```

## Options

- `--all=true`
  外部レジストリからインポートされたイメージも prune の候補に含めます。prune された場合、それらに関連するミラー済みオブジェクトも統合レジストリから削除されます。

- `--certificate-authority=''`
  管理対象のコンテナイメージレジストリとの通信に使用する認証局バンドルのパス。デフォルトは、現在のユーザーの設定ファイルにある認証局データです。--force-insecure とは併用できません。

- `--confirm=false`
  true の場合、イメージの prune を実際に実行します。デフォルトは false で、削除対象を表示するだけで実際には削除しません。統合コンテナイメージレジストリへの有効なルートが必要です（--registry-url を参照）。

- `--force-insecure=false`
  true の場合、HTTP でホストされている、または無効な HTTPS 証明書を持つコンテナイメージレジストリへの非セキュアな接続を許可します。可能な限り、この危険なオプションではなく --certificate-authority を使用してください。

- `--ignore-invalid-refs=false`
  true の場合、prune 処理はイメージ参照の解析中のエラーをすべて無視します。これは、オブジェクトと参照先イメージの本来の関連を無視することを意味します。その結果、使用中のイメージが未使用として誤って削除される可能性があります。

- `--keep-tag-revisions=3`
  イメージストリーム内の 1 つのタグについて、いくつのイメージリビジョンを残すかを指定します。

- `--keep-younger-than=1h0m0s`
  prune の候補とみなす、イメージとその参照元の最小経過時間を指定します。

- `--num-workers=5`
  prune 操作を実行する際に使用する並列ワーカー数を指定します。

- `--prune-over-size-limit=false`
  同じ namespace に指定された LimitRange（'openshift.io/Image' を参照）を超えているイメージを prune の対象とするかどうかを指定します。このフラグは --keep-younger-than や --keep-tag-revisions とは併用できません。

- `--prune-registry=true`
  false の場合、prune 操作はイメージ API オブジェクトを整理しますが、レジストリ上の関連コンテンツは一切削除しません。なお、このフラグでイメージ API オブジェクトのみを整理した場合、それらに対応するレジストリ上のデータを後から削除する手段は 'hard prune' の管理タスクだけになります。

- `--registry-url=''`
  レジストリへの接続時に、デフォルト値の代わりに使用するアドレス。レジストリを名前解決できない、または到達できない（デフォルトがクラスタ内部 URL である場合など）が、代わりに使える経路がある場合に便利です。'`<scheme>`://' プレフィックスで特定の転送プロトコルを強制できます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm prune images --help` / `gen-oc-help.py` で生成</sub>
