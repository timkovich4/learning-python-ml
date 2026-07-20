import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Базовая очистка (Cabin удаляем, Embarked модой, Age групповой медианой)
df = df.drop(columns=["Cabin"])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df.groupby(['Sex', 'Pclass'])['Age'].transform('median'))

# Превращаем категориальные столбцы в бинарные столбцы 0 и 1 (One-Hot Encoding (OHE))
df_encoded = pd.get_dummies(df, columns=["Sex", "Embarked"], dtype=int)

print(df_encoded.head())
print("-" * 50)
print(df_encoded.info())