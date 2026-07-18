import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

survived_stats = df.groupby("Sex")["Survived"].agg(["mean", "median", "count"])
mean_fare_by_class = df.groupby("Pclass")["Survived"].mean()
print(mean_fare_by_class)
print(survived_stats)

