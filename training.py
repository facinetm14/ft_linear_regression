from helpers import read_dataset
from predict import predict_price

def compute_cost(mileage_data, price_data, theta0, theta1):
    m = len(mileage_data)
    total_cost = 0
    for i in range(m):
        prediction = predict_price(mileage_data[i], theta0, theta1)
        total_cost += (prediction - price_data[i]) ** 2
    return total_cost / (2 * m)

def gradient_descent(mileage_data, price_data, theta0, theta1, learning_rate, iterations):
    m = len(mileage_data)
    for iteration in range(iterations): 
        tmp_theta0 = 0.0
        tmp_theta1 = 0.0
        
        for i in range(m):
            prediction = predict_price(mileage_data[i], theta0, theta1)
            error = prediction - price_data[i]
            
            tmp_theta0 += error
            tmp_theta1 += error * mileage_data[i]

        theta0 -= (learning_rate / m) * tmp_theta0
        theta1 -= (learning_rate / m) * tmp_theta1


        if (iteration % 100 == 0):
            cost = compute_cost(mileage_data, price_data, theta0, theta1)
            print(f"Iteration {iteration} - Cost: {cost} - Theta0 = {theta0}, Theta1 = {theta1}")
    
    return theta0, theta1

def train_model(data_src = "data/data.csv", theta_values_src = "theta_values.txt", learning_rate=-0.42, iterations=10000):
    mileage_data, price_data = read_dataset(data_src)
    
    theta0 = 0.0
    theta1 = 0.0

    print(f"mileag_data {mileage_data} \n price data {price_data}")
    theta0, theta1 = gradient_descent(mileage_data, price_data, theta0, theta1, learning_rate, iterations)
    
    with open(theta_values_src, "w") as f:
        f.write(f"{theta0}\n")
        f.write(f"{theta1}\n")
    
    print(f"Training complete. Theta0 = {theta0}, Theta1 = {theta1}")


if __name__ == "__main__":
  train_model()