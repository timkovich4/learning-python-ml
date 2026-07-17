import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

plt.boxplot(df["Fare"])
plt.title("Распределение стоимости билетов (Boxplot)")
plt.ylabel("Cтоимость билета (USD)")
plt.savefig("titanic_fare_boxplot.png", dpi=300, bbox_inches="tight")
plt.show()