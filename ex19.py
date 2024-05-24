# Define a function named 'cheese_and_crackers' that takes two parameters: 'cheese_count' and 'boxes_of_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Print the number of cheeses using an f-string
    print(f"You have {cheese_count} cheeses!")
    # Print the number of boxes of crackers using an f-string
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Print a message indicating that's enough for a party
    print("Man that's enough for a party!")
    # Print a message suggesting to get a blanket, followed by a newline character
    print("Get a blanket.\n")

# Example 1: Call the function with numeric literals
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Example 2: Call the function with variables
print("OR, we can use variables from our script:")
# Assign values to variables
amount_of_cheese = 10
amount_of_crackers = 50
# Call the function using the variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Example 3: Call the function with expressions (math operations)
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Example 4: Call the function with a combination of variables and expressions
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
