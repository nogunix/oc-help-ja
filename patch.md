# `oc patch`

> リソースのフィールドを更新する

[`oc`](oc.md) / `patch`

## Usage

```
oc patch (-f FILENAME | TYPE NAME) [-p PATCH|--patch-file FILE] [options]
```

strategic merge patch、JSON merge patch、または JSON patch を使って、リソースのフィールドを更新します。

JSON と YAML 形式を受け付けます。

注: strategic merge patch はカスタムリソースではサポートされません。

## Examples

```bash
# パッチを JSON で指定し、strategic merge patch でノードを部分的に更新する
oc patch node k8s-node-1 -p '{"spec":{"unschedulable":true}}'

# パッチを YAML で指定し、strategic merge patch でノードを部分的に更新する
oc patch node k8s-node-1 -p $'spec:\n unschedulable: true'

# "node.json" で指定された type と name のノードを、strategic merge patch で部分的に更新する
oc patch -f node.json -p '{"spec":{"unschedulable":true}}'

# コンテナのイメージを更新する。spec.containers[*].name はマージキーであるため必須
oc patch pod valid-pod -p '{"spec":{"containers":[{"name":"kubernetes-serve-hostname","image":"new image"}]}}'

# 位置指定の配列を使った JSON パッチで、コンテナのイメージを更新する
oc patch pod valid-pod --type='json' -p='[{"op": "replace", "path": "/spec/containers/0/image", "value":"new image"}]'

# merge patch を使い、'scale' サブリソース経由でデプロイメントのレプリカ数を更新する
oc patch deployment nginx-deployment --subresource='scale' --type='merge' -p '{"spec":{"replicas":2}}'
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-patch'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  更新するリソースを特定するファイル名、ディレクトリ、または URL

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--local=false`
  true の場合、patch はサーバー側のリソースではなくファイルの内容に対して動作します。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-p, --patch=''`
  リソースの JSON ファイルに適用するパッチ。

- `--patch-file=''`
  リソースに適用するパッチが書かれたファイル。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--subresource=''`
  指定した場合、patch は対象オブジェクトのサブリソースに対して動作します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--type='strategic'`
  指定するパッチの種類。[json merge strategic] のいずれか

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc patch --help` / `gen-oc-help.py` で生成</sub>
