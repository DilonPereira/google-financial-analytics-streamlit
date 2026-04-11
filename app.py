import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Google Stock Dashboard", layout="wide")

# --- LOAD DATA ---
@st.cache_data # This keeps the app fast by "saving" the data in memory
def load_data():
    df = pd.read_csv('GOOGL.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())

# Filter the dataframe based on user input
filtered_df = df[(df['Date'] >= pd.Timestamp(start_date)) &
                 (df['Date'] <= pd.Timestamp(end_date))].copy()

# --- MAIN CONTENT ---
st.title("📈 Google (GOOGL) Financial Performance")
st.markdown("Interactive analysis of historical stock performance from 2004 to 2022.")

# 1. Key Metrics Row
col1, col2, col3, col4 = st.columns(4)

current_price = filtered_df['Close'].iloc[-1]
open_price = filtered_df['Open'].iloc[0]
change = ((current_price - open_price) / open_price) * 100

col1.metric("Closing Price", f"${current_price:,.2f}")
col2.metric("Period High", f"${filtered_df['High'].max():,.2f}")
col3.metric("Period Low", f"${filtered_df['Low'].min():,.2f}")
col4.metric("Total Return", f"{change:.2f}%", delta_color="normal")

# 2. Main Chart (Candlestick)
st.subheader("Price Movement & Moving Averages")
show_ma = st.checkbox("Show Moving Averages (50 & 200 day)", value=True)

fig = go.Figure()

# Add Candlestick
fig.add_trace(go.Candlestick(
    x=filtered_df['Date'],
    open=filtered_df['Open'],
    high=filtered_df['High'],
    low=filtered_df['Low'],
    close=filtered_df['Close'],
    name="Market Data"
))

if show_ma:
    fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['MA50'],
                             line=dict(color='orange', width=1), name='50 Day MA'))
    fig.add_trace(go.Scatter(x=filtered_df['Date'], y=filtered_df['MA200'],
                             line=dict(color='blue', width=1), name='200 Day MA'))

fig.update_layout(
    template="plotly_dark",
    xaxis_rangeslider_visible=False,
    height=600,
    margin=dict(l=10, r=10, t=30, b=10)
)
st.plotly_chart(fig, use_container_width=True)

# 3. Volume & Raw Data
st.subheader("Trading Volume & Raw Data")
tab1, tab2 = st.tabs(["Volume Analysis", "Data Table"])

with tab1:
    st.bar_chart(filtered_df.set_index('Date')['Volume'])

with tab2:
    st.dataframe(filtered_df.sort_values(by='Date', ascending=False), use_container_width=True)

# Footer
st.caption("Data Source: GOOGL.csv | Project for Data Analysis Portfolio")