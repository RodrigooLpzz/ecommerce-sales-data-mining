import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

amazon_data = pd.read_csv("Practica1/amazon_sales_cleaned.csv")

# the dataset doesnt have text so I use the categorical columns
# i join all of them in one variable and repeat each word by the times it appears
text = ""
for category, count in amazon_data["product_category"].value_counts().items():
    word = category.replace(" ", "_")
    text += (word + " ") * count

for method, count in amazon_data["payment_method"].value_counts().items():
    word = method.replace(" ", "_")
    text += (word + " ") * count

for region, count in amazon_data["customer_region"].value_counts().items():
    word = region.replace(" ", "_")
    text += (word + " ") * count

print(f"Total words generated: {len(text.split())}")

wordcloud = WordCloud(width=800, height=400, background_color="white", collocations=False)
wordcloud.generate(text)

plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Word cloud amazon dataset")
plt.show()
