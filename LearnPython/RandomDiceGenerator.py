import random

cumulative_count = 0
dice_rolled = 0

options = [1, 2, 3, 4, 5, 6]


while True:

    input("Type r to roll a dice. ")

    random_number = random.randint(0, 5)
    dice_roll = int(options[random_number])

    cumulative_count += int(dice_roll)
    dice_rolled += 1

    print("\nYou rolled a", str(dice_roll) + ".")
    print("Cumulative count:", cumulative_count)
    print("Dice rolled: ", dice_rolled, "\n")
    print("---------------------------------------------------------------")