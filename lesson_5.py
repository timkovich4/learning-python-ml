import numpy as np
import pandas as pd

# Специально создаем данные с пропусками (None превратится в NaN)
dirty_data = {
    "Комната": ["Кухня", "Кухня", "Спальня", "Спальня", "Кухня", "Спальня"],
    "Температура": [22.0, None, 21.5, 20.0, 24.5, None],
    "Влажность": [45, 40, None, 42, 38, 47],
}

df = pd.DataFrame(dirty_data)
print("--- Исходная таблица с пропусками ---")
print(df)

mean_temperature = df["Температура"].mean()
df["Температура"] = df["Температура"].fillna(mean_temperature)
df['Влажность'] = df['Влажность'].fillna(40)

room_summary = df.groupby("Комната")["Температура"].max()
print(room_summary)