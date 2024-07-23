import pandas as pd

#Loads a csv file, from csv_file_path, into a dataframe
def load_csv_to_dataframe(csv_file_path):
    try:
        dataframe = pd.read_csv(csv_file_path)
        print(f"Dataframe loaded from {csv_file_path}")
        return dataframe
    except Exception as e:
        print(f"An error occurred while loading the CSV file: {e}")
        return None

# Drops column names from the list sent to the function (columns)
def drop_columns_dataframe(df, columns):
    try:
        df.drop(columns=columns, axis=1, inplace=True)
        return df
    except Exception as e:
        print(f"An error occurred while dropping columns from dataframe: {e}")
        return None
    
#Saves a dataframe to a CSV file.
def save_dataframe_to_csv(dataframe, file_name):
    try:
        csv_file_name = f"{file_name}.csv"
        dataframe.to_csv(csv_file_name, index=False)
        print(f"Dataframe saved to {csv_file_name}")
    except Exception as e:
        print(f"An error occurred while saving dataframe to the CSV file: {e}")
        return None
    
import pandas as pd
import sqlite3

def load_dataframe_to_db(df, table_name, db_path):
    """
    Load a DataFrame into a SQLite database table.

    Parameters:
    - df (pd.DataFrame): The DataFrame to be loaded.
    - table_name (str): The name of the table in the database.
    - db_path (str): Path to the SQLite database file.
    """
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_path)
    
    try:
        # Load the DataFrame into the SQLite table
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"DataFrame loaded into table '{table_name}' successfully.")
    except Exception as e:
        print(f"Error loading DataFrame into table '{table_name}': {e}")
    finally:
        # Close the connection
        conn.close()

def get_dataframe_statistics(df):
    """
    This function returns descriptive statistics for each numeric column in the given pandas DataFrame,
    with all values formatted to two decimal places.
    
    Parameters:
    df (pandas.DataFrame): The input DataFrame.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the descriptive statistics for each numeric column,
                      with values formatted to two decimal places.
    """
    stats_df = df.describe().round(2)
    return stats_df
