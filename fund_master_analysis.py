import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("="*50)
print("Unique Fund Houses")
print("="*50)
print(fund_master["fund_house"].unique())

print("\n" + "="*50)
print("Categories")
print("="*50)
print(fund_master["category"].unique())

print("\n" + "="*50)
print("Sub Categories")
print("="*50)
print(fund_master["sub_category"].unique())

print("\n" + "="*50)
print("Risk Categories")
print("="*50)
print(fund_master["risk_category"].unique())