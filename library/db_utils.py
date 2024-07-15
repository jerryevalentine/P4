from sqlalchemy import create_engine
import sqlite3
import pandas as pd

def connect_db(database_path): #Pass
    conn = sqlite3.connect(database_path)
    return conn

def get_metadata(database_path): #Pass
    conn = connect_db(database_path)
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql(query, conn)
    conn.close()
    return tables['name'].tolist()

def query_table(table_name, database_path, num_of_rows=None): #Passed
    conn = sqlite3.connect(database_path)
    
    if num_of_rows:
        query = f"SELECT * FROM {table_name} LIMIT {num_of_rows};"
    else:
        query = f"SELECT * FROM {table_name};"
    
    df = pd.read_sql(query, conn)
    conn.close()
    return df