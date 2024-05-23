# Import the argv list from the sys module to handle command-line arguments
from sys import argv

# Unpack the command-line arguments into respective variables
# The first element in argv is the script name, followed by the filename provided by the user
script, filename = argv

# Open the file with the name provided as the second command-line argument
txt = open(filename)

# Print the name of the file being opened
print(f"Here's your file {filename}:")

# Read the contents of the file and print it to the console
print(txt.read())

# Close the file after reading its contents
txt.close()

# Prompt the user to type the filename again
print("Type the filename again:")
# Capture the user's input for the filename
file_again = input("> ")

# Open the file with the name provided by the user input
txt_again = open(file_again)

# Read the contents of the file and print it to the console
print(txt_again.read())

# Close the file after reading its contents
txt_again.close()
