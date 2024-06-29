from neo4j import GraphDatabase
from loguru import logger
from art import tprint

URI = "neo4j://localhost:7687" 
AUTH = ("neo4j", "your_password") 

def create_person_if_not_exists(tx, name):
    tx.run("MERGE (p:Person {name: $name})", name=name)

def create_friendship(tx, name1, name2):
    # 両方の人物を作成（存在しない場合）
    create_person_if_not_exists(tx, name1)
    create_person_if_not_exists(tx, name2)
    # 友好関係を作成
    tx.run("MATCH (p1:Person {name: $name1}), (p2:Person {name: $name2}) CREATE (p1)-[:FRIEND]->(p2)", name1=name1, name2=name2)

try:
    tprint("example06_transaction.py")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            session.execute_write(create_friendship, "Alice", "Bob")
            logger.info("AliceとBobのノードを作成し、友好関係を結びました。")
except Exception as e:
    logger.error(f"エラーが発生しました: {e}")
