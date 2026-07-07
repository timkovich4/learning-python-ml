import matplotlib.pyplot as plt

months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"]
profit = [120000, 145000, 130000, 168000, 190000, 210000]

plt.plot(months, profit)

plt.title("Динамика прибыли за 6 месяцев")
plt.xlabel("Месяц")
plt.ylabel("Прибыль (руб.)")

plt.show()