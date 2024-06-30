# %% [markdown]
# ## はじめに
#
# データサイエンスの世界では、効率的なコード管理とテキスト解析が重要な役割を果たしています。本記事では、テキスト埋め込みを可能にする Ollama Embeddings について詳しく解説します。

# %% [markdown]
# ## Ollama Embeddings: テキスト解析の新たな地平

# %% [markdown]
# ### Ollama Embeddings の概要
#
# Ollama Embeddings は、テキストデータを数値ベクトルに変換する強力なツールです。これにより、自然言語処理タスクや検索システムの性能を大幅に向上させることが可能になります。

# %% [markdown]
# ### Ollama Embeddings のセットアップ
#
# まずは、必要なライブラリをインストールしましょう。

# %%
# !pip install langchain-community

# %% [markdown]
# 次に、Ollama Embeddings クラスをインポートします。

# %%
from langchain_community.embeddings import OllamaEmbeddings

# Ollama Embeddings のインスタンスを作成
# デフォルトでは llama2 モデルを使用します
embeddings = OllamaEmbeddings(model="llama3")

# テスト用のテキストを用意
text = "これは日本語のテストドキュメントです。"

# %% [markdown]
# ### テキストの埋め込み
#
# Ollama Embeddings を使用して、テキストを数値ベクトルに変換します。

# %%
# 単一のテキストを埋め込みベクトルに変換
query_result = embeddings.embed_query(text)

# 結果の最初の5要素を表示
print("クエリの埋め込み結果（最初の5要素）:")
print(query_result[:5])

# %% [markdown]
# 上記のコードでは、以下の処理を行っています：
# 1. `embed_query` メソッドを使って、単一のテキストを埋め込みベクトルに変換しています。
# 2. 得られた埋め込みベクトルの最初の5要素を表示しています。これにより、ベクトルの一部を確認できます。

# %% [markdown]
# 複数のテキストを同時に埋め込むこともできます。

# %%
# 複数のテキストを埋め込みベクトルに変換
doc_result = embeddings.embed_documents([text])

# 結果の最初の5要素を表示
print("ドキュメントの埋め込み結果（最初の5要素）:")
print(doc_result[0][:5])

# %% [markdown]
# このコードでは：
# 1. `embed_documents` メソッドを使用して、テキストのリストを埋め込みベクトルに変換しています。
# 2. 結果は、各テキストに対応する埋め込みベクトルのリストとなります。
# 3. 最初のテキストの埋め込みベクトルの最初の5要素を表示しています。

# %% [markdown]
# ### 異なる埋め込みモデルの使用
#
# Ollama は、様々な埋め込みモデルをサポートしています。ここでは、より軽量なモデルである `mxbai-embed-large` を使用する例を示します。

# %%
# mxbai-embed-large モデルを使用して Ollama Embeddings のインスタンスを作成
embeddings_light = OllamaEmbeddings(model="mxbai-embed-large")

# テスト用のテキスト
text = "これは日本語のテストドキュメントです。"

# クエリの埋め込み
query_result = embeddings_light.embed_query(text)

print("軽量モデルによるクエリの埋め込み結果（最初の5要素）:")
print(query_result[:5])

# %% [markdown]
# このコードでは：
# 1. `OllamaEmbeddings` クラスのインスタンスを作成する際に、`model` パラメータで使用するモデルを指定しています。
# 2. 指定したモデルを使用してテキストの埋め込みを行っています。
# 3. 結果の最初の5要素を表示して、埋め込みベクトルの一部を確認しています。

# %% [markdown]
# ## まとめ
#
# 本記事では、Jupytext と Ollama Embeddings という2つの強力なツールについて解説しました。
#
# - **Jupytext** は、Jupyter ノートブックをテキストベースで管理することを可能にし、バージョン管理や共同作業を容易にします。
# - **Ollama Embeddings** は、テキストデータを数値ベクトルに変換する機能を提供し、自然言語処理タスクの性能向上に貢献します。
#
# これらのツールを活用することで、データサイエンスプロジェクトの効率と品質を大幅に向上させることができるでしょう。ぜひ、あなたのワークフローに取り入れてみてください。

# %% [markdown]
# ## 参考資料
#
# - Jupytext 公式ドキュメント: [https://jupytext.readthedocs.io/](https://jupytext.readthedocs.io/)
# - Ollama 公式ウェブサイト: [https://ollama.ai/](https://ollama.ai/)
# - LangChain ドキュメント: [https://python.langchain.com/](https://python.langchain.com/)
#
# この記事が、あなたのデータサイエンスの旅に新たな視点をもたらすことを願っています。さらに詳しい情報や、実際の使用例については、上記の参考資料をご覧ください。
