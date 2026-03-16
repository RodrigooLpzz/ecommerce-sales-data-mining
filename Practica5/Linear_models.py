import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

# Checking the correlation between the variables that will be used
# corr method uses the pearson correlation by default

price_revenue_corr = amazon_data["price"].corr(amazon_data["total_revenue"])
print(f"Correlation between price and total revenus {price_revenue_corr:.2f}")

plt.figure()
plt.scatter(amazon_data["price"], amazon_data["total_revenue"])
plt.title("Price vs Total revenue")
plt.xlabel("Price")
plt.ylabel("Total revenue")
plt.show()


quantity_revenue_corr = amazon_data["quantity_sold"].corr(amazon_data["total_revenue"])
print(f"Correlation between quantity sold and total revenue {quantity_revenue_corr:.2f}")

plt.figure()
plt.scatter(amazon_data["quantity_sold"], amazon_data["total_revenue"])
plt.title("Quantity sold vs Total revenue")
plt.xlabel("Quantity sold")
plt.ylabel("Total revenue")
plt.show()


price_quantity_corr = amazon_data["price"].corr(amazon_data["quantity_sold"])
print(f"Correlation between price and quantity sold {price_quantity_corr:.2f}")

plt.figure()
plt.scatter(amazon_data["price"], amazon_data["quantity_sold"])
plt.title("Price vs Quantity sold")
plt.xlabel("Price")
plt.ylabel("Quantity sold")
plt.show()


# I choose price as the independent variable and total revenue as the dependent variable
# as we saw in the correlation graph when price increases the revenue also increases

X = amazon_data[["price"]]
y = amazon_data["total_revenue"]

model = LinearRegression()
model.fit(X, y)

simple_regression = model.predict(X)

r2 = r2_score(y, simple_regression)
print("\nR2:", r2)



# To have a better R2 something that changes the total revenue is the quantity
# from the correlation graph we saw that when quantity increases, total revenue 
# also increases

X_multi = amazon_data[["price", "quantity_sold"]]

model_multi = LinearRegression()
model_multi.fit(X_multi, y)

multi_regression = model_multi.predict(X_multi)

r2_multi = r2_score(y, multi_regression)

print("\nR2 price, quantity sold, total revenue:", r2_multi)

print("Intercept:", model_multi.intercept_)
print("Coefficients:", model_multi.coef_)