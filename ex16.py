# Import the argv list from the sys module to handle command-line arguments
from sys import argv

# Unpack the command-line arguments into respective variables
# The first element in argv is the script name, followed by the filename provided by the user
script, filename = argv

# Inform the user that the specified file will be erased
print(f"We're going to erase {filename}.")
# Provide instructions for the user to abort or continue the operation
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Wait for user input to proceed
input("?")

# Open the file in write mode, which will also truncate the file (clear its contents)
print("Opening the file...")
target = open(filename, 'w')

# Explicitly truncate the file to ensure its contents are cleared
print("Truncating the file. Goodbye!")
target.truncate()

# Prompt the user to enter three lines of text
print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Inform the user that the lines will be written to the file
print("I'm going to write these to the file.")

# Write the three lines to the file, each followed by a newline character
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file to ensure the data is saved and resources are freed
print("And finally, we close it.")
target.close()

