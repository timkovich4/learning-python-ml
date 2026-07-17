import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Средний возраст:", df["Age"].mean())
print("Медианный возраст:", df["Age"].median())
print("Средняя цена билета:", df["Fare"].mean())
print("Медианная цена билета:", df["Fare"].median())

# Отличие между средним и медианным значением в стоимости билета может быть связано с тем, что богачи покупали роскош и он стоил очень много, а бедные покупали обыный эконом и жили в обычнах каютах, чтоб главное дешего доплыть до Америки. 