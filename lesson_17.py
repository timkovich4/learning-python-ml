import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#  Очищаем от пропусков в возрасте
df_clean = df.dropna(subset=["Age"])

plt.scatter(df_clean["Age"], df_clean["Fare"], color="green", alpha=0.5)

plt.xlabel("Возраст пассажиров")
plt.ylabel("Цена билета (USD)")
plt.title("Связь между возрастом и стоимостью билета")
plt.savefig("titanic_scatter.png", dpi=300, bbox_inches="tight")
plt.show()
