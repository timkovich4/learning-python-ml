import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Пропуски до:")
print(df.isna().sum())

mean_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(mean_age)

df_clean_embarked = df.dropna(subset=["Embarked"])

print("\nПропуски после:")
print(df_clean_embarked.isna().sum())
