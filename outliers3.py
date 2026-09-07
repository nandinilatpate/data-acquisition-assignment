import pandas as pd
from scipy.stats import zscore

# Create DataFrame with outliers
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

# Calculate Z-scores
df["Z-Score"] = zscore(df["Marks"])

# Identify outliers
outliers = df[abs(df["Z-Score"]) > 3]

print("Identified Outliers:")
print(outliers)

# Remove the outliers
df_clean = df[abs(df["Z-Score"]) <= 3]

# Remove Z-Score column
df_clean = df_clean.drop(columns=["Z-Score"])

# Display cleaned DataFrame
print("\nCleaned DataFrame:")
print(df_clean)