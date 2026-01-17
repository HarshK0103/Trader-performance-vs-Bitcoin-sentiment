# 🚀 Trader Performance vs Bitcoin Sentiment
### Behavioral Crypto Trading Intelligence using Hyperliquid + Fear & Greed Index

---

## 📌 Project Overview
This project investigates how Bitcoin market sentiment influences real trader behavior and profitability on the Hyperliquid decentralized exchange.

By combining:
- Bitcoin Fear & Greed Index  
- Hyperliquid historical trade execution data  

we perform institutional-style behavioral analysis and build an AI model that predicts trade profitability using sentiment and trading features.

---

## 🎯 Objectives
- Align trader Closed PnL with Bitcoin sentiment regimes  
- Detect behavioral trading patterns under Fear & Greed  
- Identify sentiment-specialized profitable wallets  
- Analyze directional (BUY/SELL) bias per regime  
- Train ML model to predict profitable trades  
- Deploy interactive Streamlit dashboard for exploration  

---

## 🧠 Key Insights
✔ Traders are most profitable during Fear regimes  
✔ Performance drops significantly during Greed periods  
✔ Certain wallets specialize in panic-driven volatility  
✔ Coin preference varies across sentiment cycles  
✔ Trade success is predictable using sentiment + behavior  

---

## 🤖 Machine Learning Model
We trained a RandomForestClassifier to predict trade profitability using:
- Sentiment score  
- Trade size (USD)  
- Trade side (BUY/SELL)  
- Coin traded  

---

## 📊 Dashboard Features
- Sentiment vs Trader Profit charts  
- BUY vs SELL profitability per regime  
- Wallet profit leaderboard  
- Coin profitability across sentiment  
- AI-based trade profitability predictor  

Run locally:
python -m streamlit run app/app.py

---

## 🛠 Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit

---

## 🧑‍💻 Author

**Harsh Karekar**  
B.Tech – Electronics & Communication Engineering  
Aspiring Data Scientist / AI/ML Engineer
 
📫 [LinkedIn](https://www.linkedin.com/in/harsh-karekar-01h6910a04/) | 💻 [GitHub](https://github.com/HarshK0103)
