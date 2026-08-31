# CLAUDE.md — oc-help-ja

## プロジェクト概要

`oc`（OpenShift CLI）の `--help` 出力を日本語に翻訳し、Markdown ツリーとして管理するリポジトリ。

- リポジトリ: `nogunix/oc-help-ja`
- 生成スクリプト: `gen-oc-help.py`
- 翻訳カタログ: `i18n/ja.json`（msgid → msgstr の JSON）

## 成果物

| ファイル | 内容 |
|---|---|
| `*.md` / `**/*.md` | 日本語訳された各コマンドのヘルプ |
| `all.txt` | 生ヘルプの連結（grep 用） |
| `README.md` | 目次（自動生成） |
| `i18n/ja.json` | 翻訳カタログ |

## ヘルプ更新の手順

### 1. ヘルプテキスト再取得・再生成

```bash
python3 gen-oc-help.py            # all.txt, *.md, README.md を再生成
python3 gen-oc-help.py --extract  # 新しい msgid を i18n/ja.json に抽出
python3 gen-oc-help.py --stats    # 翻訳カバレッジを確認
```

`oc` はローカルにインストール済みのものを使う（`--oc` で指定可）。

### 2. 翻訳カバレッジ確認

`--stats` で未訳文字列がないか確認する。未訳があれば `i18n/ja.json` を編集して翻訳を追加してから再生成。

### 3. コミット・プッシュ

差分を確認してコミット。コミットメッセージは `oc <バージョン> のヘルプで all.txt と Markdown を再生成` のスタイル。

## GitHub Actions 自動更新

- ワークフロー: `.github/workflows/` 内の `Update oc help (Japanese)`
- スケジュール: 毎週月曜 09:00 UTC（JST 18:00）
- 手動実行: `gh workflow run "Update oc help (Japanese)"`
- 動作: Linux 版 `oc` をダウンロード → `--extract` → `--stats` → 再生成 → 差分があれば PR 自動作成

### 必要なリポジトリ設定

Settings → Actions → General → Workflow permissions:
- **Read and write permissions** を選択
- **Allow GitHub Actions to create and approve pull requests** にチェック

## 自動生成 PR の処理

Actions が作成した PR は以下の手順で処理する。

### 1. PR の内容確認

```bash
gh pr list --state open
gh pr view <PR番号>
gh pr diff <PR番号>
```

差分が `all.txt`、`*.md`、`README.md`、`i18n/ja.json` のヘルプ更新のみであることを確認する。

### 2. マージ

```bash
gh pr merge <PR番号> --merge --delete-branch
```

squash ではなく通常マージ。マージ後にリモートブランチを削除する。

### 3. ローカルの同期

```bash
git pull
```

## 一連の作業フロー（まとめ）

1. `gh run list` で Actions の実行結果を確認
2. 失敗していれば `gh run view <run-id>` で原因を調査・修正
3. 成功していれば `gh pr list` で PR を確認
4. `gh pr view` / `gh pr diff` で差分を確認
5. `gh pr merge --merge --delete-branch` でマージ
6. 必要に応じてローカルで `python3 gen-oc-help.py --stats` を実行し翻訳カバレッジを確認
7. 未訳があれば `i18n/ja.json` を編集 → `python3 gen-oc-help.py` で再生成 → コミット・プッシュ

## コマンドリファレンス

```bash
# ワークフロー手動実行
gh workflow run "Update oc help (Japanese)"

# 実行状況確認
gh run list --limit 5
gh run view <run-id>

# PR 確認・マージ
gh pr list --state open
gh pr view <PR番号>
gh pr diff <PR番号>
gh pr merge <PR番号> --merge --delete-branch
```
