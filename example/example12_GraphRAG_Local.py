# %% [markdown]
# # ローカルNeo4jを使用したRAGアプリケーション
#
# このノートブックでは、ローカルのNeo4jインスタンスを使用してRAG（Retrieval-Augmented Generation）アプリケーションを実装する方法を詳細に説明します。

# %% [markdown]
# ## 1. Neo4j環境のセットアップ
#
# まず、必要なライブラリをインポートし、ローカルのNeo4jデータベースへの接続を設定します。

# %%
from langchain.graphs import Neo4jGraph

# ローカルのNeo4jデータベースの接続情報を設定
URI = "bolt://localhost:7687"  
AUTH = ("neo4j", "your_password") 

# Neo4jGraphオブジェクトを作成し、ローカルデータベースに接続
graph = Neo4jGraph(
    url=URI, 
    username=AUTH[0], 
    password=AUTH[1]
)

# %% [markdown]
# このコードブロックでは、ローカルで動作しているNeo4jデータベースへの接続を設定しています。`URI`は「neo4j://localhost:7687」に、`AUTH`はユーザー名とパスワードのタプルに設定されています。

# %% [markdown]
# ## 2. データセットのインポート
#
# 次に、サンプルデータをGitHubのGistから取得し、ローカルのNeo4jデータベースにインポートします。

# %%
import requests

# GitHubのGistからサンプルデータのJSONを取得
url = "https://gist.githubusercontent.com/tomasonjo/08dc8ba0e19d592c4c3cde40dd6abcc3/raw/da8882249af3e819a80debf3160ebbb3513ee962/microservices.json"
import_query = requests.get(url).json()['query']

# 取得したクエリを実行してデータをローカルのNeo4jにインポート
graph.query(
    import_query
)

# %% [markdown]
# ## 3. Neo4jベクトルインデックスの作成
#
# ここでは、OpenAIの埋め込みモデルを使用して、Neo4jのベクトルインデックスを作成します。

# %%
# %load_ext dotenv
# %dotenv ../.env

# %%
from dotenv import load_dotenv
from langchain.vectorstores.neo4j_vector import Neo4jVector
from langchain_community.embeddings import OllamaEmbeddings

# OpenAIのAPIキーを環境変数に設定
# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

ollama_embeddings = OllamaEmbeddings(
    model="llama3",
    # model_kwargs={"max_token": 1536}  # これにより出力次元が1536に設定されます
)

# Neo4jVectorオブジェクトを作成し、ローカルの既存のグラフからベクトルインデックスを生成
vector_index = Neo4jVector.from_existing_graph(
    ollama_embeddings,
    url=URI,
    username=AUTH[0],
    password=AUTH[1],
    index_name='tasks',
    node_label="Task",
    text_node_properties=['name', 'description', 'status'],
    embedding_node_property='embedding',
)

# %% [markdown]
# ## 4. ベクトル類似性検索の実行
#
# 作成したベクトルインデックスを使用して類似性検索を実行します。

# %%
# ベクトル類似性検索を実行
response = vector_index.similarity_search(
    "How will RecommendationService be updated?"
)
print(response[0].page_content)

# %% [markdown]
# ## 5. RetrievalQAモジュールの作成
#
# LangChainのRetrievalQAモジュールを使用して、ベクトル検索結果を基にした質問応答システムを構築します。

# %%
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOllama

ollama = ChatOllama(model="llama3")

# RetrievalQAオブジェクトを作成
vector_qa = RetrievalQA.from_chain_type(
    llm=ollama,
    chain_type="stuff",
    retriever=vector_index.as_retriever()
)

# 質問を実行
vector_qa.run(
    "How will recommendation service be updated?"
)

# %% [markdown]
# ## 6. Cypherクエリの生成と実行
#
# LangChainのGraphCypherQAChainを使用して、自然言語の質問からCypherクエリを生成し、実行します。

# %%
from langchain.chains import GraphCypherQAChain

# ローカルのグラフスキーマを更新
graph.refresh_schema()

# GraphCypherQAChainオブジェクトを作成
cypher_chain = GraphCypherQAChain.from_llm(
    cypher_llm = ollama,
    qa_llm = ollama, 
    graph=graph, 
    verbose=True,
)

# Cypherクエリを生成して実行
cypher_chain.run(
    "How many open tickets there are?"
)

# %% [markdown]
# ## 7. 知識グラフエージェントの作成
#
# 最後に、LangChainのエージェントフレームワークを使用して、ベクトル検索とグラフ検索の両方を組み合わせた知識グラフエージェントを作成します。

# %%
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

# ツールのリストを定義
tools = [
    Tool(
        name="Tasks",
        func=vector_qa.run,
        description="""Useful when you need to answer questions about descriptions of tasks.
        Not useful for counting the number of tasks.
        Use full question as input.
        """,
    ),
    Tool(
        name="Graph",
        func=cypher_chain.run,
        description="""Useful when you need to answer questions about microservices,
        their dependencies or assigned people. Also useful for any sort of 
        aggregation like counting the number of tasks, etc.
        Use full question as input.
        """,
    ),
]

# エージェントを初期化
mrkl = initialize_agent(
    tools, 
    ollama,
    agent=AgentType.OPENAI_FUNCTIONS, 
    verbose=True
)

# エージェントに質問を実行
response = mrkl.run("Which team is assigned to maintain PaymentService?")
print(response)

# %% [markdown]
# ## 注意点
#
# 1. ローカルのNeo4jインスタンスが正しく設定され、実行されていることを確認してください。
#
# 2. `AUTH`タプルの2番目の要素（`"your_password"`）を、実際のNeo4jパスワードに置き換えてください。
#
# 3. OpenAIのAPIキーを正しく設定していることを確認してください。環境変数`OPENAI_API_KEY`に有効なAPIキーを設定する必要があります。
#
# 4. このコードはローカル環境で動作するように設定されていますが、セキュリティに注意してください。本番環境では、パスワードやAPIキーを直接コードに記述せず、環境変数や安全な設定管理システムを使用することをお勧めします。
#
# 以上が、ローカルNeo4jを使用したRAGアプリケーションの実装方法です。このノートブックを実行することで、ローカル環境でGraphRAGシステムを構築し、テストすることができます。
