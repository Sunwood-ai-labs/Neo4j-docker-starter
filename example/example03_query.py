from neo4j import GraphDatabase
from loguru import logger
from art import tprint

URI = "neo4j://localhost:7687"  
AUTH = ("neo4j", "your_password") 

try:
    tprint("example03_query.py")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session(database="neo4j") as session:
            result = session.run("MATCH (p:Person {name: $name}) RETURN p.name AS name, p.age AS age", name="John Doe")
            for record in result:
                logger.info(f"名前: {record['name']}, 年齢: {record['age']}")
except Exception as e:
    logger.error(f"エラーが発生しました: {e}")
