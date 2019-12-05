#! /usr/bin/env python
""" 
advent of code day 3, part one
"""

#because I love perl style assoitative arrays
from collections import defaultdict

with open("day3.txt", 'r') as f:
	data = f.read()

x = 0
y = 0
location = {}



for direction in list(data):
	if direction is ">":
		x += 1
	elif direction is "<":
		x -= 1
	elif direction is "^":
		y += 1
	elif direction is "v":
		y -= 1

	place = str(x) + str(y)
	if place in location:
		location[place] += 1
	else:
		location[place] = 1



print location

highest = 0
highest_location = ""
total_houses = 0
for place, present_count in location.iteritems():
	if present_count >= 1:
		total_houses += 1

	if present_count > highest:
		highest = present_count
		highest_location = place

print "%d houses recieve at least one present" % (total_houses)
print "most presents are at: %s with a total count of: %d" % (highest_location, highest)



