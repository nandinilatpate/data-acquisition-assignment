import requests
import pandas as pd

# Public API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 10,
    "page": 1
}

# Fetch data from API
response = requests.get(url, params=params)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Data fetched successfully")

    # Convert API response to JSON
    data = response.json()

    # Store data in DataFrame
    df = pd.DataFrame(data)

    # Display first few rows
    print("\nFirst few rows of the DataFrame:")
    print(df.head())
else:
    print("Failed to fetch data")