""" Dice simulator """

import random

print("This is a dice stimulator")
X = "y"
while X == "y":
    NUMBER = random.randint(1, 6)

    if NUMBER == 1:
        print("===========")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("===========")

    if NUMBER == 2:
        print("===========")
        print("|         |")
        print("| O     O |")
        print("|         |")
        print("===========")

    if NUMBER == 3:
        print("===========")
        print("|    O    |")
        print("|    O    |")
        print("|    O    |")
        print("===========")

    if NUMBER == 4:
        print("===========")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("===========")

    if NUMBER == 5:
        print("===========")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("===========")

    if NUMBER == 6:
        print("===========")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("===========")

    X = input("Press y to roll again ")
