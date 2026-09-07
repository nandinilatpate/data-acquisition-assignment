import pandas as pd

# Load JSON file
df = pd.read_json("users.json")

# Display first 5 rows
print(df.head())