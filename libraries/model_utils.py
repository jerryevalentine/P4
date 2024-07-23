import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
import sqlite3
import pandas as pd

def build_model(input_dim):
    model = Sequential()
    model.add(Input(shape=(input_dim,)))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
    return model

def train_model(model, X_train, y_train, X_test, y_test, epochs=50, batch_size=32):
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=batch_size)
    return history

def save_results_to_db(table_name, loss, mae, val_loss, val_mae, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS neural_network_results (
            table_name TEXT,
            loss REAL,
            mae REAL,
            val_loss REAL,
            val_mae REAL
        )
    """)
    cursor.execute("INSERT INTO neural_network_results (table_name, loss, mae, val_loss, val_mae) VALUES (?, ?, ?, ?, ?)",
                   (table_name, loss, mae, val_loss, val_mae))
    conn.commit()
    conn.close()

def get_results_from_db(database_path):
    conn = sqlite3.connect(database_path)
    df = pd.read_sql_query("SELECT * FROM neural_network_results", conn)
    conn.close()
    return df
