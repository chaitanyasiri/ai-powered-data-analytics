# AI-Powered Data Analytics
# Python Data Analysis
# Dataset: 10,000 cleaned transaction records

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("AI Capstone.xlsx")

# Basic dataset inspection
print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Rows:", df.duplicated().sum())
# Revenue and Profit Analysis

total_revenue = df["Revenue_INR"].sum()
total_profit = df["Profit_INR"].sum()
total_quantity = df["Quantity"].sum()
total_transactions = df["Transaction_ID"].nunique()
average_transaction_value = df["Revenue_INR"].mean()

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue != 0 else 0
)

print("\n--- Business KPIs ---")
print("Total Revenue:", round(total_revenue, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity:", total_quantity)
print("Total Transactions:", total_transactions)
print("Average Transaction Value:", round(average_transaction_value, 2))
print("Profit Margin (%):", round(profit_margin, 2))


# Revenue by Region

region_analysis = (
    df.groupby("Region")
      .agg(
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Revenue by Region ---")
print(region_analysis)


# Revenue by Product Category

category_analysis = (
    df.groupby("Product_Category")
      .agg(
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Product Category Analysis ---")
print(category_analysis)
# Customer and Sales Channel Analysis

customer_segment_analysis = (
    df.groupby("Customer_Segment")
      .agg(
          Customers=("Customer_ID", "nunique"),
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Customer Segment Analysis ---")
print(customer_segment_analysis)


# Sales Channel Analysis

channel_analysis = (
    df.groupby("Sales_Channel")
      .agg(
          Transactions=("Transaction_ID", "nunique"),
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Sales Channel Analysis ---")
print(channel_analysis)


# Monthly Revenue and Profit

df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])

monthly_analysis = (
    df.groupby(df["Transaction_Date"].dt.to_period("M"))
      .agg(
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum"),
          Quantity=("Quantity", "sum")
      )
)

monthly_analysis.index = monthly_analysis.index.astype(str)

print("\n--- Monthly Analysis ---")
print(monthly_analysis)


# Top 10 Products

top_products = (
    df.groupby("Product_Name")
      .agg(
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print("\n--- Top 10 Products ---")
print(top_products)
# AI and Customer Risk Analysis

ai_analysis = (
    df.groupby("AI_Recommemdation")
      .agg(
          Transactions=("Transaction_ID", "nunique"),
          Revenue=("Revenue_INR", "sum"),
          Profit=("Profit_INR", "sum"),
          Average_Confidence=("AI_Confidence_Percent", "mean")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- AI Recommendation Analysis ---")
print(ai_analysis)


# AI Confidence Summary

ai_confidence = {
    "Average": df["AI_Confidence_Percent"].mean(),
    "Minimum": df["AI_Confidence_Percent"].min(),
    "Maximum": df["AI_Confidence_Percent"].max()
}

print("\n--- AI Confidence ---")
print("Average:", round(ai_confidence["Average"], 2))
print("Minimum:", round(ai_confidence["Minimum"], 2))
print("Maximum:", round(ai_confidence["Maximum"], 2))


# Churn Risk Analysis

df["Churn_Risk_Level"] = np.select(
    [
        df["Churn_Risk_Percent"] >= 70,
        df["Churn_Risk_Percent"] >= 40
    ],
    [
        "High Risk",
        "Medium Risk"
    ],
    default="Low Risk"
)

churn_analysis = (
    df.groupby("Churn_Risk_Level")
      .agg(
          Customers=("Customer_ID", "nunique"),
          Average_Churn_Risk=("Churn_Risk_Percent", "mean"),
          Revenue=("Revenue_INR", "sum")
      )
      .sort_values("Average_Churn_Risk", ascending=False)
)

print("\n--- Churn Risk Analysis ---")
print(churn_analysis)


# Demand Trend Analysis

demand_analysis = (
    df.groupby("Demand_Trend")
      .agg(
          Transactions=("Transaction_ID", "nunique"),
          Quantity=("Quantity", "sum"),
          Revenue=("Revenue_INR", "sum")
      )
      .sort_values("Revenue", ascending=False)
)

print("\n--- Demand Trend Analysis ---")
print(demand_analysis)


# Visualization 1: Monthly Revenue

monthly_analysis["Revenue"].plot(
    kind="line",
    figsize=(10, 5),
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Visualization 2: Revenue by Region

region_analysis["Revenue"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Visualization 3: Revenue by Product Category

category_analysis["Revenue"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Visualization 4: Customer Segment Revenue

customer_segment_analysis["Revenue"].plot(
    kind="bar",
    figsize=(10, 5)
)

plt.title("Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Visualization 5: Churn Risk Distribution

churn_analysis["Customers"].plot(
    kind="bar",
    figsize=(8, 5)
)

plt.title("Customers by Churn Risk Level")
plt.xlabel("Churn Risk Level")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\n--- Analysis Completed Successfully ---")
