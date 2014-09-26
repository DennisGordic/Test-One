# Craps Roller
# Demonstrates random number generation
# Original Author: Michael Dawson
# Last Edited: Dennis Gordick
# Date Edited: 9/26/2014

import random

# generate random numbers 1 - 6
die1 = random.randint(1, 6) 
die2 = random.randrange(1, 6)

total = int(die1) + int(die2)

print("You rolled a", die1, "and a", die2, "for a total of", total)

input("Press the enter key to exit.")
