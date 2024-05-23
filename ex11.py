# Print a question asking for the user's age and keep the cursor on the same line
print("How old are you?", end=' ')

# Read the user's input from the keyboard and store it in the variable 'age'
age = input()

# Print a question asking for the user's height and keep the cursor on the same line
print("How tall are you?", end=' ')

# Read the user's input from the keyboard and store it in the variable 'height'
height = input()

# Print a question asking for the user's weight and keep the cursor on the same line
print("How much do you weigh?", end=' ')

# Read the user's input from the keyboard and store it in the variable 'weight'
weight = input()

# Print a summary statement using an f-string to format the user's input values
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
