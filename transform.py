import json
import pandas as pd

# Load raw JSON file
with open("data/air_quality.json", "r") as f:
    raw_data = json.load(f)

# Extract useful info
records = []
for entry in raw_data.get("list", []):
    record = {
        "timestamp": entry["dt"],
        "aqi": entry["main"]["aqi"],  # Air Quality Index (1=Good, 5=Very Poor)
        "co": entry["components"]["co"],       # Carbon Monoxide
        "no2": entry["components"]["no2"],     # Nitrogen Dioxide
        "o3": entry["components"]["o3"],       # Ozone
        "pm2_5": entry["components"]["pm2_5"], # PM2.5
        "pm10": entry["components"]["pm10"],   # PM10
    }
    records.append(record)

# Convert to DataFrame
df = pd.DataFrame(records)

# Convert timestamp → readable datetime
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# Save as clean CSV
df.to_csv("data/clean_air_quality.csv", index=False)

print("✅ Cleaned data saved to data/clean_air_quality.csv")
