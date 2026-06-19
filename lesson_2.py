import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temps = [22.5, 25.0, 19.8, 31.2, 24.1]

plt.plot(days, temps, color = "blue", marker = "o")

plt.title("Отчет погоды за 5 деней")
plt.xlabel("День")
plt.ylabel("Температура(°C)")
plt.grid(True)

plt.show()