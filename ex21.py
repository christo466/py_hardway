# Function to add two numbers
def add(a, b):
    print(f"ADDING {a} + {b}")  # Print the operation being performed
    return a + b  # Return the result of the addition

# Function to subtract one number from another
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")  # Print the operation being performed
    return a - b  # Return the result of the subtraction

# Function to multiply two numbers
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")  # Print the operation being performed
    return a * b  # Return the result of the multiplication

# Function to divide one number by another
def divide(a, b):
    print(f"DIVIDING {a} / {b}")  # Print the operation being performed
    return a / b  # Return the result of the division

print("Let's do some math with just functions!")

# Calculate age by adding 30 and 5
age = add(30, 5)

# Calculate height by subtracting 4 from 78
height = subtract(78, 4)

# Calculate weight by multiplying 90 by 2
weight = multiply(90, 2)

# Calculate IQ by dividing 100 by 2
iq = divide(100, 2)

# Print the results of the calculations
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# Print the result of the complex expression
print("That becomes: ", what, "can you do it by hand?")
