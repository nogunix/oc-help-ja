# `oc adm certificate approve`

> 証明書署名要求を承認する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm certificate`](../certificate.md) / `approve`

## Usage

```
oc adm certificate approve (-f FILENAME | NAME) [options]
```

oc adm certificate approve を使うと、クラスタ管理者は証明書署名要求 (CSR) を承認できます。この操作により、証明書署名コントローラーは、CSR で要求された属性を持つ証明書を要求者に発行します。

セキュリティに関する注意: 要求された属性によっては、発行された証明書によって、要求者がクラスタリソースへアクセスしたり、要求された identity として認証したりできる可能性があります。CSR を承認する前に、その署名済み証明書で何ができるのかを必ず理解してください。

## Examples

```bash
# CSR 'csr-sqgzp' を承認する
oc adm certificate approve csr-sqgzp
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `-f, --filename=[]`
  更新するリソースを特定するファイル名、ディレクトリ、または URL

- `--force=false`
  既に承認済みであっても CSR を更新します。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm certificate approve --help` / `gen-oc-help.py` で生成</sub>
