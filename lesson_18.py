import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df_first10 = df.head(10)

plt.figure(figsize=(12, 6))

plt.bar(df_first10["Name"], df_first10["Fare"], color="orange", alpha=0.7)
plt.xlabel("Имена пассажиров")
plt.ylabel("Цена билета (USD)")
plt.title("Стоимость билетов первых 10 пассажиров (по именам)")
plt.xticks(rotation=45, ha="right")

# Автоматически подгоняем размеры, чтобы имена не обрезались
plt.tight_layout()

plt.savefig("titanic_names_fares.png", dpi=300, bbox_inches="tight")
plt.show()
