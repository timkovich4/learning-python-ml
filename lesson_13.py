import matplotlib.pyplot as plt

departments = ["Электроника", "Одежда", "Продукты", "Книги", "Игрушки"]
sales = [450000, 280000, 610000, 120000, 190000]

plt.bar(departments, sales, color = "#0D98BA")
plt.xlabel("Отделы")
plt.ylabel("Продажи (руб.)")
plt.grid(True)
plt.title("Выручка по отделам магазина за месяц")
plt.show()