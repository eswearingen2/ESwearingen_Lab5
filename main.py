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