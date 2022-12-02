#!/usr/bin/python3
"""
Day 1 part one of the AOC
"""

testfile = 'day1.test'
realfile = 'day1.input'

def team_calories(filename):
    """
    calculate the calories for the expedition
    """
    counter = 0
    inventory = [{'total': 0, 'items': [] }]
    # Iterate over the lines of the file
    with open(filename, 'rt') as f:
        for line in f:
            if (not line.rstrip()):
                counter += 1
                inventory.append({'total': 0, 'items':[]})
            else:
                inventory[counter]['items'].append(int(line.rstrip()))
                inventory[counter]['total'] = sum(inventory[counter]['items'])
    return(inventory)

def elf_most_calories(inventory):
    calorie_count = []
    for elf in inventory:
        calorie_count.append(elf['total'])
        print(calorie_count)
    return([max(calorie_count), calorie_count])

def calories(inventory):
    calorie_count = []
    for elf in inventory:
        calorie_count.append(elf['total'])
    return(calorie_count)

def top_three(supplies_per_elf):
    return(sum(sorted(supplies_per_elf, reverse=True)[:3]))

expedition = team_calories(testfile)
supplies_per_elf = calories(expedition)
print("Max test calories: {}".format(max(supplies_per_elf)))
print("top three calorie elves: {}".format(sorted(supplies_per_elf, reverse=True)[:3]))
print("top three totalled: {}".format(top_three(supplies_per_elf)))

expedition = team_calories(realfile)
supplies_per_elf = calories(expedition)
print("Max real calories: {}".format(max(supplies_per_elf)))
print("top three calorie elves: {}".format(sorted(supplies_per_elf, reverse=True)[:3]))
print("top three totalled: {}".format(top_three(supplies_per_elf)))
