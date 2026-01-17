import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(layout="wide")

st.title("Bitcoin Sentiment vs Hyperliquid Trader Intelligence")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load datasets
fear = pd.read_csv("dataset/fear_greed_index.csv")
hist = pd.read_csv("dataset/historical_data.csv")

fear['date'] = pd.to_datetime(fear['date'])
hist['Timestamp'] = pd.to_datetime(hist['Timestamp'], unit='ms')
hist['date'] = hist['Timestamp'].dt.date
hist['date'] = pd.to_datetime(hist['date'])

trade = hist.merge(fear[['date','classification','value']], on="date", how="left")

# Sidebar filters
st.sidebar.header("Filters")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    trade['classification'].dropna().unique(),
    default=trade['classification'].dropna().unique()
)

coin_filter = st.sidebar.multiselect(
    "Select Coin",
    trade['Coin'].unique(),
    default=trade['Coin'].unique()
)

filtered = trade[
    (trade['classification'].isin(sentiment_filter)) &
    (trade['Coin'].isin(coin_filter))
]

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("PnL by Sentiment")
    st.bar_chart(filtered.groupby("classification")['Closed PnL'].mean())

with col2:
    st.subheader("Buy vs Sell")
    pivot = filtered.groupby(['classification','Side'])['Closed PnL'].mean().unstack()
    st.bar_chart(pivot)

# Wallet Explorer
st.subheader("Top Wallets in Filtered Regime")
top_wallet = filtered.groupby("Account")['Closed PnL'].sum().sort_values(ascending=False).head(10)
st.dataframe(top_wallet)

# ML Predictor
st.subheader("🔮 Predict Trade Profitability")

sent_val = st.slider("Sentiment Value", 0, 100, 50)
size = st.number_input("Trade Size USD", 1.0)
side = st.selectbox("Side", ["BUY","SELL"])
coin = st.selectbox("Coin", trade['Coin'].unique())

side_enc = 1 if side=="SELL" else 0
coin_enc = list(trade['Coin'].unique()).index(coin)

X = np.array([[sent_val, size, side_enc, coin_enc]])
pred = model.predict_proba(X)[0][1]

st.success(f"Probability Trade Will Be Profitable: {round(pred*100,2)}%")