import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df_first10 = df.head(10)
plt.bar(df_first10["PassengerId"], df_first10["Fare"], color="purple")
plt.xlabel("ID Пассажира")
plt.ylabel("Цена билета(USD)")
plt.title("Стоимость билетов первых 10 пассажиров")
plt.savefig("titanic_fares.png", dpi=300, bbox_inches="tight")
plt.show()