import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df_sorted = df.sort_values(by="Fare", ascending=False)
df_clean = df_sorted.reset_index(drop=True)
print(df_clean.head(10))