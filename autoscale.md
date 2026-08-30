# `oc autoscale`

> デプロイメント設定、デプロイメント、レプリカセット、ステートフルセット、またはレプリケーションコントローラーをオートスケールする

[`oc`](oc.md) / `autoscale`

## Usage

```
oc autoscale (-f FILENAME | TYPE NAME | TYPE/NAME) [--min=MINPODS] --max=MAXPODS [--cpu=CPU] [--memory=MEMORY] [options]
```

Kubernetes クラスタで実行する Pod 数を自動的に決定・設定するオートスケーラーを作成します。このコマンドはまず autoscaling/v2 API の使用を試み、エラーになった場合は autoscaling/v1 API にフォールバックします。

デプロイメント、レプリカセット、ステートフルセット、またはレプリケーションコントローラーを名前で検索し、そのリソースを参照するオートスケーラーを作成します。オートスケーラーは、必要に応じてシステム内にデプロイされる Pod 数を自動的に増減できます。

## Examples

```bash
# デプロイメント "foo" を Pod 数 2〜10 でオートスケールする。目標 CPU 使用率を指定していないため、デフォルトのオートスケーリングポリシーが使用される
oc autoscale deployment foo --min=2 --max=10

# レプリケーションコントローラー "foo" を、Pod 数 1〜5、CPU 使用率の目標 80% でオートスケールする
oc autoscale rc foo --max=5 --cpu=80%

# デプロイメント "bar" を、Pod 数 3〜6、平均 CPU の目標 500m、メモリの目標 200Mi でオートスケールする
oc autoscale deployment bar --min=3 --max=6 --cpu=500m --memory=200Mi

# デプロイメント "bar" を、Pod 数 2〜8、CPU 使用率の目標 60%、メモリ使用率の目標 70% でオートスケールする
oc autoscale deployment bar --min=3 --max=6 --cpu=60% --memory=70%
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--cpu=''`
  すべての Pod にわたる目標 CPU 使用率。パーセンテージで指定した場合（要求 CPU の 70% なら "70%"）は平均使用率を目標にし、量で指定した場合（500 ミリ CPU なら "500m"）は平均値を目標にします。単位なしの値は、ミリ CPU を単位とする量として扱われます（"500" は "500m"）。

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-autoscale'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `-f, --filename=[]`
  オートスケール対象のリソースを特定するファイル名、ディレクトリ、または URL。

- `-k, --kustomize=''`
  kustomization ディレクトリを処理します。このフラグは -f や -R と併用できません。

- `--max=-1`
  オートスケーラーが設定できる Pod 数の上限。必須です。

- `--memory=''`
  すべての Pod にわたる目標メモリ使用率。パーセンテージで指定した場合（要求メモリの 60% なら "60%"）は平均使用率を目標にし、量で指定した場合（200 MiB なら "200Mi"、1 GiB なら "1Gi"）は平均値を目標にします。単位なしの値は、メビバイトを単位とする量として扱われます（"200" は "200Mi"）。

- `--min=-1`
  オートスケーラーが設定できる Pod 数の下限。指定しない場合や負の値の場合、サーバーがデフォルト値を適用します。

- `--name=''`
  新しく作成するオブジェクトの名前。指定しない場合は、入力リソースの名前が使用されます。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=false`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--save-config=false`
  true の場合、現在のオブジェクトの設定がそのアノテーションに保存されます。false の場合、アノテーションは変更されません。このフラグは、今後このオブジェクトに対して kubectl apply を実行したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc autoscale --help` / `gen-oc-help.py` で生成</sub>
