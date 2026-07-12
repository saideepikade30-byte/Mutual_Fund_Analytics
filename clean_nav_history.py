import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Sort by AMFI code and date
df = df.sort_values(by=["amfi_code", "date"])

# Forward fill missing NAV values within each fund
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicate rows
df = df.drop_duplicates()

# Keep only valid NAV values (>0)
df = df[df["nav"] > 0]

# Save cleaned dataset
output_path = "data/processed/02_nav_history.csv"
df.to_csv(output_path, index=False)

print("Cleaned Shape:", df.shape)
print("Cleaned file saved to:", output_path)
print("Missing NAV values:", df["nav"].isnull().sum())