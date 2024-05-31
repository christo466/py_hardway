# Initialize a variable i to 0
i = 0

# Initialize an empty list to store numbers
numbers = []

# Start a while loop that will run as long as i is less than 6
while i < 6:
   
    print(f"At the top i is {i}")
    
    # Append the current value of i to the numbers list
    numbers.append(i)
    
    # Increment i by 1
    i = i + 1
   
    print("Numbers now: ", numbers)
    
   
    print(f"At the bottom i is {i}")
    

print("The numbers: ")

# Iterate over each number in the numbers list
for num in numbers:
    
    print(num)
