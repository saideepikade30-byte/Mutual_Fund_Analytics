import requests
import pandas as pd
import os

# Scheme codes
scheme_codes = {
    "HDFC_Top100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

os.makedirs("data/raw", exist_ok=True)

for fund_name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    print(f"Fetching {fund_name}...")

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        filename = f"data/raw/{fund_name}.csv"

        nav_df.to_csv(filename, index=False)

        print(f"Saved -> {filename}")

    else:
        print(f"Failed for {fund_name}")