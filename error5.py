# This code will raise a ZeroDivisionError
def divide_numbers(a, b):
return a / b

# Calling the function with b = 0 will cause a division by zero error
result = divide_numbers(10, 0)
print(f"The result is: {result}")
