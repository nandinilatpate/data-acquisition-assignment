import pandas as pd

# Create a DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, None, 23, 22],
    "Marks": [85, None, 78, 90, None]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)


# 1. Drop rows with missing values
df_drop = df.dropna()

print("\nAfter dropping rows with missing values:")
print(df_drop)


# 2. Fill missing values with a specific value
df_fill = df.copy()

df_fill["Age"] = df_fill["Age"].fillna(0)
df_fill["Marks"] = df_fill["Marks"].fillna(0)

print("\nAfter filling missing values with 0:")
print(df_fill)


# 3. Fill missing values with the mean of the column
df_mean = df.copy()

df_mean["Age"] = df_mean["Age"].fillna(df_mean["Age"].mean())
df_mean["Marks"] = df_mean["Marks"].fillna(df_mean["Marks"].mean())

print("\nAfter filling missing values with mean:")
print(df_mean)