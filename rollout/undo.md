# `oc rollout undo`

> 以前のロールアウトに戻す

[`oc`](../oc.md) / [`oc rollout`](../rollout.md) / `undo`

## Usage

```
oc rollout undo (TYPE NAME | TYPE/NAME) [flags] [options]
```

以前のロールアウトへ戻します。

## Examples

```bash
# 以前のデプロイへロールバックする
oc rollout undo deployment/abc

# デーモンセットのリビジョン 3 へロールバックする
oc rollout undo daemonset/abc --to-revision=3

# dry-run で以前のデプロイへのロールバックを確認する
oc rollout undo --dry-run=server deployment/abc
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `-f, --filename=[]`
  サーバーから取得するリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `-l, --selector=''`
  絞り込みに使うセレクター（ラベルクエリ）。'='、'=='、'!='、'in'、'notin' をサポートします（例: -l key1=value1,key2=value2,key3 in (value3)）。一致するオブジェクトは、指定したラベル条件をすべて満たす必要があります。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--to-revision=0`
  ロールバック先のリビジョン。デフォルトは 0（最新のリビジョン）です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rollout undo --help` / `gen-oc-help.py` で生成</sub>
