import pandas as pd
import numpy as np

amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

print(f"Descriptive Statistics")

# To check the columns names and which ones are numeric
print("\nData preview: ")
print(amazon_data.head(4))

numeric_columns = [
    'price', 
    'discount_percent', 
    'quantity_sold', 
    'rating', 
    'review_count', 
    'discounted_price', 
    'total_revenue'
]

print("\nStatistical summary: ")
print(f"\n{amazon_data[numeric_columns].describe()}")

print(f"\nRange:\n{amazon_data[numeric_columns].max() - amazon_data[numeric_columns].min()}")

print(f"\nMedian and mean: \n{amazon_data[numeric_columns].median()}")

print(f"\n{amazon_data[numeric_columns].mean()}")

print(f"\n{35*'*'}")
print(f"\nVariance:\n{amazon_data[numeric_columns].var()}")

print(f"\nStandard deviation:\n{amazon_data[numeric_columns].std()}")


print(f"\n{10*'*'} Grouped Data {10*'*'}")

# Stats in group data that can have a relation

# Checking if the category can have a relation with how much money people
# spend depending in the category
category_data = amazon_data.groupby("product_category").agg(
    avg_price=("price", "mean"),
    avg_rating=("rating", "mean"),
    total_revenue=("total_revenue", "sum"),
    total_orders=("order_id", "count")
).sort_values('total_revenue', ascending=False)

print(f"\nCategory group: \n{category_data}")

# Getting the products more requested products
top_products = amazon_data.groupby("product_id").agg(
    total_orders=("order_id", "count"),
    avg_price=("price", "mean"),
    avg_rating=("rating", "mean"),
    total_revenue=("total_revenue", "sum")
).sort_values('total_orders', ascending=False)

print(f"\nTop products and statistical info): \n {top_products.head()}")

# For checking if the rating matters in the quantity or the total revenu
rating_data = amazon_data.groupby("rating").agg(
    avg_price=("price", "mean"),
    avg_quantity=("quantity_sold", "mean"),
    total_revenue=("total_revenue", "sum")
).sort_values('total_revenue', ascending=False)


print(f"\nRating of the best selling products: \n{rating_data}")


print(f"\n{10*'*'} Correlation {10*'*'}")

# Checking if rating affects revenue
print(f"\nRating and total revenue {amazon_data["rating"].corr(amazon_data["total_revenue"]).round(4)}")

# Checking if quantity sold affects rating
print(f"\nQuantity and rating {amazon_data["quantity_sold"].corr(amazon_data["rating"]).round(4)}")