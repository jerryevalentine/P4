import pandas as pd
import sqlite3

def get_table_names(db_path, table_name='neural_network_results'):
    conn = sqlite3.connect(db_path)
    query = f"SELECT DISTINCT model_name FROM {table_name}"
    model_names = pd.read_sql(query, conn)
    conn.close()
    return model_names['model_name'].tolist()

# Function to execute a SELECT query on a specific column in a table
def query_column(table_name, column_name, database_path, num_of_rows=None):
    try:
        conn = get_db_connection(database_path)
        if conn is None:
            return pd.DataFrame()
        
        if num_of_rows:
            query = f"SELECT {column_name} FROM {table_name} LIMIT {num_of_rows};"
        else:
            query = f"SELECT {column_name} FROM {table_name};"
        
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"An error occurred querying the database: {e}")
        return pd.DataFrame()

# Function to establish a database connection
def get_db_connection(database_path):
    try:
        conn = sqlite3.connect(database_path)
        print("Connected to database.")
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        return None

# Function to retrieve table names and columns from the database metadata
def get_metadata_tables(database_path):
    try:
        conn = get_db_connection(database_path)
        if conn is None:
            return {}
        
        query_tables = "SELECT name FROM sqlite_master WHERE type='table';"
        tables_df = pd.read_sql(query_tables, conn)
        tables = tables_df['name'].tolist()
        
        metadata = {}
        for table in tables:
            query_columns = f"PRAGMA table_info({table});"
            columns_df = pd.read_sql(query_columns, conn)
            columns = columns_df['name'].tolist()
            metadata[table] = columns
        
        conn.close()
        return metadata
    except Exception as e:
        print(f"An error occurred while retrieving the metadata: {e}")
        return {}

# Function to execute a SELECT query on a table
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

def query_model_names(database_path):
    conn = sqlite3.connect(database_path)
    query = f"SELECT model_name FROM neural_network_results;" 
    df = pd.read_sql(query, conn)
    conn.close()
    return df
