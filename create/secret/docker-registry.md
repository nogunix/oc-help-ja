# `oc create secret docker-registry`

> Docker レジストリで使用するシークレットを作成する

[`oc`](../../oc.md) / [`oc create`](../../create.md) / [`oc create secret`](../secret.md) / `docker-registry`

## Usage

```
oc create secret docker-registry NAME --docker-username=user --docker-password=password --docker-email=email [--docker-server=string] [--from-file=[key=]source] [--dry-run=server|client|none] [options]
```

Docker レジストリで使用する新しいシークレットを作成します。

        Dockercfg secrets are used to authenticate against Docker registries.
        When using the Docker command line to push images, you can authenticate to a given registry by running:
        '$ docker login DOCKER_REGISTRY_SERVER --username=DOCKER_USER --password=DOCKER_PASSWORD --email=DOCKER_EMAIL'.
これにより ~/.dockercfg ファイルが生成され、以降の 'docker push' や 'docker pull' コマンドがレジストリへの認証に使用します。メールアドレスは省略可能です。

        When creating applications, you may have a Docker registry that requires authentication.  In order for the
        nodes to pull images on your behalf, they must have the credentials.  You can provide this information
        by creating a dockercfg secret and attaching it to your service account.

## Examples

```bash
# .dockercfg ファイルをまだ持っていない場合は、dockercfg シークレットを直接作成する
oc create secret docker-registry my-secret --docker-server=DOCKER_REGISTRY_SERVER --docker-username=DOCKER_USER --docker-password=DOCKER_PASSWORD --docker-email=DOCKER_EMAIL

# ~/.docker/config.json から my-secret という名前のシークレットを新規作成する
oc create secret docker-registry my-secret --from-file=path/to/.docker/config.json
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--append-hash=false`
  シークレットの名前に、その内容のハッシュを付加します。

- `--docker-email=''`
  Docker レジストリ用のメールアドレス

- `--docker-password=''`
  Docker レジストリ認証用のパスワード

- `--docker-server='https://index.docker.io/v1/'`
  Docker レジストリのサーバーの場所

- `--docker-username=''`
  Docker レジストリ認証用のユーザー名

- `--dry-run='none'`
  "none"、"server"、"client" のいずれかを指定します。client の場合は、送信されるはずのオブジェクトを送信せずに表示するだけです。server の場合は、リソースを永続化せずにサーバー側へリクエストを送ります。

- `--field-manager='kubectl-create'`
  フィールドの所有権の追跡に使用するマネージャー名。

- `--from-file=[]`
  キーとなるファイルは、パスだけを指定するとデフォルト名 .dockerconfigjson が付けられます。名前とパスを組み合わせて指定した場合は、指定した名前が使われます。ディレクトリを指定した場合は、有効なシークレットキーとなるディレクトリ内の各ファイルを処理します。このコマンドでは、キーは常に .dockerconfigjson にしてください。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

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

<sub>`$ oc create secret docker-registry --help` / `gen-oc-help.py` で生成</sub>
