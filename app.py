import sys
import os
sys.path.append(os.getcwd())
import streamlit as st
import pandas as pd

from preprocessing import load_data, add_features
from classifier import apply_categories
from anomaly import detect_anomalies
from forecast import forecast_balance
from insights import generate_insights
from health_score import calculate_health_score

# ------------------ CONFIG ------------------
st.set_page_config(page_title="AI Finance Analyzer", layout="wide")

# ------------------ HEADER ------------------
st.title("💰 AI Personal Finance Analyzer")
st.caption("Analyze • Predict • Improve your financial behavior")

# ------------------ SIDEBAR ------------------
st.sidebar.header("📂 Upload Data")
file = st.sidebar.file_uploader("Upload your transaction CSV", type=["csv"])

st.sidebar.markdown("---")
st.sidebar.info("Tip: Upload bank transaction CSV")

# ------------------ MAIN ------------------
if file:
    df = load_data(file)
    df = add_features(df)
    df = apply_categories(df)

    # ------------------ METRICS ------------------
    income = df[df['amount'] > 0]['amount'].sum()
    expense = abs(df[df['amount'] < 0]['amount'].sum())
    savings = income - expense
    score = calculate_health_score(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Income", f"₹{income}")
    col2.metric("💸 Expense", f"₹{expense}")
    col3.metric("💵 Savings", f"₹{savings}")
    col4.metric("🧠 Health Score", f"{score}/100")

    st.markdown("---")

    # ------------------ CHARTS ------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Spending by Category")
        st.bar_chart(df.groupby('category')['amount'].sum())

    with col2:
        st.subheader("📈 Monthly Trend")
        monthly = df.groupby('month')['amount'].sum()
        st.line_chart(monthly)

    st.markdown("---")

    # ------------------ FORECAST ------------------
    st.subheader("🔮 Future Balance Prediction")
    forecast = forecast_balance(df)
    st.line_chart(forecast.set_index('ds')['yhat'])

    st.markdown("---")

    # ------------------ ANOMALIES ------------------
    st.subheader("⚠️ Unusual Spending")
    anomalies = detect_anomalies(df)
    st.write(anomalies)

    st.markdown("---")

    # ------------------ INSIGHTS ------------------
    st.subheader("💡 AI Insights")
    insights = generate_insights(df)

    for i in insights:
        st.info(i)

    # ------------------ ADVICE ------------------
    st.subheader("🤖 AI Advice")

    if expense > income:
        st.error("You are overspending. Reduce unnecessary expenses.")
    elif savings > income * 0.3:
        st.success("Excellent savings habit!")
    else:
        st.warning("Try to increase your savings rate.")

else:
    st.warning("👈 Upload a CSV file from sidebar to begin")
