import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def pp_load_clean(df, target_column):
    try:
        df = df.dropna()
        return df
    except Exception as e:
        print(f"An error occurred while loading and cleaning data: {e}")
        raise

def scale_data(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

def train_test_split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def create_dummies(df, columns):
    return pd.get_dummies(df, columns=columns)

def identify_column_types(df):
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    categorical_columns = df.select_dtypes(exclude='number').columns.tolist()
    return numeric_columns, categorical_columns
