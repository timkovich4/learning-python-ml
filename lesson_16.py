import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df_clean = df.dropna(subset=["Age"])

plt.hist(df_clean["Age"], bins=20, color="skyblue", edgecolor="black")
plt.xlabel("Возраст пассажиров")
plt.ylabel("Количество людей")
plt.title("Распределение возраста пассажиров Титаника")
plt.savefig("titanic_age_hist.png", dpi=300, bbox_inches="tight")
plt.show()