import pandas as pd
import os

# Folder containing CSV files
data_folder = "data/raw"

# Check if folder exists
if not os.path.exists(data_folder):
    print("Error: data/raw folder not found!")
    exit()

# Get all CSV files
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

print(f"Total CSV files found: {len(csv_files)}")

for file in csv_files:
    print("\n" + "=" * 60)
    print(f"Dataset: {file}")

    file_path = os.path.join(data_folder, file)

    df = pd.read_csv(file_path)

    print("Shape:", df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())