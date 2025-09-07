import requests
import json
import os

# Your new API key
API_KEY = "e309c43afc77ffe2c85d9aca17bf5c2a"

# Example city (change if you want)
CITY = "Delhi,IN"

def get_city_coordinates(city):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Handle errors gracefully
    if isinstance(data, dict) and data.get("cod") == 401:
        raise Exception("❌ Invalid API Key. Please check your OpenWeather account.")

    if not data:
        raise Exception("❌ City not found. Try another city name (e.g., 'Mumbai,IN').")

    return data[0]['lat'], data[0]['lon']

def fetch_air_quality(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    try:
        lat, lon = get_city_coordinates(CITY)
        aq_data = fetch_air_quality(lat, lon)

        os.makedirs("data", exist_ok=True)
        with open("data/air_quality.json", "w") as f:
            json.dump(aq_data, f, indent=4)

        print(f"✅ Air quality data for {CITY} saved to data/air_quality.json")

    except Exception as e:
        print(str(e))
