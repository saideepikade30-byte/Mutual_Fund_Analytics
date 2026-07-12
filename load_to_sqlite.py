import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned datasets
nav = pd.read_csv("data/processed/02_nav_history.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions.csv")
performance = pd.read_csv("data/processed/07_scheme_performance.csv")
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

# Save to SQLite
fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("✅ SQLite database created successfully!")

# Verify row counts
tables = {
    "dim_fund": fund_master,
    "fact_nav": nav,
    "fact_transactions": transactions,
    "fact_performance": performance,
}

print("\nRow Count Verification")
for table_name, dataframe in tables.items():
    count = pd.read_sql(f"SELECT COUNT(*) AS total FROM {table_name}", engine)
    print(f"{table_name}: Source = {len(dataframe)}, SQLite = {count['total'][0]}")