import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df.head(5))
df.info()
print(df.describe())

print(df.iloc[0,1])
print(df.loc[0:9, ["Sex", "Fare"]])

children = df[df["Age"] <18 ]
print(len(children))
