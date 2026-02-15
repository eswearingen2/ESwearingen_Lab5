"""
Dice Rolling Terms,
Ethan Swearingen,
Rolls two dice and prints a corresponding term,
Starter code is mine,
02/15/2026
"""
import random

while True:
    dice1 = random.randint(1,6) # Will roll two ints 1-6 every pass throught the while loop
    dice2 = random.randint(1,6)

    print(f"Dice 1: {dice1}") # Prints the individual and combined totals of the dice. Will repeat with every loop.
    print(f"Dice 2: {dice2}")
    print(f"Dice total: {dice1 + dice2}")
    
    if dice1 == 1 and dice2 == 1: # Multiple if statements searching for certain criterea. Will end with else statement if left unfufilled.
        print("Snake Eyes")
    elif dice1 == 1 and dice2 == 2 or dice1 == 2 and dice2 == 1:
        print("Ace Caught a Duece")
    elif dice1 == 2 and dice2 == 2:
        print("Little Joe from Kokomo")
    elif dice1 == 1 and dice2 == 4 or dice1 == 4 and dice2 == 1 or dice1 == 2 and dice2 == 3 or dice1 == 3 and dice2 == 2:
        print("Little Phoebe")
    elif dice1 == 3 and dice2 == 3:
        print("Jimmy Hicks from the Sticks")
    elif dice1 == 6 and dice2 == 1 or dice1 == 1 and dice2 == 6:
        print("Six Ace")
    elif dice1 == 4 and dice2 == 4:
        print("Eighter from Decatur")
    elif dice1 == 3 and dice2 == 6 or dice1 == 6 and dice2 == 3 or dice1 == 4 and dice2 == 5 or dice1 == 5 and dice2 == 4:
        print("Nina from Pasadena")
    elif dice1 == 5 and dice2 == 5:
        print("Puppy Paws")
    elif dice1 == 6 and dice2 == 5 or dice1 == 5 and dice2 == 6:
        print("Six Five no Jive")
    elif dice1 == 6 and dice2 == 6:
        print("Boxcars")
    else:
        print("Nothing Special")