import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.pyplot as plt
from shared.helpers import read_dataset , get_theta
from predictor.predict import get_predicted_prices

x, y = read_dataset("../data/data.csv")
    
theta0, theta1 = get_theta()

y_pred = get_predicted_prices(x, theta0, theta1)
    

plt.title("Price repartition by mileage")
plt.xlabel("Mileage")
plt.ylabel("Price")


plt.scatter(x, y, color='blue', label='Actual prices')
plt.plot(x, y_pred, color='red', label='Predicted prices')

plt.legend()
plt.show()
