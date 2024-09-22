# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    training.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fakouyat <fakouyat@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/22 15:37:41 by fakouyat          #+#    #+#              #
#    Updated: 2024/09/22 15:37:42 by fakouyat         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from shared.helpers import read_dataset
from gradient_descent import gradient_descent


def train_model(
    data_src="../data/data.csv",
    theta_values_src="theta_values.txt",
    learning_rate=0.00000000000009,
    iterations=1000,
):
    mileage_data, price_data = read_dataset(data_src)

    theta0 = 0.0
    theta1 = 0.0

    theta0, theta1 = gradient_descent(
        mileage_data, price_data, theta0, theta1, learning_rate, iterations
    )

    with open(theta_values_src, "w") as f:
        f.write(f"{theta0}\n")
        f.write(f"{theta1}\n")

    print(f"Training complete. Theta0 = {theta0}, Theta1 = {theta1}")


if __name__ == "__main__":
    train_model()
