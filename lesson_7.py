import pandas as pd

data_records = {
    "id_датчика":[101, 102, 101, 103, 102],
    "Температура": [21.5, 23.0, 22.0, 19.5, 24.0]
}
df_records = pd.DataFrame(data_records)

data_rooms = {
    "id_датчика": [101, 102, 103],
    "Комната": ["Кухня", "Гостиная", "Спальня"]
}
df_rooms = pd.DataFrame(data_rooms)

df_merged = pd.merge(df_records, df_rooms, on="id_датчика")
rooms = df_merged.groupby("Комната")["Температура"].mean()

print(rooms)