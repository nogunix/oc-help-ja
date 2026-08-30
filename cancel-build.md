# `oc cancel-build`

> 実行中・保留中・新規のビルドをキャンセルする

[`oc`](oc.md) / `cancel-build`

## Usage

```
oc cancel-build (BUILD | BUILDCONFIG) [flags] [options]
```

このコマンドは、ビルドの正常な停止を要求します。要求してから実際にビルドが終了するまでには、多少の時間差が生じることがあります。

## Examples

```bash
# 指定した名前のビルドをキャンセルする
oc cancel-build ruby-build-2

# 指定した名前のビルドをキャンセルし、ビルドログを表示する
oc cancel-build ruby-build-2 --dump-logs

# 指定した名前のビルドをキャンセルし、同じパラメータで新しいビルドを作成する
oc cancel-build ruby-build-2 --restart

# 複数のビルドをキャンセルする
oc cancel-build ruby-build-1 ruby-build-2 ruby-build-3

# 'ruby-build' ビルド設定から作成された 'new' 状態のビルドをすべてキャンセルする
oc cancel-build bc/ruby-build --state=new
```

## Options

- `--dump-logs=false`
  キャンセルしたビルドのビルドログを表示するかどうかを指定します。

- `--restart=false`
  現在のビルドをキャンセルした後、新しいビルドを作成するかどうかを指定します。

- `--state=[new,pending,running]`
  この状態のビルドのみをキャンセルします

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc cancel-build --help` / `gen-oc-help.py` で生成</sub>
