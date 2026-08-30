# `oc status`

> 現在のプロジェクトの概要を表示する

[`oc`](oc.md) / `status`

## Usage

```
oc status [-o dot | --suggest ] [flags] [options]
```

現在のプロジェクトの概要を表示します。

このコマンドは、Service、デプロイメント設定、ビルド設定、実行中のデプロイを表示します。設定に問題のあるコンポーネントがあれば、その情報も表示されます。個々の項目の詳細については describe コマンドを使用してください（例: oc describe buildconfig、oc describe deploymentconfig、oc describe service）。

出力形式に "-o dot" を指定すると、生成されたステータスグラフを "dot" コマンドで扱える DOT 形式で出力できます。

## Examples

```bash
# 現在のプロジェクトの概要を確認する
oc status

# 現在のプロジェクトの概要を svg ファイルに書き出す
oc status -o dot | dot -T svg -o project.svg

# 検出された問題の詳細を含めて、現在のプロジェクトの概要を確認する
oc status --suggest
```

## Options

- `-A, --all-namespaces=false`
  true の場合、すべての namespace のステータスを表示します（cluster admin 権限が必要）

- `-o, --output=''`
  出力形式。dot のみ指定できます。

- `--suggest=false`
  問題を解決するための詳細情報を表示する

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc status --help` / `gen-oc-help.py` で生成</sub>
