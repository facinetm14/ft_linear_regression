import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from sklearn.metrics import r2_score, mean_absolute_error
from shared.helpers import read_dataset, get_theta
from predictor.predict import get_predicted_prices


mileage, prices = read_dataset("../data/data.csv")
theta0, theta1 = get_theta()
prices_pred = get_predicted_prices(mileage, theta0, theta1)


r2 = r2_score(prices, prices_pred)
mae = mean_absolute_error(prices, prices_pred)

print (f"R-squared score: {r2}")
print(f"Mean Absolute Error: {mae}")

