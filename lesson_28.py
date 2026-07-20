import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Удаляем столбец Cabin (columns=['Cabin'])
df = df.drop(columns=["Cabin"])

# Заполнение пропусков в столбце Embarked модой (частым значением)
# .mode() возвращает Series, поэтому берем первый элемент [0]
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Заполнение пропусков в столбце Age медианой
df["Age"] = df["Age"].fillna(df["Age"].median())

# А так можно узнать процент пропусков, если поделить на общую длину таблицы
missing_zero = (df.isna().sum() / len(df)) * 100
print("\nПроцент пропусков по столбцам:")
print(missing_zero)