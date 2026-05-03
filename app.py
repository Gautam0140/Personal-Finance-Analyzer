import streamlit as st
from src.preprocessing import load_data, add_features
from src.classifier import apply_categories
from src.anomaly import detect_anomalies
from src.forecast import forecast_balance
from src.insights import generate_insights
from src.health_score import calculate_health_score

st.title("AI Personal Finance Behavior Analyzer")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = load_data(file)
    df = add_features(df)
    df = apply_categories(df)

    st.write(df)
    st.bar_chart(df.groupby('category')['amount'].sum())
    st.write(detect_anomalies(df))
    forecast = forecast_balance(df)
    st.line_chart(forecast.set_index('ds')['yhat'])

    for i in generate_insights(df):
        st.write("- " + i)

    score = calculate_health_score(df)
    st.metric("Financial Health Score", f"{score}/100")
