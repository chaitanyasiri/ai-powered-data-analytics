# AI-Powered Data Analytics Platform

## Project Overview

An end-to-end data analytics project that combines business intelligence, SQL, Python, and AI-driven analytics to transform transactional data into actionable business insights.

The project analyzes 10,000 synthetic transaction records covering sales, customers, products, campaigns, demand trends, customer sentiment, churn risk, and AI recommendations.

The objective is to help business teams understand revenue and profitability, identify high-value customers and products, monitor churn risk, evaluate campaigns, and use AI-generated insights to support data-driven decision-making.

## Business Objectives

- Analyze revenue and profitability performance
- Identify high-performing regions and product categories
- Understand customer segment and sales channel performance
- Analyze customer churn risk
- Evaluate AI recommendations and confidence levels
- Identify demand trends and customer sentiment
- Monitor campaign performance
- Create an interactive business intelligence dashboard
## Dataset

The project uses a synthetic dataset containing 10,000 cleaned transaction records.

### Key Fields

- Transaction_ID
- Transaction_Date
- Region
- State
- City
- Customer_ID
- Customer_Name
- Customer_Segment
- Product_Category
- Product_Name
- Sales_Channel
- Campaign
- Quantity
- Unit_Price_INR
- Discount_Percent
- Revenue_INR
- Cost_INR
- Profit_INR
- Inventory_Units
- Forecasted_Next_Month_Units
- Demand_Trend
- Customer_Sentiment
- Churn_Risk_Percent
- AI_Recommemdation
- AI_Confidence_Percent

## Data Preparation

The dataset was prepared before analysis to improve data quality and consistency.

Key data preparation activities included:

- Duplicate record identification and removal
- Missing-value validation
- Data type validation
- Date format standardization
- Text-value consistency checks
- Numerical field validation
- Percentage field validation
- Final dataset validation

The final dataset contains **10,000 cleaned records**.

## Tools & Technologies

- **Microsoft Excel** — Data review and dataset management
- **Power Query / Power BI** — Data transformation and dashboard development
- **MySQL** — SQL-based business analysis
- **Python** — Data analysis and visualization
- **Pandas** — Data manipulation
- **NumPy** — Numerical analysis
- **Matplotlib** — Data visualization
- **GitHub** — Project version control and portfolio
- **AI tools** — AI-assisted analysis and recommendation insights
## Analysis Performed

### SQL Analysis

MySQL was used to perform business-focused analysis, including:

- Total revenue and total profit
- Total transactions and quantity sold
- Average transaction value
- Profit margin
- Revenue by region
- Revenue by product category
- Top-performing products
- Monthly revenue and profit trends
- Sales channel performance
- Customer segment performance
- Customer churn-risk classification
- AI recommendation performance
- AI confidence analysis
- Demand trend analysis
- Customer sentiment analysis
- Campaign performance
- State-wise revenue analysis
- Highest-value transactions

See `AI_Capstone_Analysis.sql` for the complete SQL analysis.

### Python Analysis

Python was used for exploratory data analysis and visualization.

The analysis includes:

- Dataset structure and statistical summary
- Missing-value and duplicate checks
- Business KPI calculations
- Regional performance analysis
- Product category analysis
- Customer segment analysis
- Sales channel analysis
- Monthly revenue trends
- Top product analysis
- AI recommendation analysis
- AI confidence analysis
- Churn-risk analysis
- Demand trend analysis

Visualizations were created using **Matplotlib**.

See `AI_Capstone_Analysis.py` for the Python analysis.

## Power BI Dashboard

The Power BI dashboard provides an executive view of business performance and AI-driven insights.

### Key KPIs

- Total Revenue
- Total Profit
- Profit Margin
- Total Quantity
- Total Orders
- Average Order Value
- Average AI Confidence

### Dashboard Insights

The dashboard enables users to explore:

- Revenue and profitability trends
- Regional performance
- Product and category performance
- Customer segments
- Sales channels
- AI recommendations
- Customer churn risk
- Demand trends
- Campaign performance
## Project Structure

```text
AI-Powered-Data-Analytics/
│
├── AI_Capstone_Analysis.sql
├── AI_Capstone_Analysis.py
├── AI-Powered-Data-Analytics-Platform.pdf
├── Customer Churn Analysis.pdf
├── E-commerce Analytics.pdf
├── HR Analytics Dashboard.pdf
└── Sales & Revenue Analytics Dashboard.pdf
Key Business Questions
This project addresses practical business questions such as:
Which regions generate the highest revenue and profit?
Which products and categories perform best?
Which customer segments contribute the most revenue?
Which sales channels perform best?
What are the monthly revenue and profit trends?
Which customers have higher churn risk?
How confident are the AI-generated recommendations?
Which demand trends are associated with higher sales?
Which campaigns generate the strongest business results?
Which transactions represent the highest-value opportunities?
Business Value
The analysis can support business teams in:
Improving sales and revenue strategies
Identifying profitable products and customer segments
Prioritizing high-risk customers
Evaluating marketing campaigns
Monitoring demand trends
Supporting inventory planning
Evaluating AI-assisted recommendations
Making data-driven business decisions
Portfolio Files
AI_Capstone_Analysis.sql — MySQL business analysis queries
AI_Capstone_Analysis.py — Python data analysis and visualizations
AI-Powered-Data-Analytics-Platform.pdf — Power BI dashboard
Additional dashboard PDFs — Supporting analytics projects
Skills Demonstrated
Data Analysis: Data cleaning, validation, EDA, KPI analysis, business insights
SQL: SELECT, aggregation, GROUP BY, CASE, filtering, sorting, date analysis
Python: Pandas, NumPy, Matplotlib
Business Intelligence: Power BI, dashboard design, KPI development, interactive analysis
AI Analytics: AI recommendations, confidence analysis, churn-risk analysis, demand insights
Data Storytelling: Translating analytical results into actionable business recommendations
Author
Chaitanya Siri
Aspiring Data Analyst | Python | SQL | Excel | Power BI | Tableau | AI Analytics
⭐ This project demonstrates an end-to-end approach to transforming raw business data into analytical insights and decision-support dashboards.