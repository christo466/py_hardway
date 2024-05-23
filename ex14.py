# Import the argv list from the sys module to handle command-line arguments
from sys import argv

# Unpack the command-line arguments into respective variables
# The first element in argv is the script name, followed by the user-provided arguments
script, user_name = argv

# Define a prompt symbol for user input
prompt = '> '

# Greet the user by name and mention the script name
print(f"Hi {user_name}, I'm the {script} script.")

# Inform the user that some questions will be asked
print("I'd like to ask you a few questions.")

# Ask the user if they like the script
print(f"Do you like me {user_name}?")
# Capture the user's response to the 'like' question using the prompt symbol
like = input(prompt)

# Ask the user where they live
print(f"Where do you live {user_name}?")
# Capture the user's response to the 'lives' question using the prompt symbol
lives = input(prompt)

# Ask the user what kind of computer they have
print("What kind of computer do you have?")
# Capture the user's response to the 'computer' question using the prompt symbol
computer = input(prompt)

# Summarize the collected information and print it in a formatted manner
print(f"""
Alright, so you said {like} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
