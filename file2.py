 if last_digit > 5:
    # Perform bitwise right shift by 2
    shifted_number = number >> 2
    print(f"The last digit of {number} is {last_digit}, which is greater than 5.")
    print(f"Performing bitwise right shift by 2: {number} >> 2 = {shifted_number}")
  else:
    print(f"The last digit of {number} is {last_digit}, which is not greater than 5.")