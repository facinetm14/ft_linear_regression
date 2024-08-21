from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.read_csv('../dataset/data.csv')

x = data[['km']]
y = data[['price']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print('x_train:', x_train)
print('x_test:', x_test)
print('y_train:', y_train)
print('y_test:', y_test)

model = LinearRegression() 
model.fit(x_train, y_train)

print(f'Coefficient: {model.coef_}')
print(f'Intercept: {model.intercept_}')
print(f'Score: {model.score(x_test, y_test)}')

