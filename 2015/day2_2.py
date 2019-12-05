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

	array = (length, width, height)
	smallest_dimensions = sorted(array)[0:2]
	
		
	subtotal = ( smallest_dimensions[0] + 
		smallest_dimensions[0] +
		smallest_dimensions[1] +
		smallest_dimensions[1]
		)
	bow = (length * height * width)
	print subtotal
	print bow
	total += subtotal + bow
	

print "total  feet of ribbon is %d" % (total)