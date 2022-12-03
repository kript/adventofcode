#!/usr/bin/python3
"""
Day 2 part one of the AOC
# Opponent: A for Rock, B for Paper, and C for Scissors
# Player: X for Rock, Y for Paper, and Z for Scissors
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
# If both players choose the same shape, the round instead ends in a draw.
# The score for a single round is the score for the shape you selected
#   (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
#   (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

TESTFILE = "day2.test"
REALFILE = "day2.input"


def scoreit(line):
    """
    calculate the score for the round
    """
    lookup_table = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    return lookup_table[line]


def strategy_guide(filename):
    """
    read in strategy guide
    """
    score = 0
    # Iterate over the lines of the file
    with open(filename, "rt", encoding="utf-8") as filetoread:
        for line in filetoread:
            # opponent, player = line.split()
            # print(line.rstrip())
            result = scoreit(line.rstrip())
            score = score + result
    return score

print("Test score: {}".format(strategy_guide(TESTFILE)))
print("Real score: {}".format(strategy_guide(REALFILE)))
