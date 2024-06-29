# example01_connect.py
from neo4j import GraphDatabase
from loguru import logger
from art import tprint
import sys

URI = "neo4j://localhost:7687"  
AUTH = ("neo4j", "your_password")  

try:
    tprint("example01_connect.py")
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        logger.info("Neo4jデータベースに接続しました。")
except Exception as e:
    logger.error(f"エラーが発生しました: {e}")
