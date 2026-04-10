# Google (GOOGL) Financial Analytics & Performance Dashboard

**Interactive Python-based equity analysis and visualization dashboard for Alphabet Inc. (GOOGL)** — exploring historical price action, technical indicators, volatility, and market resilience since its IPO.

---

### **Equity Dynamics and Market Resilience: An Interactive Analysis of GOOGL Historical Performance and Technical Indicators (2004–2022)**

**Author**: Dilon Pereira  
**University**: University of Passau – School of Business, Economics and Information Systems  
**Date**: April 2026

---

## Project Purpose

This repository contains a **full-stack Python analytical workflow** and **interactive web application** designed to transform raw historical stock data (`GOOGL.csv`) into clean, analysis-ready structures.

The dashboard provides a comprehensive, data-driven overview of Alphabet Inc.’s (Google) equity performance through three core analytical lenses:

- **Price Action** → Interactive candlestick charts displaying Open, High, Low, and Close (OHLC) data with full zoom and drill-down capability.  
- **Trend Identification** → Dynamic overlay of 50-day and 200-day Simple Moving Averages (SMA) to detect Golden Cross / Death Cross events and long-term trend shifts.  
- **Performance Metrics** → Automated calculation of Period ROI (%), highest/lowest price points, volume density, and volatility statistics across any user-selected date range.

Built as both a reproducible analysis pipeline and a production-grade Streamlit dashboard, the project enables institutional-grade technical analysis with zero manual Excel work.

---

## Key Features

- **Robust Time-Series Processing** — Automated date parsing, indexing, and cleaning of 4,400+ rows of daily OHLCV data.
- **Dynamic Technical Indicators** — Real-time calculation and visualization of 50-day and 200-day SMAs with automatic detection of crossover events.
- **Interactive Visualization Suite** — High-fidelity Plotly charts (candlestick, line, volume, and ROI overlays) with granular date-range selectors.
- **Optimized Performance** — Uses `st.cache_data` for lightning-fast responsiveness even with large datasets.
- **Automated KPI Reporting** — Instant computation of total return, annualized ROI, maximum drawdown, and volume-weighted volatility for any selected period.
- **Fully Reproducible** — One-click pipeline from raw CSV → cleaned DataFrame → live dashboard.

---

## Analytical Context

The dashboard is specifically designed to isolate and visualize the impact of major market cycles on Google’s stock performance, focusing on:

- **Historical Volatility** — Identification of major price drawdowns and recovery periods during the 2008 Financial Crisis, 2020 COVID-19 market shock, and other regime shifts.
- **Momentum Analysis** — Evaluation of the predictive power of 50/200-day SMA crossovers in signaling sustained bullish or bearish trends.
- **Liquidity Examination** — Mapping trading volume against price movements to detect anomalies in market interest and institutional activity.

By combining interactive visuals with automated metrics, the project offers clear insights into Alphabet’s market resilience and long-term equity dynamics.

---

## Tech Stack

- **Python**  
- **Pandas** (data cleaning & transformation)  
- **Plotly** (interactive visualizations)  
- **Streamlit** (web dashboard framework)  
- **Time-Series Analysis** (rolling windows, SMAs, ROI calculations)
