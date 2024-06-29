<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/neo4j-docker-starter.png" width="100%">
<br>
<h1 align="center">Neo4j-docker-starter</h1>
<h2 align="center">
  ～ Your Neo4j, in a Box. ～
<br>
  <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/Neo4j-docker-starter-SURF">
<img alt="PyPI - Format" src="https://img.shields.io/pypi/format/Neo4j-docker-starter-SURF">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/Neo4j-docker-starter-SURF">
<img alt="PyPI - Status" src="https://img.shields.io/pypi/status/Neo4j-docker-starter-SURF">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dd/Neo4j-docker-starter-SURF">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/Neo4j-docker-starter-SURF">
<a href="https://github.com/Sunwood-ai-labs/Neo4j-docker-starter" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=Neo4j-docker-starter&message=Sunwood-ai-labs&color=blue&logo=github"></a>
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/Neo4j-docker-starter">
<a href="https://github.com/Sunwood-ai-labs/Neo4j-docker-starter"><img alt="forks - Sunwood-ai-labs" src="https://img.shields.io/github/forks/Neo4j-docker-starter/Sunwood-ai-labs?style=social"></a>
<a href="https://github.com/Sunwood-ai-labs/Neo4j-docker-starter"><img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/Neo4j-docker-starter"></a>
<a href="https://github.com/Sunwood-ai-labs/Neo4j-docker-starter"><img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/Neo4j-docker-starter"></a>
<img alt="GitHub Release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/Neo4j-docker-starter?color=red">
<img alt="GitHub Tag" src="https://img.shields.io/github/v/tag/Sunwood-ai-labs/Neo4j-docker-starter?sort=semver&color=orange">
<img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Sunwood-ai-labs/Neo4j-docker-starter/publish-to-pypi.yml">
<br>
<p align="center">
  <a href="https://hamaruki.com/"><b>[🌐 Website]</b></a> •
  <a href="https://github.com/Sunwood-ai-labs"><b>[🐱 GitHub]</b></a>
  <a href="https://x.com/hAru_mAki_ch"><b>[🐦 Twitter]</b></a> •
  <a href="https://hamaruki.com/"><b>[🍀 Official Blog]</b></a>
</p>

</h2>

</p>

>[!IMPORTANT]
>このリポジトリのリリースノートやREADME、コミットメッセージの9割近くは[claude.ai](https://claude.ai/)や[ChatGPT4](https://chatgpt.com/)を活用した[AIRA](https://github.com/Sunwood-ai-labs/AIRA), [SourceSage](https://github.com/Sunwood-ai-labs/SourceSage), [Gaiah](https://github.com/Sunwood-ai-labs/Gaiah), [HarmonAI_II](https://github.com/Sunwood-ai-labs/HarmonAI_II)で生成しています。

## 🌟 はじめに

このリポジトリには、Docker Compose を使用して Pegasus を簡単に実行するためのファイルが含まれています。Pegasus は、ウェブサイトを再帰的にクロールし、そのコンテンツを美しくフォーマットされた Markdown ドキュメントに変換する、パワフルで柔軟な Python パッケージです。

## 🎥 デモ

（デモ動画またはスクリーンショットがあればここに挿入）

## 🚀 はじめよう

1. **リポジトリのクローン:**

```bash
git clone https://github.com/{あなたのGitHubユーザーネーム}/pegasus-docker.git
cd pegasus-docker
```

2. **Docker Compose ファイルの編集:**

`docker-compose.yml` ファイルを開き、`command` セクションで Pegasus に渡す引数を編集します。例：

```yaml
version: "3.9"
services:
  pegasus:
    image: pegasus-crawler/pegasus
    command: ["pegasus", "https://www.example.com", "-o", "/data"]
    volumes:
      - ./output:/data
```

* `https://www.example.com` をクロールしたいウェブサイトのURLに置き換えます。
* `-o /data` は、Markdownファイルの出力先ディレクトリを指定します。これはコンテナ内の `/data` ディレクトリにマウントされます。

3. **Pegasusの実行:**

```bash
docker-compose up -d
```

4. **結果の確認:**

Pegasus がクロールと変換を完了すると、Markdown ファイルは `./output` ディレクトリに出力されます。

## 📝 更新情報

（更新情報があればここに記載）

## ✨ 機能

* **再帰的なクロール:** 指定された URL から始まり、リンクをたどって関連するページを探索します。
* **美しい Markdown 変換:** HTML コンテンツを構造化された読みやすい Markdown ファイルに変換します。
* **柔軟な設定:** クロールの深さ、変換するファイルの種類、出力ディレクトリなどをカスタマイズできます。
* **コマンドラインと Python の両方から使用可能:** コマンドラインインターフェイス（CLI）から実行することも、Python スクリプトから直接使用することもできます。

## 🤝 コントリビュート

（コントリビュートの方法があればここに記載）

## 📄 ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細については、`LICENSE` ファイルを参照してください。

## 🙏 謝辞

（謝辞があればここに記載）
