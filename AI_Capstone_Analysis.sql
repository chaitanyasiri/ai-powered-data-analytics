-- AI-Powered Data Analytics
-- MySQL Analysis Queries
-- Dataset: 10,000 cleaned transaction records
-- Table: ai_capstone

USE ai_capstone;

-- 1. Total Revenue
SELECT SUM(Revenue_INR) AS Total_Revenue
FROM ai_capstone;

-- 2. Total Profit
SELECT SUM(Profit_INR) AS Total_Profit
FROM ai_capstone;

-- 3. Total Transactions
SELECT COUNT(DISTINCT Transaction_ID) AS Total_Transactions
FROM ai_capstone;

-- 4. Total Quantity Sold
SELECT SUM(Quantity) AS Total_Quantity
FROM ai_capstone;

-- 5. Average Transaction Value
SELECT ROUND(AVG(Revenue_INR), 2) AS Average_Transaction_Value
FROM ai_capstone;

-- 6. Profit Margin
SELECT ROUND(
    SUM(Profit_INR) / NULLIF(SUM(Revenue_INR), 0) * 100, 2
) AS Profit_Margin_Percent
FROM ai_capstone;

-- 7. Revenue by Region
SELECT
    Region,
    ROUND(SUM(Revenue_INR), 2) AS Revenue
FROM ai_capstone
GROUP BY Region
ORDER BY Revenue DESC;

-- 8. Revenue by Product Category
SELECT
    Product_Category,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY Product_Category
ORDER BY Revenue DESC;

-- 9. Top 10 Products by Revenue
SELECT
    Product_Name,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit,
    SUM(Quantity) AS Quantity_Sold
FROM ai_capstone
GROUP BY Product_Name
ORDER BY Revenue DESC
LIMIT 10;

-- 10. Monthly Revenue and Profit
SELECT
    DATE_FORMAT(Transaction_Date, '%Y-%m') AS Month,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY DATE_FORMAT(Transaction_Date, '%Y-%m')
ORDER BY Month;

-- 11. Sales Channel Performance
SELECT
    Sales_Channel,
    COUNT(DISTINCT Transaction_ID) AS Transactions,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY Sales_Channel
ORDER BY Revenue DESC;

-- 12. Customer Segment Performance
SELECT
    Customer_Segment,
    COUNT(DISTINCT Customer_ID) AS Customers,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY Customer_Segment
ORDER BY Revenue DESC;

-- 13. Churn Risk Analysis
SELECT
    CASE
        WHEN Churn_Risk_Percent >= 70 THEN 'High Risk'
        WHEN Churn_Risk_Percent >= 40 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS Churn_Risk_Level,
    COUNT(DISTINCT Customer_ID) AS Customers,
    ROUND(AVG(Churn_Risk_Percent), 2) AS Avg_Churn_Risk
FROM ai_capstone
GROUP BY
    CASE
        WHEN Churn_Risk_Percent >= 70 THEN 'High Risk'
        WHEN Churn_Risk_Percent >= 40 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END
ORDER BY Avg_Churn_Risk DESC;

-- 14. AI Recommendation Analysis
SELECT
    AI_Recommemdation,
    COUNT(*) AS Transactions,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY AI_Recommemdation
ORDER BY Revenue DESC;

-- 15. AI Confidence Analysis
SELECT
    ROUND(AVG(AI_Confidence_Percent), 2) AS Average_AI_Confidence,
    MIN(AI_Confidence_Percent) AS Minimum_AI_Confidence,
    MAX(AI_Confidence_Percent) AS Maximum_AI_Confidence
FROM ai_capstone;

-- 16. Demand Trend Analysis
SELECT
    Demand_Trend,
    COUNT(*) AS Transactions,
    SUM(Quantity) AS Quantity,
    ROUND(SUM(Revenue_INR), 2) AS Revenue
FROM ai_capstone
GROUP BY Demand_Trend
ORDER BY Revenue DESC;

-- 17. Customer Sentiment Analysis
SELECT
    Customer_Sentiment,
    COUNT(DISTINCT Customer_ID) AS Customers,
    ROUND(AVG(Churn_Risk_Percent), 2) AS Avg_Churn_Risk,
    ROUND(SUM(Revenue_INR), 2) AS Revenue
FROM ai_capstone
GROUP BY Customer_Sentiment
ORDER BY Revenue DESC;

-- 18. Campaign Performance
SELECT
    Campaign,
    COUNT(DISTINCT Transaction_ID) AS Transactions,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY Campaign
ORDER BY Revenue DESC;

-- 19. State-wise Revenue
SELECT
    State,
    ROUND(SUM(Revenue_INR), 2) AS Revenue,
    ROUND(SUM(Profit_INR), 2) AS Profit
FROM ai_capstone
GROUP BY State
ORDER BY Revenue DESC
LIMIT 10;

-- 20. Highest-Value Transactions
SELECT
    Transaction_ID,
    Transaction_Date,
    Customer_ID,
    Customer_Name,
    Product_Name,
    Revenue_INR,
    Profit_INR
FROM ai_capstone
ORDER BY Revenue_INR DESC
LIMIT 20;