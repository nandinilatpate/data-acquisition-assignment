import pandas as pd
from scipy.stats import zscore

# Step 1: Create DataFrame with outliers
data = {
    "Name": [
        "Student1", "Student2", "Student3", "Student4", "Student5",
        "Student6", "Student7", "Student8", "Student9", "Student10",
        "Student11", "Student12", "Student13", "Student14", "Student15",
        "Student16", "Student17", "Student18", "Student19", "Student20",
        "Student21"
    ],
    "Marks": [
        50, 51, 52, 53, 54,
        55, 56, 57, 58, 59,
        60, 61, 62, 63, 64,
        65, 66, 67, 68, 69,
        200
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# Step 2: Calculate Z-scores
df["Z-Score"] = zscore(df["Marks"])

print("\nDataFrame with Z-Scores:")
print(df)


# Identify outliers
outliers = df[abs(df["Z-Score"]) > 3]

print("\nIdentified Outliers:")
print(outliers)