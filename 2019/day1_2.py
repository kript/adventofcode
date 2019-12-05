#!/usr/bin/python

lines = [line.rstrip('\n') for line in open('day1.input')]

mass_fuel = 0

def recursive_fuel(f, total_fuel=0):
	new_fuel = f
	while True:
		new_fuel = (int(new_fuel) // 3) - 2
		if new_fuel > 0:
			total_fuel += new_fuel
		else:
			break
	return(total_fuel)

for line in lines:
	print(f'mass: {line}')
	rounded = int(line) // 3 # round down
	final = rounded - 2
	print(f'rounded and minus 2: {final}')
	final_plus = recursive_fuel(final)
	print(f'fuel plus its own fuel: {final_plus}')
	mass_fuel += final_plus
	print(f'current fuel required: {mass_fuel}')

