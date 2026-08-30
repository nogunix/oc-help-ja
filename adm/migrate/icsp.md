# `oc adm migrate icsp`

> imagecontentsourcepolicy ファイルを imagedigestmirrorset ファイルに更新する

[`oc`](../../oc.md) / [`oc adm`](../../adm.md) / [`oc adm migrate`](../migrate.md) / `icsp`

## Usage

```
oc adm migrate icsp [flags] [options]
```

imagecontentsourcepolicy ファイルを imagedigestmirrorset ファイルに更新します。--dest-dir を指定しない場合、クラスタに追加できる imagedigestmirrorset ファイルがカレントディレクトリ配下に書き出されます。

## Examples

```bash
# imagecontentsourcepolicy.yaml ファイルを、mydir ディレクトリ配下の新しい imagedigestmirrorset ファイルに更新する
oc adm migrate icsp imagecontentsourcepolicy.yaml --dest-dir mydir
```

## Options

- `--dest-dir=''`
  imagedigestmirrorset ファイルを書き出す、ローカルマシン上のディレクトリを指定します。

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc adm migrate icsp --help` / `gen-oc-help.py` で生成</sub>
