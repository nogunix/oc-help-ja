# `oc set volumes`

> Pod テンプレートのボリュームを更新する

[`oc`](../oc.md) / [`oc set`](../set.md) / `volumes`

## Usage

```
oc set volumes RESOURCE/NAME --add|--remove [flags] [options]
```

このコマンドを使うと、Pod テンプレートを持つ任意のオブジェクト（デプロイメント設定、レプリケーションコントローラー、Pod）について、コンテナのボリュームを追加・更新・削除できます。Pod や Pod テンプレートを持つ任意のオブジェクトのボリュームを一覧することもできます。対象は 1 つでも複数でも指定でき、すべてのコンテナ、または指定した名前に一致するコンテナだけのボリュームを変更できます。

デプロイメント設定のボリューム設定を変更すると、デプロイがトリガーされます。レプリケーションコントローラーの変更は実行中の Pod には影響せず、Pod のボリュームは作成後に変更できません。

ボリュームタイプ:

- emptydir（空のディレクトリ、デフォルト）: Pod がローカルホスト上に作成された時点で割り当てられ、Pod の削除時に削除されるディレクトリ。サーバー間でコピーはされません
- hostdir（ホストのディレクトリ）: 任意のホスト上の特定パスにあるディレクトリ（昇格した権限が必要）
- persistentvolumeclaim または pvc（永続ボリュームクレーム）: コンテナ内のボリュームディレクトリを、名前で指定した既存の永続ボリュームクレームに結び付けます。永続ボリュームクレームはストレージ割り当ての要求です。クレームがバインドされていない場合、Pod は起動しない点に注意してください。
- secret（マウントされたシークレット）: シークレットボリュームは、名前で指定したシークレットを指定のディレクトリにマウントします。
他のボリュームタイプの説明については https://docs.openshift.com を参照してください

エイリアス: volumes, volume

## Examples

```bash
# 現在のプロジェクトのすべてのデプロイメント設定に定義されたボリュームを一覧する
oc set volume dc --all

# デプロイメント設定 (dc) 'myapp' に、新しい empty dir ボリュームを追加して以下にマウントする
# /var/lib/myapp
oc set volume dc/myapp --add --mount-path=/var/lib/myapp

# 既存の永続ボリュームクレーム (PVC) を使って、既存のボリューム 'v1' を上書きする
oc set volume dc/myapp --add --name=v1 -t pvc --claim-name=pvc1 --overwrite

# デプロイメント設定 'myapp' からボリューム 'v1' を削除する
oc set volume dc/myapp --remove --name=v1

# 既存のボリューム 'v1' を上書きする新しい永続ボリュームクレームを作成する
oc set volume dc/myapp --add --name=v1 -t pvc --claim-size=1G --overwrite

# ボリューム 'v1' のマウントポイントを /data に変更する
oc set volume dc/myapp --add --name=v1 -m /data --overwrite

# コンテナ "c1" からボリュームマウント "v1" を削除して、デプロイメント設定を変更する
# （そのボリューム "v1" を参照するボリュームマウントを持つコンテナが他になければ、ボリューム "v1" 自体も削除します）
oc set volume dc/myapp --remove --name=v1 --containers=c1

# より複雑なボリュームソース（AWS EBS、GCE PD、
# Ceph、Gluster、NFS、ISCSI、...）
oc set volume dc/myapp --add -m /data --source=<json-string>
```

## Options

- `--add=false`
  true の場合、コンテナにボリュームやボリュームマウントを追加します

- `--all=false`
  true の場合、指定したリソースタイプについて、namespace 内のすべてのリソースを選択します

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--claim-class=''`
  永続ボリュームクレームで使用する StorageClass

- `--claim-mode='ReadWriteOnce'`
  作成するクレームのアクセスモードを設定します。有効な値は ReadWriteOnce (rwo)、ReadWriteMany (rwm)、ReadOnlyMany (rom) です

- `--claim-name=''`
  永続ボリュームクレームの名前。persistentVolumeClaim ボリュームタイプでは指定が必須です

- `--claim-size=''`
  永続ボリュームのタイプとともに指定した場合、指定サイズ（バイト）の新しいクレームを作成します。SI 表記を受け付けます: 10、10G、10Gi

- `--configmap-name=''`
  永続化された config map の名前。configmap ボリュームタイプでは指定が必須です

- `--confirm=false`
  true の場合、複数のボリュームを本当に削除してよいことを確認したものとみなします

- `-c, --containers='*'`
  変更対象とする、選択した Pod テンプレート内のコンテナ名。ワイルドカードを使用できます

- `--default-mode=''`
  ファイル作成時のデフォルトのモードビット。0000 から 0777 の範囲で指定できます。デフォルトは 0644 です。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-set'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  リソースの編集に使用するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、set image は API サーバーに接続せずローカルで実行します。

- `-m, --mount-path=''`
  コンテナ内のマウントパス。--add または --remove の省略可能なパラメータです

- `--name=''`
  ボリュームの名前。空の場合、add 操作では自動生成されます

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--overwrite=false`
  true の場合、対象リソースの既存のボリュームソースを、指定した名前のもの、またはボリュームマウントで置き換えます

- `--path=''`
  ホスト側のパス。hostPath ボリュームタイプでは指定が必須です

- `--read-only=false`
  ボリュームを ReadOnly でマウントします。--add または --remove の省略可能なパラメータです

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--remove=false`
  true の場合、コンテナからボリュームやボリュームマウントを削除します

- `--secret-name=''`
  永続化されたシークレットの名前。secret ボリュームタイプでは指定が必須です

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--source=''`
  ボリュームソースの詳細を JSON 文字列で指定します。--type オプションが対応していないボリュームタイプが必要な場合に使用します（例: '{"nfs": {"path": "/tmp","server":"172.17.0.2"}}'）

- `--sub-path=''`
  コンテナのボリュームをマウントする際に使用する、ローカルボリューム内のパス。--add または --remove の省略可能なパラメータです

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `-t, --type=''`
  add 操作で使用するボリュームソースのタイプ。サポートされる値: emptyDir、hostPath、secret、configmap、persistentVolumeClaim

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc set volumes --help` / `gen-oc-help.py` で生成</sub>
