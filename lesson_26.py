import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Смотрим, сколько пропусков в каждом столбце
missing_data = df.isnull().sum()
print("Пропуски по столбцам:")
print(missing_data)

# А так можно узнать процент пропусков, если поделить на общую длину таблицы
missing_percent = (df.isna().sum() / len(df)) * 100
print("\nПроцент пропусков по столбцам:")
print(missing_percent)