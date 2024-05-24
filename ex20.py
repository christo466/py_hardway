# Import the argv function from the sys module to handle command-line arguments
from sys import argv

# Unpack the command-line arguments into script name and input file name
script, input_file = argv

# Define a function to print the entire content of a file
def print_all(f):
    print(f.read())

# Define a function to rewind the file to the beginning
def rewind(f):
    f.seek(0)

# Define a function to print a specific line from the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Open the input file in read mode
current_file = open(input_file)

# Print a message and then the entire content of the file
print("First let's print the whole file:\n")
print_all(current_file)

# Print a message and rewind the file to the beginning
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# Print a message and then print three lines from the file
print("Let's print three lines:")

# Initialize the current line number
current_line = 1
# Print the first line
print_a_line(current_line, current_file)

# Increment the current line number and print the next line
current_line = current_line + 1
print_a_line(current_line, current_file)

# Increment the current line number again and print the next line
current_line = current_line + 1
print_a_line(current_line, current_file)
