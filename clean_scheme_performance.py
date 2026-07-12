import pandas as pd
import os

# Create processed folder
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

# Convert return columns to numeric
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Find rows with missing return values
anomalies = df[df[return_columns].isnull().any(axis=1)]

print("Anomalies Found:", len(anomalies))

# Convert expense ratio to numeric
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Check valid expense ratio range (0.1% - 2.5%)
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio Records:", len(invalid_expense))

# Save cleaned dataset
output_path = "data/processed/07_scheme_performance.csv"

df.to_csv(output_path, index=False)

print("Cleaned Shape:", df.shape)
print("Saved:", output_path)