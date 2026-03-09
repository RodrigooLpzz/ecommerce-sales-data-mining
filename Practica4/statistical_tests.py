import pandas as pd
from scipy.stats import shapiro
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

# Checking which label column I can use with a numeric one
print(amazon_data.columns)

# Checking if the data follows a normal distribution
# If it doesn't, I will also run Kruskal-Wallis
sns.boxplot(x="product_category", y="total_revenue", data=amazon_data)
plt.title("Total Revenue by Product Category")
plt.xticks(rotation=45)
plt.show()

# In the readme I will explain why I didn't use this test for the others analyses
print(shapiro(amazon_data["total_revenue"]))

# Grouping total_revenue values by product category
first_group = amazon_data.groupby("product_category")["total_revenue"].apply(list)

anova_result = stats.f_oneway(*first_group)
print(anova_result)

# If the p value is greater than 0.05 there is no significant difference
if anova_result.pvalue < 0.05:
    print("\nSignificant difference")
else:
    print("\nNo significant difference")


# I use kruskal to check if it shows a different conclusion to the anova
result = stats.kruskal(*first_group)
print(result)

print("\nStatistical test 2 price vs product category\n")
sns.boxplot(x="product_category", y="price", data=amazon_data)
plt.xticks(rotation=45)
plt.title("Price by Product Category")
plt.show()

# Now checking the difference in prices between categories
groups2 = amazon_data.groupby("product_category")["price"].apply(list)

anova_result = stats.f_oneway(*groups2)
print(anova_result)

if anova_result.pvalue < 0.05:
    print("\nSignificant difference")
else:
    print("\nNo significant difference")

print(stats.kruskal(*groups2))


print("\nStatistical test 3 Rating vs Product category\n")

sns.boxplot(x="product_category", y="rating", data=amazon_data)
plt.xticks(rotation=45)
plt.title("Rating by Product category")
plt.show()

# Checking if product category affects rating
groups3 = amazon_data.groupby("product_category")["rating"].apply(list)

anova_result = stats.f_oneway(*groups3)
print(anova_result)

if anova_result.pvalue < 0.05:
    print("\nSignificant difference")
else:
    print("\nNo significant difference")

print(stats.kruskal(*groups3))


print("\nStatistical test 4 Total revenue vs Customer region\n")
sns.boxplot(x="customer_region", y="total_revenue", data=amazon_data)
plt.title("Total revenue by Customer region")
plt.show()

# Checking if the total revenue differs between customer regions
groups4 = amazon_data.groupby("customer_region")["total_revenue"].apply(list)

anova_result = stats.f_oneway(*groups4)
print(anova_result)

if anova_result.pvalue < 0.05:
    print("\nSignificant difference")
else:
    print("\nNo significant difference")

print(stats.kruskal(*groups4))


print("\nStatistical test 5 Quantity sold vs Customer region\n")


sns.boxplot(x="customer_region", y="quantity_sold", data=amazon_data)
plt.title("Quantity sold by Customer region")
plt.show()

# Checking if quantity sold differs between customer regions
groups5 = amazon_data.groupby("customer_region")["quantity_sold"].apply(list)
anova_result = stats.f_oneway(*groups5)
print(anova_result)

if anova_result.pvalue < 0.05:
    print("\nSignificant difference")
else:
    print("\nNo significant difference")

print(stats.kruskal(*groups5))
