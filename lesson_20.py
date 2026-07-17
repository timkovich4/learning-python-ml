import ssl
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

q1 = df["Fare"].quantile(0.25)
q3 = df["Fare"].quantile(0.75)
iqr = q3 - q1

print(iqr)


#25-й перцентиль (Первый квартиль, q1): 25% значений в данных меньше этого числа.

#50-й перцентиль (q2): Это наша старая знакомая — медиана. 50% данных меньше неё.

#75-й перцентиль (Третий квартиль, q3): 75% значений меньше этого числа (и, соответственно, 25% больше него).

#Разница между третьим и первым квартилем (q3 - q1) называется межквартильным размахом (IQR — Interquartile Range). Она показывает, в каком диапазоне лежит ровно половина (50%) самых "типичных" средних значений, отсекая экстремально маленькие и экстремально большие выбросы.