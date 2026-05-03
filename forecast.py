from prophet import Prophet

def forecast_balance(df):
    df2 = df[['date','amount']].copy()
    df2 = df2.groupby('date').sum().cumsum().reset_index()
    df2.columns = ['ds','y']
    model = Prophet()
    model.fit(df2)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast[['ds','yhat']]
