import ssl
import pandas as pd
from sklearn.preprocessing import StandardScaler

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

# Выводим первые 5 строк масштабированных данных
print(X_scaled[:5])