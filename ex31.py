# Print the initial prompt asking the player to choose a door
print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2?""")

# Get the player's choice of door
door = input("> ")

# If player chooses door #1
if door == "1":
    # Describe the scenario behind door #1
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    # Get the player's choice of action
    bear = input("> ")
    # Outcome based on player's choice
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        # Default outcome if player enters something other than 1 or 2
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
        
# If player chooses door #2
elif door == "2":
    # Describe the scenario behind door #2
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    # Get the player's choice of action
    insanity = input("> ")
    # Outcome based on player's choice
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
# Default outcome if player chooses neither door #1 nor door #2
else:
    print("You stumble around and fall on a knife and die. Good job!")
