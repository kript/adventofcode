#!/usr/bin/python

lines = [line.rstrip('\n') for line in open('day1.input')]

mass_fuel = 0

for line in lines:
	print(f'mass: {line}')
	rounded = int(line) // 3 # round down
	final = rounded - 2
	print(f'rounded and minus 2: {final}')
	mass_fuel += final
	print(f'current fuel required: {mass_fuel}')

