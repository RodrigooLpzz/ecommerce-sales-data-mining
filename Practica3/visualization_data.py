import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

print(f"Data type: \n{amazon_data.dtypes}")

histogram_columns = [
  'price',
  'discounted_price',
  'total_revenue',
  'rating',
  'review_count'
]

bar_columns = [
  'quantity_sold',
  'discount_percent',
  'product_category',
  'payment_method',
  'customer_region'
]

# Checking the spread of numeric values like rating, price, revenue
for column in histogram_columns:
  plt.figure()
  plt.hist(amazon_data[column], bins=15)
  plt.title(f"{column.replace('_', ' ').title()} Distribution")
  plt.xlabel(column)
  plt.ylabel("Number of values")
  plt.show()

# Creating bar charts to see how many time each category appears
# columns that we didn't analyze in the last homework like customer region, payment method
for column in bar_columns:
  plt.figure()
  amazon_data[column].value_counts().sort_index().plot(kind='bar')
  plt.title(f"{column.replace('_', ' ').title()} Bar Chart")
  plt.xlabel(column)
  plt.ylabel("Total")
  plt.show()

box_plots_columns = histogram_columns

# Helps to see the median value
for column in box_plots_columns:
  plt.figure()
  plt.boxplot(amazon_data[column])
  plt.title(column.replace("_", " ").title() + " Boxplot")
  plt.ylabel(column)
  plt.show()

# Checking if rating has some relation with revenue
# In the last homework the correlation was very very low
plt.figure()
plt.scatter(amazon_data["rating"], amazon_data["total_revenue"])
plt.title("Rating vs Total Revenue")
plt.xlabel("Rating")
plt.ylabel("Total Revenue")
plt.show()


# Checking if there are months where amazon sells more
# and if revenue changes across the years
amazon_data["order_date"] = pd.to_datetime(amazon_data["order_date"])
revenue_vs_month = amazon_data.set_index("order_date")["total_revenue"].resample("ME").sum()

plt.figure()
plt.plot(revenue_vs_month)
plt.title("Revenue vs Month ")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()
