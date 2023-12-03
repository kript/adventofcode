#!/usr/bin/python3
"""
Day 4 of the AOC

Some of the pairs have noticed that one of their assignments fully contains the other. 
For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. 
In pairs where one assignment fully contains the other, one Elf in the pair would be 
exclusively cleaning sections their partner will already be cleaning, so these seem 
like the most in need of reconsideration. In this example, there are 2 such pairs.

2-4,6-8

part two:

In how many assignment pairs do the ranges overlap?

2000 too high
"""


FILES = ["day4.test", "day4.input"]
#FILES = ["day4.test"]

def assignments(filename):
    """
    read in assignments
    """
    duplicate_count = 0
    overlap_count = 0
    # Iterate over the lines of the file
    with open(filename, "rt", encoding="utf-8") as filetoread:
        for line in filetoread:
            # split line in half to find each compartment
            # create an array starting and stopping with the numbers
            elf1 = line.rstrip().split(",")[0].split("-")
            elf2 = line.rstrip().split(",")[1].split("-")
            elf1_assignment = []
#            for increment in range(int(elf1[0]),int(elf1[1]) + 1):
#                elf1_assignment.append(increment)
            elf2_assignment = []
#            for increment in range(int(elf2[0]),int(elf2[1]) + 1):
#                elf2_assignment.append(increment)
            elf1_assignment
            print("elf1: {} elf2: {} ".format(elf1_assignment,elf2_assignment))

            # stole this from https://www.reddit.com/r/adventofcode/comments/zcokrb/2022_day_4_part_1_python_number_of_overlaps_works/
            elf1_assignment
            print("elf1: {} elf2: {} ".format(elf1_assignment,elf2_assignment))

            if(int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])):
                duplicate_count = duplicate_count + 1
                print("duplicate found, count is: {}".format(duplicate_count))
            # check if elf 2's range contains elf 1's range
            elif(int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])):
                duplicate_count = duplicate_count + 1
                print("duplicate found, count is: {}".format(duplicate_count))

            if all([item in elf2_assignment for item in elf1_assignment ]):
                overlap_count += 1
                print("overlap found, count is: {}".format(overlap_count))
                if all([item in elf1_assignment for item in elf2_assignment ]):
                    overlap_count += 1
                    print("overlap found, count is: {}".format(overlap_count))
                # check if elf 1's range contains elf 2's range

    return duplicate_count, overlap_count


for answerfile in FILES:
    answers = assignments(answerfile)
    print("{} duplicate count: {} overlap: {}".format(answerfile,answers[0],answers[1]))
