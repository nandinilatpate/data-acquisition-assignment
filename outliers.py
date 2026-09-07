import pandas as pd

# Create DataFrame with outliers
data = {
    "Name": ["Student1", "Student2", "Student3", "Student4", "Student5",
             "Student6", "Student7", "Student8", "Student9", "Student10"],
    "Marks": [50, 52, 55, 58, 60, 62, 65, 68, 70, 200]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)