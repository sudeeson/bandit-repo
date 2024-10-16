# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

# Input from user
num = int(input("Enter a number: "))

# Calling the function
check_even_odd(num)
