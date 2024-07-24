# Project Intro
- An interactive Web application for users to get song recommendations and to predict a future song’s popularity
- Purpose:
  1. Artists can use this site to predict whether their songs will be a hit when deciding which single to release
  2. Consumers can discover new songs that match their preferences
- Data source: https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs

# Data Preprocessing & Database Creation
- Dependencies: Pandas, datetime, sklearn.model_selection, sklearn.preprocessing
- First, we removed irrelevant columns like “track_id", "track_name", "track_artist", "track_album_id", "track_album_name", "playlist_name", and "playlist_id". Next, we used datetime() and get_dummies() to convert data to numerical format. We identified “hit” songs as those with a score above 90. Finally, we generated the training and testing data, established a database using SQLite, and created a Flask app.

# Machine Learning – Models
### Recommendation Model
1.	Set features as X, and set ‘track_popularity’ as the target y. The features we defined are: danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness'.
2.	Define the Neural Network Model: 
We defined the architecture of the neural network model using the Sequential class. The model consists of:
Input layer (Dense with 64 neurons and 'relu' activation function).
Hidden layer (Dense with 32 neurons and 'relu' activation function).
Output layer (Dense with 1 neuron and 'linear' activation function for regression tasks).
3.	Compile the Model: 
We compiled the model using the compile method. Compilation involves specifying the optimizer, loss function, and metrics to evaluate during training:
Optimizer: Adam optimizer with a learning rate of 0.001.
Loss function: Mean Squared Error (MSE) is used as the loss function for regression tasks.
Metrics: Mean Absolute Error (MAE) is used as a metric to monitor model performance.
4.	Created a user input feature preference to get the top 10 recommended songs.
#    ![Screenshot 2024-07-23 at 9 09 02 PM](https://github.com/user-attachments/assets/96545824-1eb6-4ac8-9509-ed819fa9d966)

### Popularity Model
1.	Set “hit” as our target y, and set the rest of columns as X. 
2.	Define the Neural Network Model: 
2 hidden layers with 80 and 30 neurons respectively and an output layer with one neuron for binary classification. The ReLU activation function is used in the hidden layers, and the sigmoid activation function is used in the output layer.
3.	Compiled the neural network model and trained the model with 100 epochs.
4.	Print the evaluated loss and accuracy results.
- Classification Report showing the results of this model
  # ![Screenshot 2024-07-23 at 9 05 29 PM](https://github.com/user-attachments/assets/f3e8ec13-b448-4a5c-a0c1-5e0a38e54078)

# Application Architecture
![P4 Application Architecture drawio](https://github.com/user-attachments/assets/ad2df0de-1878-49e3-ae93-50bcc4e4038a)

# Interactive Web Application
![css added to prd](https://github.com/user-attachments/assets/4445392d-7766-467f-807c-97c3a8dbe023)


# Conclusion 
- The Popularity Model can accurately predict the hit songs. The most important feature for the model is tempo.
- The recommendation model is most accurate when inputting numerical values, but becomes less accurate when simplifying the input into high/med/low

# Next Step
- Challenges and Limitations: Linking python model to flask app
- Model accuracy:
  1. Maintain and eventually improve recommendation model after high/med/low classification
  2. Understand predictive model accuracy
- UX of website:
  1. Simplify ease of use
  2. Rate given songs instead of inputting song attributes in recommendation model
- Update the database with new songs




