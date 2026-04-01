import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report


def knn_test(x, y):

  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

  # scaling the data knn its affected by big numbers
  scaler = StandardScaler()
  x_train = scaler.fit_transform(x_train)
  x_test = scaler.transform(x_test)

  errors = []

  # different k values to see which one works better
  for i in range(1, 21):
      model = KNeighborsClassifier(n_neighbors=i)
      scores = cross_val_score(model, x_train, y_train, cv=5)
      errors.append(1 - scores.mean())

  plt.figure()
  plt.plot(range(1, 21), errors, marker='o')
  plt.title('Error vs K')
  plt.xlabel('K')
  plt.ylabel('Error')
  plt.show()

  # taking the best k to do the knn classification
  best_k = errors.index(min(errors)) + 1
  print("\nBest k:", best_k)

  final_model = KNeighborsClassifier(n_neighbors=best_k)
  final_model.fit(x_train, y_train)

  predictions = final_model.predict(x_test)

  print(confusion_matrix(y_test, predictions))
  print(classification_report(y_test, predictions))


amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")
# print(amazon_data.dtypes)


# First I tried using basic columns like price, quantity and discount
X = amazon_data[['price', 'quantity_sold', 'discount_percent']]
y = amazon_data['product_category']
knn_test(X, y)


X = amazon_data[['price', 'quantity_sold', 'discount_percent', 'rating']]
y = amazon_data['product_category']
knn_test(X, y)


# Checking if using more columns improves the result
X = amazon_data[['price', 'quantity_sold', 'discount_percent', 'rating', 'review_count']]
y = amazon_data['product_category']
knn_test(X, y)


amazon_data["rating_label"] = amazon_data["rating"].apply(
    lambda x: "Good" if x >= 4 else "Bad"
)

# checking if the rating label has more relation with the others
X = amazon_data[['price', 'quantity_sold', 'discount_percent']]
y = amazon_data['rating_label']
knn_test(X, y)