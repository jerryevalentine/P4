from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

from libraries.db_utils import query_table, get_metadata_tables

base_dir = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(base_dir, 'resources', 'spotify.db')

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

if __name__ == '__main__':
    app.run(debug=True)
