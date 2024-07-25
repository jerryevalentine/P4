import openai
import sqlite3
import pandas as pd

def get_db_connection(database_path):
    try:
        conn = sqlite3.connect(database_path)
        print("Connected to database.")
        return conn
    except Exception as e:
        print(f"Failed to connect to database: {e}")
        return None

def get_chatgpt_analysis(api_key, model_name, database_path, table_name='neural_network_results', user_input=''):
    openai.api_key = api_key
    conn = sqlite3.connect(database_path)
    
    try:
        # Fetch model results
        query = f"SELECT * FROM {table_name} WHERE model_name = ?"
        result = pd.read_sql_query(query, conn, params=(model_name,))
        
        # Fetch data dictionary
        data_dictionary_query = "SELECT * FROM data_dictionary"
        conn = get_db_connection(database_path)
        data_dictionary = pd.read_sql_query(data_dictionary_query, conn)
        
    except pd.io.sql.DatabaseError as e:
        conn.close()
        return f"Database error: {str(e)}"
    
    conn.close()
    
    if result.empty:
        return "No results found for the selected model."
    
    # Check for expected columns in data dictionary
    expected_columns = {'variable', 'class', 'description'}
    actual_columns = set(data_dictionary.columns)
    
    missing_columns = expected_columns - actual_columns
    if missing_columns:
        return f"Missing columns in data dictionary: {', '.join(missing_columns)}"
    
    # Formatting the data for analysis
    analysis_text = f"This is a Neural Network Model. Please acknowledge receipt of the data dictionary. Also, please provide the analysis for Model: {model_name}\n\n"
    
    for _, row in result.iterrows():
        analysis_text += f"Table: {row.get('table_name', 'N/A')}\n"
        analysis_text += f"Loss: {row.get('loss', 'N/A')}\n"
        analysis_text += f"MAE: {row.get('mae', 'N/A')}\n"
        analysis_text += f"Val Loss: {row.get('val_loss', 'N/A')}\n"
        analysis_text += f"Val MAE: {row.get('val_mae', 'N/A')}\n\n"
    
    analysis_text += "Data Dictionary:\n"
    for _, row in data_dictionary.iterrows():
        analysis_text += f"Variable: {row.get('variable', 'N/A')}, Class: {row.get('class', 'N/A')}, Description: {row.get('description', 'N/A')}\n"
    
    if user_input:
        analysis_text += f"\nUser Input: {user_input}\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": analysis_text}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"OpenAI error: {str(e)}"

def get_chatgpt_response(api_key, user_input):
    openai.api_key = api_key
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"OpenAI error: {str(e)}"
