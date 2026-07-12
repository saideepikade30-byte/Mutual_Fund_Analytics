# Data Dictionary

## dim_fund
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| scheme_name | TEXT | Mutual Fund Scheme Name |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Equity/Debt |
| sub_category | TEXT | Scheme Category |
| risk_grade | TEXT | Risk Level |

## fact_nav
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

## fact_transactions
| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction Amount |
| state | TEXT | Investor State |
| kyc_status | TEXT | Verified/Pending |

## fact_performance
| Column | Data Type | Description |
|---------|-----------|-------------|
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| return_5yr_pct | REAL | 5 Year Return |
| expense_ratio_pct | REAL | Expense Ratio |
| aum_crore | REAL | Assets Under Management |