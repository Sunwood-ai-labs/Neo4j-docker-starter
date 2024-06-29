from neo4j import GraphDatabase
from loguru import logger
from art import tprint

URI = "neo4j://localhost:7687"  
AUTH = ("neo4j", "your_password") 

try:
    tprint("example04_update.py")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            session.run("MATCH (p:Person {name: $name}) SET p.age = $new_age", name="John Doe", new_age=35)
            logger.info("データを更新しました。")
except Exception as e:
    logger.error(f"エラーが発生しました: {e}")
