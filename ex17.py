# Import the argv list from the sys module to handle command-line arguments
from sys import argv

# Import the exists function from the os.path module to check if a file exists
from os.path import exists

# Unpack the command-line arguments into respective variables
# The first element in argv is the script name, followed by the source and destination filenames
script, from_file, to_file = argv

# Inform the user about the file copying operation
print(f"Copying from {from_file} to {to_file}")

# Open the source file in read mode
in_file = open(from_file)
# Read the entire contents of the source file
indata = in_file.read()

# Print the size of the input file in bytes
print(f"The input file is {len(indata)} bytes long")

# Check if the destination file exists and print the result
print(f"Does the output file exist? {exists(to_file)}")
# Prompt the user to continue or abort the operation
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# Open the destination file in write mode
out_file = open(to_file, 'w')
# Write the contents of the source file to the destination file
out_file.write(indata)

# Inform the user that the operation is complete
print("Alright, all done.")

# Close the destination file to ensure data is saved and resources are freed
out_file.close()
# Close the source file
in_file.close()
