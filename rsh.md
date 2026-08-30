# `oc rsh`

> コンテナ内でシェルセッションを開始する

[`oc`](oc.md) / `rsh`

## Usage

```
oc rsh [-c CONTAINER] [flags] (POD | TYPE/NAME) COMMAND [args...] [options]
```

コンテナへのリモートシェルセッションを開きます。

このコマンドは、指定したリソースの Pod 内でシェルセッションを開始しようとします。Pod、デプロイメント設定、デプロイメント、ジョブ、デーモンセット、レプリケーションコントローラー、レプリカセットに対して使用できます。Pod 以外のリソースを指定した場合は、準備完了状態の Pod に解決されます。コンテナを指定しなければ最初のコンテナが使われ、デフォルトのシェルとして '/bin/sh' の使用を試みます。このコマンドがサポートするフラグはリソース名より前に指定でき、リソース名の後にコマンドを指定すると、ログインシェルの代わりにそのコマンドが実行されます。標準入力が対話的な場合、TTY が自動的に割り当てられます。-t と -T で上書きできます。シェル（またはコマンド）が実行される環境には TERM 変数が渡されます。デフォルトの値はローカル環境の TERM と同じで、未設定の場合は 'xterm' が使われます。

コンテナによってはシェルが含まれていない場合があります。コマンドを直接実行したい場合は 'oc exec' を使用してください。

## Examples

```bash
# Pod 'foo' の最初のコンテナでシェルセッションを開く
oc rsh foo

# namespace 'bar' の Pod 'foo' の最初のコンテナでシェルセッションを開く
# （oc クライアント固有の引数は、リソース名とその引数より前に置く必要があります）
oc rsh -n bar foo

# Pod 'foo' の中で 'cat /etc/resolv.conf' コマンドを実行する
oc rsh foo cat /etc/resolv.conf

# 内部レジストリの設定を確認する
oc rsh dc/docker-registry cat config.yml

# ジョブの Pod 内にある 'index' という名前のコンテナでシェルセッションを開く
oc rsh -c index job/scheduled
```

## Options

- `-c, --container=''`
  コンテナ名。デフォルトは最初のコンテナです

- `-f, --filename=[]`
  リソース内で rsh するために使用する

- `-T, --no-tty=false`
  擬似端末の割り当てを無効にします

- `--pod-running-timeout=1m0s`
  少なくとも 1 つの Pod が実行状態になるまで待つ時間（5s、2m、3h のような 0 より大きい値）

- `--shell='/bin/sh'`
  シェルコマンドのパス

- `-t, --tty=false`
  擬似端末の割り当てを強制する

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc rsh --help` / `gen-oc-help.py` で生成</sub>
