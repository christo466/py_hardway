# Define a function that accepts a variable number of arguments
def print_two(*args):
    # Unpack the arguments into individual variables
    arg1, arg2 = args
    # Print the arguments
    print(f"arg1: {arg1}, arg2: {arg2}")

# Define a function that accepts exactly two arguments
def print_two_again(arg1, arg2):
    # Print the arguments
    print(f"arg1: {arg1}, arg2: {arg2}")

# Define a function that accepts exactly one argument
def print_one(arg1):
    # Print the argument
    print(f"arg1: {arg1}")

# Define a function that accepts no arguments
def print_none():
    # Print a message indicating no arguments
    print("I got nothing'.")

# Call the function with two arguments using the *args syntax
print_two("zed", "shaw")

# Call the function with two arguments using direct argument passing
print_two_again("zed", "Shaw")

# Call the function with one argument
print_one("First!")

# Call the function with no arguments
print_none()
