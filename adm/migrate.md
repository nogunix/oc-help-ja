# `oc adm migrate`

> クラスタ内のデータを移行する

[`oc`](../oc.md) / [`oc adm`](../adm.md) / `migrate`

## Usage

```
oc adm migrate [flags] [options]
```

クラスタ上のリソースを移行する

これらのコマンドは、管理者がクラスタの予防保守を行うのを支援します。

## Subcommands

- [`icsp`](migrate/icsp.md) — imagecontentsourcepolicy ファイルを imagedigestmirrorset ファイルに更新する
- [`template-instances`](migrate/template-instances.md) — テンプレートインスタンスが最新の group-version-kind を指すよう更新する

> 各コマンドの詳細については "oc adm migrate `<command>` --help" を使用してください。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm migrate --help` / `gen-oc-help.py` で生成</sub>
