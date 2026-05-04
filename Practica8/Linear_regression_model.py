import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

# get the revenue by month
amazon_data["order_date"] = pd.to_datetime(amazon_data["order_date"])
revenue_by_month = amazon_data.set_index("order_date")["total_revenue"].resample("ME").sum()

print(revenue_by_month)

# the model needs numbers not dates
time_index = np.array(range(len(revenue_by_month))).reshape(-1, 1)
revenue = revenue_by_month.values

# first 18 months to train the model
X_train = time_index[:18]
X_test = time_index[18:]
y_train = revenue[:18]
y_test = revenue[18:]

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(f"\nR2: {r2:.4f}")
print(f"Coefficient: {model.coef_[0]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

print("\nTest months:")
for i in range(len(y_test)):
    month_label = revenue_by_month.index[18 + i].strftime("%Y-%m")
    print(f"{month_label} real: {y_test[i]:,.2f} pred: {y_pred[i]:,.2f}")

# predict 6 months that i dont have
next_months = 6
future_x = np.array(range(24, 24 + next_months)).reshape(-1, 1)
future_pred = model.predict(future_x)

future_dates = pd.date_range("2024-01-31", periods=next_months, freq="ME")

print("\nPrediction next months:")
for date, value in zip(future_dates, future_pred):
    print(f"{date.strftime('%Y-%m')}: {value:,.2f}")

plt.figure()
plt.plot(revenue_by_month.index, revenue)
plt.plot(revenue_by_month.index[18:], y_pred)
plt.plot(future_dates, future_pred)
plt.title("Monthly revenue forecast")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()
