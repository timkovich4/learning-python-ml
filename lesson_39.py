import ssl
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

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
# 1. Задаем "сетку" параметров, которые хотим проверить
param_grid = {
    'n_estimators': [50,100,200], # Лес из 50, 100 или 200 деревьев
    'max_depth': [3,5,10,None]    # Глубина 3, 5, 10 и без ограничений (None)
}
# 2. Создаем базовую модель (обязательно random_state=42 для воспроизводимости)
rf = RandomForestClassifier(random_state=42)

# 3. Настраиваем поисковик
# cv=5 означает кросс-валидацию: он будет делить X_train еще на 5 частей для надежной проверки
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy')

# 4. Запускаем перебор (это может занять пару секунд, так как он обучает десятки моделей)
grid_search.fit(X_train, y_train)

# 5. Выводим лучшие настройки, которые нашел GridSearch
print("Лучшие параметры:", grid_search.best_params_)

# 6. Берем лучшую модель из всех проверенных
best_model = grid_search.best_estimator_

# 7. Делаем предсказание уже с помощью лучшей модели
y_pred = best_model.predict(X_test)

# Считаем и выводим новую точность
accuracy = accuracy_score(y_test, y_pred)
print(f"Точность прокачанного Леса: {accuracy:.2%}")