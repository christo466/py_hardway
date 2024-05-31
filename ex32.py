# Initialize a list with a series of numbers
the_count = [1, 2, 3, 4, 5]

# Initialize a list with different types of fruits
fruits = ['apples', 'oranges', 'pears', 'apricots']

# Initialize a list with mixed data types: integers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Loop through the 'the_count' list and print each number
for number in the_count:
    print(f"This is count {number}")

# Loop through the 'fruits' list and print each fruit
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# Loop through the 'change' list and print each item
for i in change:
    print(f"I got {i}")

# Initialize an empty list to store elements
elements = []

# Loop from 0 to 5 (inclusive) and add each number to the 'elements' list
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)

# Loop through the 'elements' list and print each element
for i in elements:
    print(f"Element was: {i}")
