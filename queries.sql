-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT
    strftime('%Y-%m', date) AS Month,
    AVG(nav) AS Average_NAV
FROM fact_nav
GROUP BY Month;

-- 3. SIP transaction count
SELECT COUNT(*) AS SIP_Count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 4. Transactions by State
SELECT state, COUNT(*) AS Total_Transactions
FROM fact_transactions
GROUP BY state
ORDER BY Total_Transactions DESC;

-- 5. Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average 1-Year Return
SELECT AVG(return_1yr_pct) AS Avg_Return_1Y
FROM fact_performance;

-- 7. Average 3-Year Return
SELECT AVG(return_3yr_pct) AS Avg_Return_3Y
FROM fact_performance;

-- 8. Average 5-Year Return
SELECT AVG(return_5yr_pct) AS Avg_Return_5Y
FROM fact_performance;

-- 9. Fund Count by Category
SELECT category, COUNT(*) AS Total_Funds
FROM dim_fund
GROUP BY category;

-- 10. Verified KYC Investors
SELECT COUNT(*) AS Verified_Investors
FROM fact_transactions
WHERE kyc_status='Verified';