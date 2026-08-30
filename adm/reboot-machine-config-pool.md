# `oc adm reboot-machine-config-pool`

> 指定した MachineConfigPool の再起動を開始する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `reboot-machine-config-pool`

## Usage

```
oc adm reboot-machine-config-pool [options]
```

適切な MachineConfig を変更することで、指定した machine config pool を再起動します。

再起動の完了は待たず、開始するだけです。このコマンドは一時停止中のプールを尊重します。Degraded、failed、その他の正常でないノードは再起動されません。

実験的機能: このコマンドは現在活発に開発中であり、予告なく変更される可能性があります。

## Examples

```bash
# すべての MachineConfigPool を再起動する
oc adm reboot-machine-config-pool mcp/worker mcp/master

# worker を継承するすべての MachineConfigPool を再起動する。カスタムの MachineConfigPool と infra もすべて含まれる
oc adm reboot-machine-config-pool mcp/worker

# master を再起動する
oc adm reboot-machine-config-pool mcp/master
```

## Options

- `--allow-missing-template-keys=true`
  true の場合、テンプレート内でフィールドやマップのキーが見つからなくても、テンプレートのエラーを無視します。golang と jsonpath の出力形式にのみ適用されます。

- `--dry-run=false`
  サーバーサイドの dry run を使用する場合に true を設定します。

- `-f, --filename=[]`
  リソースを特定する。

- `-o, --output=''`
  出力形式。次のいずれかを指定します: (json, yaml, kyaml, name, go-template, go-template-file, template, templatefile, jsonpath, jsonpath-as-json, jsonpath-file)。

- `-R, --recursive=true`
  -f, --filename で指定したディレクトリを再帰的に処理します。関連するマニフェストを同じディレクトリにまとめて管理したい場合に便利です。

- `--show-managed-fields=false`
  true の場合、オブジェクトを JSON または YAML 形式で出力する際に managedFields を残します。

- `--template=''`
  -o=go-template、-o=go-template-file を使う場合のテンプレート文字列、またはテンプレートファイルのパス。形式は golang テンプレート [http://golang.org/pkg/text/template/#pkg-overview] です。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm reboot-machine-config-pool --help` / `gen-oc-help.py` で生成</sub>
