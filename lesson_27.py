import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Выведет, что порт 'S' (Саутгемптон) встречается чаще всего (более 600 раз)
print(df["Embarked"].value_counts())
# Заполняем пропуски и перезаписываем столбец
df["Embarked"] = df["Embarked"].fillna("S")
# Проверяем, остались ли пропуски
print(df["Embarked"].isna().sum())