# `oc create ingress`

> 指定した名前で Ingress を作成する

[`oc`](../oc.md) / [`oc create`](../create.md) / `ingress`

## Usage

```
oc create ingress NAME --rule=host/path=service:port[,tls[=secret]]  [options]
```

エイリアス: ingress, ing

## Examples

```bash
# foo.com/bar へのリクエストを svc に転送する 'simple' という名前の Ingress を 1 つ作成する
# TLS シークレット "my-cert" を指定した svc1:8080
oc create ingress simple --rule="foo.com/bar=svc1:8080,tls=my-cert"

# "/path" をサービス svc:port に転送し、Ingress Class を "otheringress" とする catch-all の Ingress を作成する
oc create ingress catch-all --class=otheringress --rule="/path=svc:port"

# ingress.annotation1 と ingress.annotations2 の 2 つのアノテーションを付けて Ingress を作成する
oc create ingress annotated --class=default --rule="foo.com/bar=svc:port" \
--annotation ingress.annotation1=foo \
--annotation ingress.annotation2=bla

# 同一ホストで複数のパスを持つ Ingress を作成する
oc create ingress multipath --class=default \
--rule="foo.com/=svc:port" \
--rule="foo.com/admin/=svcadmin:portadmin"

# 複数のホストと pathType=Prefix を指定した Ingress を作成する
oc create ingress ingress1 --class=default \
--rule="foo.com/path*=svc:8080" \
--rule="bar.com/admin*=svc2:http"

# デフォルトの Ingress 証明書と複数の pathType を使って、TLS を有効にした Ingress を作成する
oc create ingress ingtls --class=default \
--rule="foo.com/=svc:https,tls" \
--rule="foo.com/path/subpath*=othersvc:8080"

# 特定のシークレットと pathType=Prefix を指定し、TLS を有効にした Ingress を作成する
oc create ingress ingsecret --class=default \
--rule="foo.com/*=svc:8080,tls=secret1"

# デフォルトバックエンド付きの Ingress を作成する
oc create ingress ingdefault --class=default \
--default-backend=defaultsvc:http \
--rule="foo.com/*=svc:8080,tls=secret1"
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--annotation=[]`
  Ingress オブジェクトに挿入するアノテーション。annotation=value の形式で指定します

- `--class=''`
  使用する Ingress Class

- `--default-backend=''`
  バックエンドのデフォルトサービス。svcname:port の形式で指定します

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `--rule=[]`
  host/path=service:port[,tls=secretname] の形式のルール。先頭に '*' を含むパスは pathType=Prefix として扱われます。tls 引数は省略可能です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

- `--validate='ignore'`
  strict（または true）、warn、ignore（または false）のいずれかを指定します。"true" または "strict" はスキーマで入力を検証し、不正ならリクエストを失敗させます。API サーバーで ServerSideFieldValidation が有効ならサーバー側で検証し、無効なら信頼性の低いクライアント側の検証にフォールバックします。"warn" は、API サーバーでサーバーサイドのフィールド検証が有効な場合、未知のフィールドや重複フィールドについてリクエストを止めずに警告し、そうでない場合は "ignore" と同じ動作になります。"false" または "ignore" はスキーマ検証を一切行わず、未知のフィールドや重複フィールドを黙って捨てます。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc create ingress --help` / `gen-oc-help.py` で生成</sub>
