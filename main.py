# I miss C-style syntax and idioms

import random


def user_input(die_sides):
    # How many sides the die should have, from 1 to 6
    # Would rather user be able to select 1-100 for sides, and input be validated as such.
    if die_sides.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(die_sides)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)


def roll_dice(die_count):
    # Rolls the die or dice
    roll_output = []
    for _ in range(die_count):
        roll = random.randint(1, die_count)
        roll_output.append(roll)
    return roll_output


# Ask how many of what side die to roll
num_rolls = input("How many rolls will you be wanting? ")
dice_count = user_input(num_rolls)
roll_results = roll_dice(dice_count)

print(roll_results)
