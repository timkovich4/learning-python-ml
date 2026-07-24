import ssl
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Отключаем проверку сертификатов (нужно для скачивания датасета)
ssl._create_default_https_context = ssl._create_unverified_context

# Загружаем данные
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# --- Подготовка данных ---
df = df.drop(columns=["Cabin"])
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df['Age'] = df['Age'].fillna(df.groupby(['Sex', 'Pclass'])['Age'].transform('median'))

df_encoded = pd.get_dummies(df, columns=["Sex", "Embarked"], dtype=int)
df_final = df_encoded.drop(columns=['PassengerId', 'Name', 'Ticket'])

# Разделение на X и y
X = df_final.drop(columns=['Survived'])
y = df_final['Survived']

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Разбивка на train и test
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, 
    y, 
    test_size=0.2,       
    random_state=42     
)

# --- Обучение и оценка модели ---
# 1. Создаем экземпляр модели
model = LogisticRegression()

# 2. Обучаем модель
model.fit(X_train, y_train)

# 3. Делаем предсказания
y_pred = model.predict(X_test)

# 4. Считаем и выводим метрики
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность модели: {accuracy:.2%}")

# Вывод подробный отчет о метриках
report = classification_report(y_test, y_pred)
print("Отчет о классификации:")
print(report)