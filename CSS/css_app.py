from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This is just a test route for the layout
@app.route('/test')
def display_data():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
