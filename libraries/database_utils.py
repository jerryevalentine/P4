import sqlite3
import pandas as pd

# Function to establish a database connection
def get_db_connection(database_path):
    try:
        conn = sqlite3.connect(database_path)
        print("Connected to database.")
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        return None

# Function to query the database table
def query_table(table_name, database_path, num_of_rows=None):
    try:
        conn = get_db_connection(database_path)
        if conn is None:
            return pd.DataFrame()
        
        if num_of_rows:
            query = f"SELECT * FROM {table_name} LIMIT {num_of_rows};"
        else:
            query = f"SELECT * FROM {table_name};"

        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"An error occurred querying the database: {e}")
        return pd.DataFrame()

# Function to get columns of a table
def get_columns(database_path, table_name):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]
    conn.close()
    return columns

# Function to get all table names in the database
def get_tables(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables
