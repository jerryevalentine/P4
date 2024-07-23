import openai
import sqlite3
import pandas as pd

def get_chatgpt_analysis(api_key, model_name, db_path, table_name='neural_network_results'):
    openai.api_key = api_key
    conn = sqlite3.connect(db_path)
    try:
        query = f"SELECT * FROM {table_name} WHERE model_name = ?"
        result = pd.read_sql_query(query, conn, params=(model_name,))
    except pd.io.sql.DatabaseError as e:
        conn.close()
        return f"Database error: {str(e)}"
    conn.close()
    
    if result.empty:
        return "No results found for the selected model."

    # Formatting the data for analysis
    analysis_text = f"This is a Logistic Regression Model. Analysis for Model: {model_name}\n\n"
    for _, row in result.iterrows():
        analysis_text += f"Table: {row['table_name']}\n"
        analysis_text += f"Loss: {row['loss']}\n"
        analysis_text += f"MAE: {row['mae']}\n"
        analysis_text += f"Val Loss: {row['val_loss']}\n"
        analysis_text += f"Val MAE: {row['val_mae']}\n\n"

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

def get_model_names_from_results2(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    query = "SELECT DISTINCT model_name FROM model_results2"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
