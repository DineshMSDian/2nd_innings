import psycopg2
import os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

def get_connection():
    conn = psycopg2.connect(
        database = 'cricketiq',
        user = 'cricketiq_user',
        password = os.getenv('db_password'),
        host = 'localhost',
        port = '5432'
    )
    return conn