from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data-dictionary')
def data_dictionary():
    df = pd.read_csv('datadictionary.csv')
    return render_template('data_dictionary.html', tables=df.to_html(classes='data', header="true", index=False))

@app.route('/EDA')
def EDA():
    return "<h2>EDA</h2><p>More data to come here.</p>"

@app.route('/ChatGPT')
def ChatGPT():
    return "<h2>ChatGPT</h2><p>More data to come here.</p>"

@app.route('/model_prediction')
def model_prediction():
    return "<h2>Model Prediction</h2><p>More data to come here.</p>"

@app.route('/model_results')
def model_results():
    return "<h2>Model Results</h2><p>More data to come here.</p>"

if __name__ == '__main__':
    app.run(debug=True)
