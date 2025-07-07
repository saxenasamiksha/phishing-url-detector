import pandas as pd

# Load Parquet file
df = pd.read_parquet("phishing_dataset/Training.parquet")

# Show the first few rows
print(df.head())

# Save as CSV
df.to_csv("urls.csv", index=False)
print("✅ Saved as urls.csv")
