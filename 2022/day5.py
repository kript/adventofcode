#!/usr/bin/python3
"""
Day 5 of the AOC

which crate will end up on top of each stack; in this example, 
the top crates are C in stack 1, M in stack 2, and Z in stack 3, 
so you should combine these together and give the Elves the message CMZ.

part one:
After the rearrangement procedure completes, what crate ends up on top of each stack?

```
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
```
part two:


"""


#FILES = ["day5.test", "day5.input"]
FILES = ["day5.test"]

def parser(filename):
    """
    read in assignment
    """
    duplicate_count = 0
    overlap_count = 0
    # Iterate over the lines of the file
    with open(filename, "rt", encoding="utf-8") as filetoread:
        for line in filetoread:
            # if it has a [] its a crate
            # if it has a ' [0..9]'  its a stack - is this true? check! 
            # if it starts with 'move' its an instruction           

    return duplicate_count, overlap_count

def stacks():
    parser(filename)

for answerfile in FILES:
    answers = stacks(answerfile)
    print("{} duplicate count: {} overlap: {}".format(answerfile,answers[0],answers[1]))
