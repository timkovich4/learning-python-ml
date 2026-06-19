import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperatures = [22.5, 25.0, 19.8, 31.2, 24.1]

plt.plot(days, temperatures, color="green", marker="o") # Сделаем линию зеленой и добавим точки-маркеры

# Добавляем оформление
plt.title("Мониторинг температуры")
plt.xlabel("Дни недели")
plt.ylabel("Градусы Цельсия")
plt.grid(True) # Включаем сетку

plt.show()