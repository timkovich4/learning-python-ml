import ssl
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df = df.drop(columns=["Cabin"])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df.groupby(['Sex', 'Pclass'])['Age'].transform('median'))

df_encoded = pd.get_dummies(df, columns=["Sex", "Embarked"], dtype=int)
df_final = df_encoded.drop(columns=['PassengerId', 'Name', 'Ticket'])

# Разделение и масштабирование
X = df_final.drop(columns=['Survived'])
y = df_final['Survived']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разделяем X и y на 4 части: X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, 
    y, 
    test_size=0.2,       # 20% данных уходит в тест, 80% — в обучение
    random_state=42     # Фиксируем случайность, чтобы результаты воспроизводились
)

# 1. Создаем экземпляр модели
model = LogisticRegression()

# 2. Обучаем модель на ТРЕНИРОВОЧНЫХ данных (учим паттерны)
model.fit(X_train, y_train)

# 3. Делаем предсказание на ТЕСТОВЫХ признаках (сдаем экзамен)
y_pred = model.predict(X_test)

# 4. Сравниваем предсказания y_pred с правильными ответами y_test
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy:.2%}")