# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fakouyat <fakouyat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/22 15:37:48 by fakouyat          #+#    #+#              #
#    Updated: 2024/09/22 17:17:38 by fakouyat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def predict_price(mileage, theta0, theta1):
     return theta0 + theta1 * mileage 

def get_predicted_prices(x, theta0, theta1):
    prices = []
    for i in range(len(x)):
        prices.append(predict_price(x[i], theta0, theta1))
    return prices