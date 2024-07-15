from flask import Flask, render_template, request
import os
import sys

library_directory = os.path.abspath('C:\\Users\\jerry\\Programming\\P4\\library')
if library_directory not in sys.path:
    sys.path.append(library_directory)
from test_utils import helloworld
from db_utils import query_table, get_metadata

database_path = r'C:\Users\jerry\Programming\P4\resources\spotify.db'

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/helloworld') 
def display_helloworld(): 
    message = helloworld()  # Call the function to get the message
    return render_template('helloworld.html', message=message)  # Pass the message to the template
###
@app.route('/display_data', methods=['GET', 'POST'])
def display_data():
    tables = get_metadata(database_path)
    selected_table = None
    table_data = None

    if request.method == 'POST':
        selected_table = request.form.get('table')
        if selected_table:
            table_data = query_table(selected_table, database_path, num_of_rows = 10)

    return render_template('display_data.html', tables=tables, selected_table=selected_table, table_data=table_data)
###
@app.route('/EDA') 
def EDA(): 
    return render_template('EDA.html')

@app.route('/ChatGPT') 
def ChatGPT(): 
    return render_template('ChatGPT.html')

@app.route('/model_prediction') 
def model_prediction(): 
    return render_template('model_prediction.html')

@app.route('/model_results') 
def model_results(): 
    return render_template('model_results.html')

if __name__ == '__main__':
    app.run(debug=True)