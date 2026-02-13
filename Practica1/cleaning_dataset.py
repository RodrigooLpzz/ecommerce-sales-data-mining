import pandas as pd
import numpy as np

amazon_data = pd.read_csv("data/amazon_sales_dataset.csv")


print(f"Number of rows: {amazon_data.shape[0]}")
print(f"\nData Types:\n{amazon_data.dtypes}")


pd.set_option('display.max_columns', 20)

# Preview the dataset
print(f"\nData preview: \n{amazon_data.head(5)}")


print(f"\n{10*'*'} Null Validation {10*'*'}")
# Check for null values in the dataset
null_count = amazon_data.isnull().sum()
print(f"\nNull data in each column: \n{null_count}")

# Check for different types of null
types_of_null = ["", " ", "NA", "null"]

string_data_columns = amazon_data.select_dtypes(include=['string', 'object'])
different_types_of_null = string_data_columns.isin(types_of_null).sum()
print(f"\nIncomplete data or values with whitespace: \n{different_types_of_null}")



# Checking the types of columns only the order_id should be unique 
duplicated_orders = amazon_data["order_id"].duplicated()
print(f"\n\nDuplicated Rows in order_id: {duplicated_orders.sum()}")


print(f"\n{10*'*'} Date Validation {10*'*'}")
# Changing the format of dates it was string and now is datetime
incorrect_format_dates = (~amazon_data["order_date"].str.contains(r"^\d{4}-\d{2}-\d{2}$", regex=True)).sum()
print(f"\n\nNumber of rows with an incorrect date format: {incorrect_format_dates}")

if incorrect_format_dates == 0: 
  amazon_data["order_date"] = pd.to_datetime(amazon_data["order_date"])
  print(f"\nData Type: \norder_date: {amazon_data['order_date'].dtypes}")
  print(f"\nIncorrect dates after conversion: {amazon_data['order_date'].isnull().sum()}")



# Check for negative values in numeric columns
print(f"\n\n{10*'*'} Checking Specific Range Of Values {10*'*'}\n")
numeric_data_columns = amazon_data.select_dtypes(include=['int64', 'float64'])

print("\nChecking for negative values in numeric columns:")
for column in numeric_data_columns:
  number_of_negatives = (amazon_data[column] < 0).sum()
  print(f"{column}: {number_of_negatives}")


# Check if the price, quantity_sold and total_revenue is not zero 
print("\nChecking for zeros in columns where zero is not valid:")

print("Price:", (amazon_data["price"] == 0).sum())
print("Quantity sold:", (amazon_data["quantity_sold"] == 0).sum())
print("Total revenue:", (amazon_data["total_revenue"] == 0).sum())


# Rating should be between 0-5
print("\nChecking the rating values")
print("Rating values less than 0:", (amazon_data["rating"] < 0 ).sum())
print("Rating values more than 5:", (amazon_data["rating"] > 5 ).sum())


# Discount should be between 0 and 100
print("\nChecking the discount percent values")
print("Discount percent less than 0:", (amazon_data["discount_percent"] < 0 ).sum())
print("Discount percent more than 100:", (amazon_data["discount_percent"] > 100 ).sum())



amazon_data.to_csv("Practica1/amazon_sales_cleaned.csv", index=False)
