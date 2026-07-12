import pandas as pd
import os

# Create processed folder if it doesn't exist
os.makedirs("data/processed", exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction_type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

mapping = {
    "Sip": "SIP",
    "Lumpsum": "Lumpsum",
    "Redemption": "Redemption"
}

df["transaction_type"] = df["transaction_type"].replace(mapping)

# Validate amount_inr > 0
df = df[df["amount_inr"] > 0]

# Validate KYC status
valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print("Invalid KYC Records:", len(invalid_kyc))

# Save cleaned dataset
output_path = "data/processed/08_investor_transactions.csv"

df.to_csv(output_path, index=False)

print("Cleaned Shape:", df.shape)
print("Saved:", output_path)