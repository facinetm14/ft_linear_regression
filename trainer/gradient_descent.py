# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient_descent.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fakouyat <fakouyat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/22 15:38:02 by fakouyat          #+#    #+#              #
#    Updated: 2024/09/22 15:38:03 by fakouyat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from predictor.predict import predict_price


def gradient_descent(
    mileage_data, price_data, theta0, theta1, learning_rate, iterations
):
    m = len(mileage_data)

    for iteration in range(iterations):
        tmp_theta0 = 0.0
        tmp_theta1 = 0.0

        for i in range(m):
            error = predict_price(mileage_data[i], theta0, theta1) - price_data[i]

            tmp_theta0 += error
            tmp_theta1 += error * mileage_data[i]

        theta0 -= (learning_rate / m) * tmp_theta0
        theta1 -= (learning_rate / m) * tmp_theta1

        if iteration % 100 == 0:
            print(f"Iteration {iteration} - Theta0 = {theta0}, Theta1 = {theta1}")

    return theta0, theta1
