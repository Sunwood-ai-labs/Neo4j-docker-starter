from neo4j import GraphDatabase
from loguru import logger
from art import tprint

URI = "neo4j://localhost:7687"  
AUTH = ("neo4j", "your_password") 

try:
    tprint("example02_create.py")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            session.run("CREATE (p:Person {name: $name, age: $age})", name="John Doe", age=30)
            logger.info("データを作成しました。")
except Exception as e:
    logger.error(f"エラーが発生しました: {e}")
