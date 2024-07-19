from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from libraries.db_utils import query_table, get_metadata_tables, query_column
from libraries.chatgpt_utils import get_chatgpt_analysis

# load scaler
# load model
# load original_df

database_path = r'C:\Users\jerry\Programming\P4\resources\spotify.db'
OPENAI_API_KEY = 'sk-proj-2F0wcgrKsNYmYqANo00aT3BlbkFJVuZiG980OzTXp2v9ykiZ'  # Hard-coded API key

if not OPENAI_API_KEY:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/helloworld')
def display_helloworld():
    message = helloworld()  # Call the function to get the message
    return render_template('helloworld.html', message=message)  # Pass the message to the template

@app.route('/display_data', methods=['GET', 'POST'])
def display_data():
    tables = get_metadata_tables(database_path)
    selected_table = None
    table_data = None
    if request.method == 'POST':
        selected_table = request.form.get('table')
        if selected_table:
            table_data = query_table(selected_table, database_path, num_of_rows=10)

    return render_template('display_data.html', tables=tables, selected_table=selected_table, table_data=table_data)

@app.route('/EDA')
def EDA():
    return render_template('EDA.html')

@app.route('/model_results')
def model_results():
    return render_template('model_results.html')

@app.route('/model_recommendation', methods=['GET', 'POST'])
def model_recommendation(): 
    if request.method=='POST': 
        # model predict
        preferences=request.form
        recommendations=recommend_songs(X, X, preferences, X, X) # TODO
        
        return render_template('model_recommendation.html', recommendations=list(recommendations))
    else: 
        return render_template('model_recommendation.html')

def recommend_songs(model, scaler, preferences, original_df, features):
    # Convert preferences to DataFrame
    user_df = pd.DataFrame([preferences])
    
    # Scale the user preferences
    user_scaled = scaler.transform(user_df)
    
    # Predict the popularity for the user's preferences
    predicted_popularity = model.predict(user_scaled)
    
    # Add the predicted popularity to the user_df
    user_df['predicted_popularity'] = predicted_popularity
    
    # Combine with the original dataset to find similar songs
    similar_songs = original_df.copy()
    for feature in preferences.keys():
        similar_songs[feature] = similar_songs[feature] - preferences[feature]
    similar_songs['distance'] = np.sqrt(np.sum(np.square(similar_songs[features]), axis=1))
    
    # Drop duplicates based on track_name and track_artist
    similar_songs = similar_songs.drop_duplicates(subset=['track_name', 'track_artist'])
    
    # Get the top 10 similar songs
    top_10_songs = similar_songs.sort_values(by='distance').head(10)
    return top_10_songs[['track_name', 'track_artist', 'distance']]

@app.route('/model_prediction')
def model_prediction():
    return render_template('model_prediction.html')

@app.route('/chatgpt_analysis', methods=['GET', 'POST'])
def chatgpt_analysis():
    table_name = 'model_results'
    column_name = 'model_name'

    if request.method == 'POST':
        model_name = request.form['model_name']
        user_input = request.form['user_input']
        # Combine user input with model data for ChatGPT analysis
        chatgpt_results = get_chatgpt_analysis(OPENAI_API_KEY, model_name, user_input, database_path)
        return render_template('chatgpt_analysis.html', model_names=query_column(table_name, column_name, database_path), chatgpt_results=chatgpt_results)
    
    model_names = query_column(table_name, column_name, database_path)
    return render_template('chatgpt_analysis.html', model_names=model_names)


if __name__ == '__main__':
    app.run(debug=True)
