import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['date'])
    return df

def add_features(df):
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    return df
