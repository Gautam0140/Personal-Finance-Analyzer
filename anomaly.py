from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    df_exp = df[df['amount'] < 0].copy()
    if len(df_exp) < 5:
        df_exp['anomaly'] = 1
        return df_exp
    model = IsolationForest(contamination=0.2, random_state=42)
    df_exp['anomaly'] = model.fit_predict(df_exp[['amount']])
    return df_exp
