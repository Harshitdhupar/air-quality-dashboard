import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned CSV
df = pd.read_csv("data/clean_air_quality.csv")

# Title
st.title("🌍 Air Quality & Health Impact Dashboard")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# AQI Trend
st.subheader("📈 AQI Trend Over Time")
fig, ax = plt.subplots()
ax.plot(df["timestamp"], df["aqi"], marker="o", linestyle="-")
ax.set_xlabel("Time")
ax.set_ylabel("AQI (1=Good, 5=Very Poor)")
st.pyplot(fig)

# Pollutants Correlation Heatmap
st.subheader("📊 Pollutants Correlation Heatmap")
corr = df[["co", "no2", "o3", "pm2_5", "pm10"]].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Health Risk Warning
st.subheader("🚨 Health Risk Warning")
latest_aqi = df.iloc[-1]["aqi"]

if latest_aqi == 1:
    st.success("✅ Good: Air quality is safe.")
elif latest_aqi == 2:
    st.info("ℹ️ Fair: Acceptable but a bit polluted.")
elif latest_aqi == 3:
    st.warning("⚠️ Moderate: Sensitive groups should reduce outdoor activity.")
elif latest_aqi == 4:
    st.error("❌ Poor: Health risk for everyone.")
else:
    st.error("☠️ Very Poor: Dangerous for health!")

# Bonus: Healthy Day Predictor
st.subheader("🌤️ Healthy Day Predictor")
best_day = df.loc[df["aqi"].idxmin()]
st.write(f"The healthiest day was **{best_day['timestamp']}** with AQI = {best_day['aqi']}.")
