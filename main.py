from predict import predict_price
from helpers import get_input, get_theta
import os

def main():
    mileage = get_input()
    theta0, theta1 = get_theta()
    print(f'The estimated price of the car is: {predict_price(int(mileage), theta0, theta1)}')

if __name__== "__main__":
    main()