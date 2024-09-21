def get_input():
  msg = 'Please enter the mileage of the car: '
  attempt = 0

  while True:
    user_input = input(msg)
    if (user_input.isnumeric()):
      return float(user_input)
    if (not attempt):
      msg = 'Invalid input. Please enter a number for mileage: '
      attempt += 1

def get_theta(theta_values_src ="theta_values.txt"):
    with open(theta_values_src, "r") as f:
        theta0, theta1 = map(float, f.readlines())
    return theta0, theta1

def read_dataset(file_name):
    mileage = []
    price = []
    
    with open(file_name, "r") as f:
        next(f)
        for line in f:
            m, p = line.strip().split(',')
            mileage.append(float(m))
            price.append(float(p))
    
    return mileage, price

