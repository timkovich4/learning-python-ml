import matplotlib.pyplot as plt

months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"]
income = [160000, 185000, 175000, 210000, 240000, 260000]
expenses = [120000, 130000, 140000, 150000, 160000, 165000]

plt.plot(months, income, color = "green", marker = "o", label = "Доходы")
plt.plot(months, expenses, color = "red", marker = "s", label = "Расходы")
plt.grid(True)
plt.title("Финансовые показатели компании")
plt.xlabel("Месяц")
plt.ylabel("Сумма (руб.)")
plt.legend()
plt.show()
