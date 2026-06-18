import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=-1.29&longitude=36.82&daily=temperature_2m_max,temperature_2m_min&timezone=Africa/Nairobi"

print("Sending request...")
response = requests.get(url, timeout=10)
print("Got response!")

data = response.json()
df = pd.DataFrame(data["daily"])

def categorize(temp):
    if temp < 22:
        return "cold"
    elif temp < 24:
        return "mild"
    else:
        return "hot"
    
df["category"] = df["temperature_2m_max"].apply(categorize)
print(df)

df.to_csv("nairobi_weather.csv", index=False)