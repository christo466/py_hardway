# Import the argv function from the sys module to handle command-line arguments
from sys import argv

# Unpack the command-line arguments into respective variables
# The first argument is the script name, followed by user-provided arguments
# argv is a list that contains the command-line arguments passed to the script
# When you run `python script.py arg1 arg2 arg3`, argv will be ['script.py', 'arg1', 'arg2', 'arg3']
script, first, second, third = argv

# Print the script name
# This will output the name of the script being executed
print("The script is called:", script)


# This will output the first user-provided argument
print("Your first variable is:", first)


# This will output the second user-provided argument
print("Your second variable is:", second)


# This will output the third user-provided argument
print("Your third variable is:", third)
