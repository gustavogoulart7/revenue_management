from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()


connect = psycopg2.connect(
    database = os.getenv("database"),
    user = os.getenv("user"),
    password = os.getenv("password"),
    host = os.getenv("host"),
    port = os.getenv("port")
)

cursor = connect.cursor()