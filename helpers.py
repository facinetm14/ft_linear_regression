def get_input():
  msg = 'Please enter the mileage of the car: '
  attempt = 0

  while True:
    user_input = input(msg)
    if (user_input.isnumeric()):
      return int(user_input)
    if (not attempt):
      msg = 'Invalid input. Please enter a number for mileage: '
      attempt += 1
      