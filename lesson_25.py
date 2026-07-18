import ssl
import pandas as pd
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

pivot_swapped = df.pivot_table(
    values="Survived", 
    index="Sex",      
    columns="Pclass",  
    aggfunc="mean"     
)
# Рисуем тепловую карту на основе нашей pivot-таблицы
plt.imshow(pivot_swapped, cmap="YlGnBu", aspect="auto") 
plt.colorbar(label="Доля выживших") # Добавляем шкалу цветов справа

# Настраиваем подписи осей, чтобы вместо индексов были понятные слова
plt.xticks(range(len(pivot_swapped.columns)), pivot_swapped.columns)
plt.yticks(range(len(pivot_swapped.index)), pivot_swapped.index)

plt.title("Тепловая карта выживаемости (Пол vs Класс)")
plt.savefig("survival_heatmap.png", dpi=300, bbox_inches="tight")
plt.show()
print(pivot_swapped)