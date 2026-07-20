import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 1. Удаляем неинформативный столбец Cabin
df = df.drop(columns=["Cabin"])

# 2. Выводим сами медианы на экран, чтобы увидеть разницу между группами
print("Медианный возраст по группам (Sex + Pclass):")
print(df.groupby(['Sex', 'Pclass'])['Age'].median())
print("-" * 40)

# 3. Заполняем пропуски умной медианой по группам
df['Age'] = df['Age'].fillna(df.groupby(['Sex', 'Pclass'])['Age'].transform('median'))

# 4. Проверяем процент пропусков
missing_zero = (df.isna().sum() / len(df)) * 100
print("\nПроцент пропусков по столбцам:")
print(missing_zero)