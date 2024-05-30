from sys import argv

# Prompt the user for their age and store the input in the variable 'age'
print("How old are you?", end=' ')
age = input()

# Prompt the user for their height and store the input in the variable 'height'
print("How tall are you?", end=' ')
height = input()

# Prompt the user for their weight and store the input in the variable 'weight'
print("How much do you weigh?", end=' ')
weight = input()

# Print the collected information using an f-string for formatted output
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# Unpack the command line arguments into 'script' and 'filename'
script, filename = argv

# Open the file specified by 'filename' for reading
txt = open(filename)

# Print the filename and the contents of the file
print(f"Here's your file {filename}:")
print(txt.read())

# Prompt the user to type the filename again
print("Type the filename again:")
file_again = input("> ")

# Open the file specified by the user's input for reading
txt_again = open(file_again)

# Print the contents of the file
print(txt_again.read())

# Print a statement indicating practice of different Python features
print("Let's practice everything.")

# Print a string with escaped characters for demonstration
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

# Define a multi-line string (poem) with embedded tabs and newlines
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Print the poem within a visual separator
print("--------------")
print(poem)
print("--------------")

# Perform a simple arithmetic operation and store the result in 'five'
five = 10 - 2 + 3 - 6

# Print the result of the arithmetic operation
print(f"This should be five: {five}")

# Define a function that performs calculations and returns multiple values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# Set the starting point for calculations
start_point = 10000

# Call the function with the starting point and unpack the results into variables
beans, jars, crates = secret_formula(start_point)

# Print the results using the format method
print("With a starting point of: {}".format(start_point))

# Print the results using an f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Update the starting point by dividing it by 10
start_point = start_point / 10

# Print a statement indicating another way to do the same thing
print("We can also do that this way:")

# Call the function again with the updated starting point
formula = secret_formula(start_point)

# Print the results using the format method and unpacking the list directly into the format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

# Define variables for the number of people, cats, and dogs
people = 20
cats = 30
dogs = 15

# Check if there are more cats than people and print a message if true
if people < cats:
    print("Too many cats! The world is doomed!")

# Check if there are fewer cats than people and print a message if true
if people > cats:
    print("Not many cats! The world is saved!")

# Check if there are more dogs than people and print a message if true
if people < dogs:
    print("The world is drooled on!")

# Check if there are more people than dogs and print a message if true
if people > dogs:
    print("The world is dry!")

# Increase the number of dogs by 5
dogs += 5

# Check if the number of people is greater than or equal to the number of dogs and print a message if true
if people >= dogs:
    print("People are greater than or equal to dogs.")

# Check if the number of people is less than or equal to the number of dogs and print a message if true
if people <= dogs:
    print("People are less than or equal to dogs.")

# Check if the number of people is equal to the number of dogs and print a message if true
if people == dogs:
    print("People are dogs.")
