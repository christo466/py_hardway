# Initialize variables to represent the number of people, cars, and trucks
people = 30
cars = 40
trucks = 15

# Check if the number of cars is greater than the number of people
if cars > people:
    
    print("We should take the cars.")

# Check if the number of cars is less than the number of people
elif cars < people:
    
    print("We can't decide.")

# Check if the number of trucks is greater than the number of cars
if trucks > cars:
   
    print("That's too many trucks.")

# Check if the number of trucks is less than the number of cars
elif trucks < cars:
  
    print("Maybe we could take the trucks.")

# This else statement covers the case where the number of trucks equals the number of cars
else:
    
    print("We still can't decide.")

# Check if the number of people is greater than the number of trucks
if people > trucks:
    
    print("Alright, let's just take the trucks.")

# This else statement covers the case where the number of people is not greater than the number of trucks
else:
    
    print("Fine, let's stay home then.")
