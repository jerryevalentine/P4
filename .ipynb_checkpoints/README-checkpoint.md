# Data
- https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs
- The data is on song, not by customer.

# Questions
- How well can we predict the popularity of a song (for instance, r-squared)?
- What are the most important factors in predicting the popularity of a song?
- Can we build a recommendation based on user preferences (danceability, liveness, etc.)?
- Predicting popularity of a song, versus recommending songs to a customer.  We will focus on the first, and the second is option.

# Song (focus)
- danceability
- liveness
- popularity (0/1)
- r-squared .95
- Predict popularity of new song
    -- new song ---> (model)--> 0/1
    
customer - find 10 songs - (optional)
    danceability  
    liveness
    song -->(model)--> Recommend

# Application Architecture
### HTML pages
    - pages
        - index.html
        - EDA.html
        - model_resuls.html
        - model_prediction.html
        - ChatGPT.html
### Flask App
    - routes
        /index
        /EDA
            - Heatmap
            - Scatterplot subplots
            - Bar Chart subplots
        /model_resuls
            - R-squared
            - Confusion Matrix
            - etc.
        /model_prediction
            - User enters in values for columns, such as danceability and liveness, will it be popular?
            - 
        /ChatGPT
            - Send sample data (5 rows), definition of tables and columns, model results.
            - Return model intepretation in HTML.
### Database
- tables
--spotify

# Dividing work (forthcoming)

# Timeline (forthcoming)

