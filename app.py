from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

# Add the libraries directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'libraries'))

from libraries.chatgpt_utils import get_chatgpt_analysis, get_chatgpt_response, get_model_names_from_results2
from libraries.db_utils import query_table, get_metadata_tables



base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, 'resources', 'spotify.db')

# This is if it is set as an environment variable.
if not OPENAI_API_KEY:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/display_data', methods=['GET', 'POST'])
def display_data():
    metadata = get_metadata_tables(database_path)
    selected_table = None
    table_data = None
    if request.method == 'POST':
        selected_table = request.form.get('table')
        if selected_table:
            table_data = query_table(selected_table, database_path, num_of_rows=10)

    return render_template('display_data.html', metadata=metadata, selected_table=selected_table, table_data=table_data)

@app.route('/chatgpt_analysis', methods=['GET', 'POST'])
def chatgpt_analysis():
    if request.method == 'POST':
        model_name = request.form['model_name']
        # Fetch necessary data for ChatGPT analysis
        chatgpt_results = get_chatgpt_analysis(OPENAI_API_KEY, model_name, database_path, table_name='model_results2')
        return render_template('chatgpt_analysis.html', chatgpt_results=chatgpt_results)
    
    model_names = get_model_names_from_results2(database_path)
    return render_template('chatgpt_analysis.html', model_names=model_names)

@app.route('/chatgpt_conversation', methods=['GET', 'POST'])
def chatgpt_conversation():
    chatgpt_response = None
    if request.method == 'POST':
        user_input = request.form['user_input']
        chatgpt_response = get_chatgpt_response(OPENAI_API_KEY, user_input)
    
    return render_template('chatgpt_conversation.html', chatgpt_response=chatgpt_response)

if __name__ == '__main__':
    app.run(debug=True)
