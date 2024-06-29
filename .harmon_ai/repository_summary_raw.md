## Pegasus: ウェブサイトをMarkdownに変換するPythonパッケージ

[![Docker Pulls](https://img.shields.io/docker/pulls/{あなたのDocker Hubユーザーネーム}/pegasus?style=flat-square)](https://hub.docker.com/r/{あなたのDocker Hubユーザーネーム}/pegasus)
[![GitHub stars](https://img.shields.io/github/stars/{あなたのGitHubユーザーネーム}/pegasus-docker?style=flat-square)](https://github.com/{あなたのGitHubユーザーネーム}/pegasus-docker)

このリポジトリには、Docker Composeを使用してPegasusを簡単に実行するためのファイルが含まれています。Pegasusは、ウェブサイトを再帰的にクロールし、そのコンテンツを美しくフォーマットされたMarkdownドキュメントに変換する、パワフルで柔軟なPythonパッケージです。

### 機能

* **再帰的なクロール:** 指定されたURLから始まり、リンクをたどって関連するページを探索します。
* **美しいMarkdown変換:** HTMLコンテンツを構造化された読みやすいMarkdownファイルに変換します。
* **柔軟な設定:** クロールの深さ、変換するファイルの種類、出力ディレクトリなどをカスタマイズできます。
* **コマンドラインとPythonの両方から使用可能:** コマンドラインインターフェイス（CLI）から実行することも、Pythonスクリプトから直接使用することもできます。

### 使用方法

1. **リポジトリのクローン:**

```bash
git clone https://github.com/{あなたのGitHubユーザーネーム}/pegasus-docker.git
cd pegasus-docker
```

2. **Docker Composeファイルの編集:**

`docker-compose.yml` ファイルを開き、`command` セクションでPegasusに渡す引数を編集します。例：

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

Pegasusがクロールと変換を完了すると、Markdownファイルは`./output` ディレクトリに出力されます。

### コマンドラインオプション

Pegasus CLIで使用できるコマンドラインオプションの詳細については、Pegasusのドキュメントを参照してください: [https://pegasus-crawler.github.io/](https://pegasus-crawler.github.io/)

### Pythonからの使用

PegasusをPythonスクリプトから直接使用する方法については、Pegasusのドキュメントを参照してください: [https://pegasus-crawler.github.io/](https://pegasus-crawler.github.io/)

### ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細については、`LICENSE` ファイルを参照してください。
