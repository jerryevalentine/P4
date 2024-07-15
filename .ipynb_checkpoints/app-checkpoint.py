from flask import Flask, render_template 
import os
import sys

library_directory = os.path.abspath('C:\\Users\\jerry\\Programming\\library')
if library_directory not in sys.path:
    sys.path.append(library_directory)
from test_utils import helloworld 

app = Flask(__name__)

@app.route('/') 
def index(): 
    return render_template('index.html') 

@app.route('/helloworld') 
def display_helloworld(): 
    message = helloworld()  # Call the function to get the message
    return render_template('helloworld.html', message=message)  # Pass the message to the template

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