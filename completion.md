# `oc completion`

> 指定したシェル (bash, zsh, fish, powershell) 用のシェル補完コードを出力する

[`oc`](oc.md) / `completion`

## Usage

```
oc completion SHELL [options]
```

指定したシェル (bash または zsh) 用のシェル補完コードを出力します。oc コマンドの対話的な補完を有効にするには、このコードを評価する必要があります。.bash_profile から source して読み込むとよいでしょう。

zsh ユーザーへの注意: [1] zsh の補完は zsh 5.2 以降でのみサポートされます

## Examples

```bash
# macOS で homebrew を使って bash 補完をインストールする
## If running Bash 3.2 included with macOS
brew install bash-completion
## or, if running Bash 4.1+
brew install bash-completion@2
## If oc is installed via homebrew, this should start working immediately
## If you've installed via other means, you may need add the completion to your completion directory
oc completion bash > $(brew --prefix)/etc/bash_completion.d/oc

# Linux で bash 補完をインストールする
## If bash-completion is not installed on Linux, install the 'bash-completion' package
## via your distribution's package manager.
## Load the oc completion code for bash into the current shell
source <(oc completion bash)
## Write bash completion code to a file and source it from .bash_profile
oc completion bash > ~/.kube/completion.bash.inc
printf "
# oc のシェル補完
source '$HOME/.kube/completion.bash.inc'
" >> $HOME/.bash_profile
source $HOME/.bash_profile

# zsh[1] 用の oc 補完コードを現在のシェルに読み込む
source <(oc completion zsh)
# zsh[1] 用の oc 補完コードを起動時に autoload するよう設定する
oc completion zsh > "${fpath[1]}/_oc"

# fish[2] 用の oc 補完コードを現在のシェルに読み込む
oc completion fish | source
# セッションごとに補完を読み込ませるには、次を 1 回実行します:
oc completion fish > ~/.config/fish/completions/oc.fish

# powershell 用の oc 補完コードを現在のシェルに読み込む
oc completion powershell | Out-String | Invoke-Expression
# powershell 用の oc 補完コードを起動時に実行するよう設定する
## Save completion code to a script and execute in the profile
oc completion powershell > "$HOME\.kube\completion.ps1"
Add-Content $PROFILE ". '$HOME\.kube\completion.ps1'"
## Execute completion code in the profile
Add-Content $PROFILE "if (Get-Command oc -ErrorAction SilentlyContinue) {
oc completion powershell | Out-String | Invoke-Expression
}"
## Add completion code directly to the $PROFILE script
oc completion powershell >> $PROFILE
```

> すべてのコマンドに共通するグローバルオプションの一覧は "oc options" で確認できます。

---

<sub>`$ oc completion --help` / `gen-oc-help.py` で生成</sub>
