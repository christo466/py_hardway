# Print a simple statement
print("Let's practice everything.")

# Print a statement demonstrating the use of escape sequences
print('You\'d need to know \'bout escapes with \\ that do:')

# Print a statement showing how newlines (\n) and tabs (\t) work
print('\n newlines and \t tabs.')

# Define a multi-line string (poem) using triple quotes
poem = """
\tThe lovely world 
with logic so firmly planted 
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# Print a separator line of dots
print("...................")

# Print the poem variable, which includes formatted text with tabs and newlines
print(poem)

# Print another separator line of dots
print("...................")

# Perform basic arithmetic to calculate the value of five
five = 10 - 2 + 3 - 6

# Print the result using an f-string to embed the value of five in the string
print(f"This should be five: {five}")

# Define a function named secret_formula that calculates jelly_beans, jars, and crates
def secret_formula(started):
    jelly_beans = started * 500  # Calculate the number of jelly beans
    jars = jelly_beans / 1000    # Calculate the number of jars
    crates = jars / 100          # Calculate the number of crates
    return jelly_beans, jars, crates  # Return the calculated values as a tuple

# Set the initial start_point value
start_point = 10000

# Call the secret_formula function with start_point and unpack the returned values
beans, jars, crates = secret_formula(start_point)

# Print the starting point using the .format() method for string formatting
print("With a starting point of: {}".format(start_point))

# Print the calculated values using an f-string for string formatting
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Update the start_point by dividing it by 10
start_point = start_point / 10

# Print a statement indicating another method to format strings
print("We can also do that this way:")

# Call the secret_formula function with the updated start_point and store the result in formula
formula = secret_formula(start_point)

# Print the calculated values using the .format() method with unpacking the tuple
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
