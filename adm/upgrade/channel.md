# `oc adm upgrade channel`

> 更新チャネルを設定またはクリアする

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm upgrade`](../upgrade.md) / `channel`

## Usage

```
oc adm upgrade channel CHANNEL [flags] [options]
```

このコマンドは更新チャネルを設定またはクリアします。これは、そのクラスタに推奨される更新の一覧に影響します。

指定したチャネルが空の場合、このコマンドは更新チャネルをクリアします。許容されるチャネルのリストがあり、現在の更新チャネルがその中にある場合、クリアを実行するには --allow-explicit-channel を指定する必要があります。

指定したチャネルが空でない場合、このコマンドは更新チャネルをその値に設定します。許容されるチャネルのリストがあり、指定したチャネルがその中に無い場合、変更を実行するには --allow-explicit-channel を指定する必要があります。

## Options

- `--allow-explicit-channel=false`
  許容されるチャネルのリストがあり、指定したチャネルがその中に無い場合でも、チャネルを変更します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm upgrade channel --help` / `gen-oc-help.py` で生成</sub>
