# Task 1
def welcome_message():
    # Ask the user for their name, age, and favorite color
    # Return a formatted welcome message
    name = input("Enter your name:")
    age = input("Enter your age:")
    color = input("Enter your favourite color:")
    print(f"Hello, {name}! You are {age} years old and your favourite color is {color}")
    pass

# Task 2


def add_two_numbers():
    # Ask the user to enter two numbers
    # Add them together, print and return the result
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    print(f"SUM: {sum}")
    pass

# Task 3


def is_even(number):
    # Return True if number is even, False if odd
    if num %2 ==0:
        return True
    else:
        return False
    pass
    
welcome_message()
add_two_numbers()
num = int(input("Enter a number: "))
print(is_even(num))
