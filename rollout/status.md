# `oc rollout status`

> ロールアウトの状況を表示する

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `status`

## Usage

```
oc rollout status (TYPE NAME | TYPE/NAME) [flags] [options]
```

デフォルトでは 'rollout status' は、最新のロールアウトが完了するまでその状態を監視し続けます。完了を待ちたくない場合は --watch=false を使用します。なお、途中で新しいロールアウトが始まった場合、'rollout status' は最新のリビジョンの監視を続けます。特定のリビジョンに固定し、別のリビジョンに置き換えられたら中断したい場合は、監視したいリビジョンを N として --revision=N を使用してください。

## Examples

```bash
# デプロイメントのロールアウト状況を監視する
oc rollout status deployment/nginx
```

## Options

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--revision=0`
  ステータスを表示する対象を特定のリビジョンに固定します。デフォルトは 0（最新のリビジョン）です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--timeout=0s`
  watch を終了するまでの待ち時間。0 は無期限を意味します。それ以外の値には対応する時間の単位を付けてください（例: 1s、2m、3h）。

- `-w, --watch=true`
  ロールアウトが完了するまで、その状況を監視します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollout status --help` / `gen-oc-help.py` で生成</sub>
