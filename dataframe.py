import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, None, 23, 22],
    "Marks": [85, None, 78, 90, None]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)