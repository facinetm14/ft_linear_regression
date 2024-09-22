# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fakouyat <fakouyat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/22 15:37:27 by fakouyat          #+#    #+#              #
#    Updated: 2024/09/22 15:37:28 by fakouyat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from predictor.predict import predict_price
from shared.helpers import get_input, get_theta

def main():
    mileage = get_input()
    theta0, theta1 = get_theta()
    print(f'The estimated price of the car is: {predict_price(int(mileage), theta0, theta1)}')

if __name__== "__main__":
    main()