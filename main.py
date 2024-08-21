from predict import predict_price
from helpers import get_input
import os

mileage = get_input()
print(f'The estimated price of the car is: {predict_price(int(mileage))}')