from flask import Flask, request, render_template
import pandas as pd
import tensorflow as tf
from libraries.recommendation_utils import get_user_preferences, recommend_songs

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('resources/songs_df_pp_encoded.h5')

# Load the original dataset
songs_df_pp_encoded = pd.read_csv('resources/songs_df_pp_encoded.csv')
features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness']

# Ensure necessary columns are present
if 'song' not in songs_df_pp_encoded.columns or 'artist' not in songs_df_pp_encoded.columns:
    raise KeyError("The dataset must contain 'song' and 'artist' columns.")

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        preferences = get_user_preferences(request.form)
        top_10_songs = recommend_songs(model, preferences, songs_df_pp_encoded, features)
        return render_template('recommendation.html', songs=top_10_songs.to_dict(orient='records'))
    return render_template('recommendation.html')

if __name__ == '__main__':
    app.run(debug=True)
