import random


def user_input(die_side_count):
    # How many sides the die should have, from 1 to 100
    sides = range(1, 100)
    for _, side in enumerate(sides):
        if die_side_count == "4":
            print(_)
            print(type(_))
            print(die_side_count)
            print(type(die_side_count))
            print("Made it here")
            return int(die_side_count)
        else:
            print(_)
            print(type(_))
            print(die_side_count)
            print(type(die_side_count))
            print("Please enter a number from 1 to 100.")
            raise SystemExit(1)


def roll_dice(dice_count):
    # Rolls the die or dice
    roll_results = []
    for _ in range(dice_count):
        roll = random.randint(1, dice_count)
        roll_results.append(roll)
    return roll_results


# Ask how many of what side die to roll
num_rolls = input("How many rolls will you be wanting? ")
side_count = input("How many sides do you want to roll, from 1-100? ")
num_dice = user_input(num_rolls)
final_results = roll_dice(num_dice)

print(final_results)
