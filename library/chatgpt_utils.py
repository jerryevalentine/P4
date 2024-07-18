import openai
import sqlite3
import pandas as pd

def get_chatgpt_analysis(api_key, model_name, user_input, db_path):
    openai.api_key = api_key
    conn = sqlite3.connect(db_path)
    query = f"SELECT * FROM model_results WHERE model_name=?"
    result = pd.read_sql(query, conn, params=(model_name,))
    conn.close()
    
    if result.empty:
        return "No results found for the selected model."

    analysis_text = f"""
    This is a Logistic Regression Model.
    Model Name: {result['model_name'][0]}
    R-Squared: {result['r_squared'][0]}
    Confusion Matrix: {result['confusion_matrix'][0]}
    """
    
    combined_text = f"{user_input}\n\n{analysis_text}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": combined_text}
        ]
    )
    return response.choices[0].message['content'].strip()
