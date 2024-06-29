<p align="center">
<img src="https://huggingface.co/datasets/MakiAi/IconAssets/resolve/main/neo4j-docker-starter.png" width="100%">
<br>
<h1 align="center">Neo4j-docker-starter</h1>
<h2 align="center">
  ～ Your Neo4j, in a Box. ～
<br>
 
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

Neo4j-docker-starterは、Docker Composeを使用してNeo4jグラフデータベース環境を簡単に構築し、Pythonを使ってデータベース操作を行うためのスターターキットです。

## 🚀 特徴

- Docker Composeを使用した簡単なNeo4j環境のセットアップ
- Pythonを使ったNeo4jデータベース操作の基本的な例
- 初心者にも分かりやすいステップバイステップの説明

## 📋 前提条件

- Docker
- Docker Compose
- Python 3.7以上

## 🛠 セットアップ

1. リポジトリをクローンします：

```bash
git clone https://github.com/Sunwood-ai-labs/Neo4j-docker-starter.git
cd Neo4j-docker-starter
```

2. `docker-compose.yml`ファイルを編集し、必要に応じてパスワードを変更します：

```yaml
environment:
  - NEO4J_AUTH=neo4j/your_password
```

3. Docker Composeを使用してNeo4jコンテナを起動します：

```bash
docker-compose up -d
```

4. 必要なPythonパッケージをインストールします：

```bash
pip install neo4j loguru art
```

## 📊 サンプルプログラム

`example`ディレクトリには、Neo4jデータベースの基本的な操作を示す6つのサンプルプログラムが含まれています：

1. **example01_connect.py**: Neo4jデータベースへの接続
2. **example02_create.py**: ノードの作成
3. **example03_query.py**: データのクエリ
4. **example04_update.py**: データの更新
5. **example05_delete.py**: データの削除
6. **example06_transaction.py**: トランザクションの使用

各サンプルプログラムは以下のように実行できます：

```bash
python example/example01_connect.py
```

## 🔧 使用方法

1. Neo4j Browserにアクセス：`http://localhost:7474`
2. ログイン情報を入力：
   - ユーザー名: `neo4j`
   - パスワード: `your_password`（docker-compose.ymlで設定したもの）
3. サンプルプログラムを実行して、Neo4jデータベースの基本的な操作を確認

## 🤝 コントリビューション

プルリクエストは大歓迎です。大きな変更の場合は、まずissueを開いて議論してください。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🙏 謝辞

- Neo4jコミュニティの皆様
- Docker Composeの開発者の皆様

---

開発者：Sunwood AI Labs
