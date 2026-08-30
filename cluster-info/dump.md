# `oc cluster-info dump`

> デバッグと診断に必要な情報をダンプする

[`oc`](../oc.md) / [`oc cluster-info`](../cluster-info.md) / `dump`

## Usage

```
oc cluster-info dump [flags] [options]
```

クラスタの問題のデバッグ・診断に適した形でクラスタ情報をダンプします。デフォルトではすべてを標準出力に出力します。--output-directory でディレクトリを指定することもでき、その場合 Kubernetes はそのディレクトリに一連のファイルを作成します。デフォルトでは現在の namespace と 'kube-system' namespace の情報のみをダンプしますが、--namespaces フラグで別の namespace に切り替えたり、--all-namespaces ですべての namespace をダンプしたりできます。

このコマンドは、クラスタ内のすべての Pod のログもダンプします。これらのログは、namespace と Pod 名に基づいて別々のディレクトリに出力されます。

## Examples

```bash
# 現在のクラスタの状態を標準出力にダンプする
oc cluster-info dump

# 現在のクラスタの状態を /path/to/cluster-state にダンプする
oc cluster-info dump --output-directory=/path/to/cluster-state

# すべての namespace を標準出力にダンプする
oc cluster-info dump --all-namespaces

# 指定した namespace 群を /path/to/cluster-state にダンプする
oc cluster-info dump --namespaces default,kube-system --output-directory=/path/to/cluster-state
```

## Options

- `-A, --all-namespaces=false`
  true の場合、すべての namespace をダンプします。true の場合、--namespaces は無視されます。

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--namespaces=[]`
  ダンプ対象の namespace をカンマ区切りで指定します。

- `-o, --output='json'`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--output-directory=''`
  ファイルの出力先。空または '-' の場合は標準出力に出力し、それ以外の場合はそのディレクトリ配下にディレクトリ階層を作成します

- `--pod-running-timeout=20s`
  少なくとも 1 つの Pod が実行状態になるまで待つ時間（5s、2m、3h のような 0 より大きい値）

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc cluster-info dump --help` / `gen-oc-help.py` で生成</sub>
