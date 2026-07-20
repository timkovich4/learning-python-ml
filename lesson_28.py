import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df = df.drop(columns=["Cabin"])


df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


df["Age"] = df["Age"].fillna(df["Age"].median())


missing_zero = (df.isna().sum() / len(df)) * 100
print("\nПроцент пропусков по столбцам:")
print(missing_zero)