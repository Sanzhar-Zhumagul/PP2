import psycopg2
from config import DB
def connect():
    try:
        conn = psycopg2.connect(**DB)
        return conn
    except Exception as e:
        print("Connection error:", e)