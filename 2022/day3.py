#!/usr/bin/python3
"""
Day 3 of the AOC
The list of items for each rucksack is given as characters all on a single line.
A given rucksack always has the same number of items in each of its two compartments,
so the first half of the characters represent items in the first compartment,
while the second half of the characters represent items in the second compartment.

every item type can be converted to a priority

Find the item type that appears in both compartments of each rucksack.
What is the sum of the priorities of those item types?
"""

TESTFILE = "day3.test"
REALFILE = "day3.input"


def priority(item):
    """
    find the priority of the item

    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    Thanks to
        https://stackoverflow.com/a/4319407 (just learned this!)
        https://stackoverflow.com/a/12935035 (forgot this!)
    """
    if item.islower():
        score = ord(item) - ord("a") + 1
    else:
        score = ord(item) - ord("A") + 27
    return score


def intersection(compartment_one, compartment_two):
    """
    Calculate the intersection of the two sets
    Thanks to
        https://www.geeksforgeeks.org/python-intersection-two-lists/
        https://betterprogramming.pub/a-visual-guide-to-set-comparisons-in-python-6ab7edb9ec41

    This has a gotcha - if there is more than one item in the union,
     this function will only return the first one.
    """
    return list(set(compartment_one).intersection(compartment_two))[0]


def contents(filename):
    """
    read in backpack contents
    """
    score = 0
    # Iterate over the lines of the file
    with open(filename, "rt", encoding="utf-8") as filetoread:
        for line in filetoread:
            # split line in half to find each compartment
            halfway = int(len(line.rstrip()) / 2)
            # print(halfway)
            compartment_one = line.rstrip()[:halfway]
            compartment_two = line.rstrip()[halfway:]
            # Find the item type that appears in both compartments of each rucksack.
            item = intersection(compartment_one, compartment_two)
            # with the item that is in both compartments, calculate its pirority
            backpack_score = priority(item)
            # print(backpack_score)
            score = score + backpack_score
    return score


print("Test score: {}".format(contents(TESTFILE)))
print("Real score: {}".format(contents(REALFILE)))
