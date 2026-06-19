import matplotlib.pyplot as plt
import numpy as np


def analyze_climate(data):
    temperatures_array = np.array(data)
        
    print(f"Максимальная температура: {np.max(temperatures_array)}")
    print(f"Минимальная температура: {np.min(temperatures_array)}")
    print(f"Средняя температура: {np.mean(temperatures_array):.1f}")

    temperatures = [20.1, 23.5, 25.0, 28.2, 27.5, 24.0, 19.5]  
    day_namber = 1

    for temp in temperatures:
        if temp > 26:
            print(f"День №{day_namber} был таким жарким!")
        day_namber = day_namber + 1
    

    days = [1, 2, 3, 4, 5, 6, 7]

    plt.plot(days, temperatures_array, color = "blue", marker = "o")

    plt.title("Отчет погоды за 7 дней")
    plt.xlabel("День")
    plt.ylabel("Температура(°C)")
    plt.grid(True)

    plt.show()

room_data = [20.1, 23.5, 25.0, 28.2, 27.5, 24.0, 19.5]

analyze_climate(room_data)