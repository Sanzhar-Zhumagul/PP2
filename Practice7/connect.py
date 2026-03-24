import psycopg2
from config import DB

def connect():
    return psycopg2.connect(**DB)