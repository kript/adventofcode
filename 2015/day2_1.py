#/usr/bin/python

fname = "day2.txt"

with open(fname) as f:
    content = f.readlines()

total = 0
surface_area = 0

for line in content:
	l, w, h = line.split("x")
	length = int(l)
	width = int(w)
	height = int(h)
	
	side_one = ( (int(length) * int(width) ) )
	side_two = ( (int(width) * int(height) ) ) 
	side_three = ( (int(height) * int(length) ) )

	square_one = ( 2 * side_one)
	square_two = ( 2 * side_two)
	square_three = ( 2 * side_three)

	array = (side_one, side_two, side_three)
	smallest_side = sorted(array)[0]
	square_array = ( 
		square_one,
		square_two,
		square_three,
		)
		
	subtotal = ( sum(square_array) + smallest_side )
	print subtotal
	total += subtotal
	

print "total square feet of wrapping paper is %d" % (total)