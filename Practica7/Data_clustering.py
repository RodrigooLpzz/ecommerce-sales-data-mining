import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

# First test using price and total revenue
X = amazon_data[['price', 'total_revenue']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
inertias = []

# different k values
for i in range(1, 11):
    model = KMeans(n_clusters=i, random_state=42, n_init=10)
    model.fit(X_scaled)
    inertias.append(model.inertia_)

plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.show()

# k 3 is where it looks like elbow
k = 3

model = KMeans(n_clusters=k, random_state=42, n_init=10)
amazon_data['cluster1'] = model.fit_predict(X_scaled)

sns.scatterplot(x='price', y='total_revenue', hue='cluster1', data=amazon_data)
plt.title("Price vs revenue clusters")
plt.show()

print("\nUsing k = 3")
score = silhouette_score(X_scaled, amazon_data['cluster1'])
print("\nSilhouette score:", score)


# Second test using rating and quantity sold
X2 = amazon_data[['rating', 'quantity_sold']]
X_scaled2 = scaler.fit_transform(X2)

inertias2 = []

for i in range(1, 11):
    model = KMeans(n_clusters=i, random_state=42, n_init=10)
    model.fit(X_scaled2)
    inertias2.append(model.inertia_)

plt.plot(range(1, 11), inertias2, marker='o')
plt.title('Elbow method 2')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.show()

k2 = 4
model2 = KMeans(n_clusters=k2, random_state=42, n_init=10)
amazon_data['cluster2'] = model2.fit_predict(X_scaled2)

sns.scatterplot(x='rating', y='quantity_sold', hue='cluster2', data=amazon_data)
plt.title("Rating vs quantity clusters")
plt.show()


score2 = silhouette_score(X_scaled2, amazon_data['cluster2'])
print("\nUsing k = 4")
print("\n~Silhouette score 2:", score2)