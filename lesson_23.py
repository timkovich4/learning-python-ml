import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df.groupby("Sex")["Survived"].mean().plot(kind="bar", color="#003366", edgecolor="black")

plt.title("Доля выживших пассажиров по половому признаку")
plt.xlabel("Пол")
plt.ylabel("Доля выживших (0.0 - 1.0)")
plt.xticks(rotation=0)
plt.savefig("survived_by_sex.png", dpi=300, bbox_inches="tight")
plt.show()