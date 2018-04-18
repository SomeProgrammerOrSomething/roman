# Nested Stuff
array_outer = range(5)
# This is a List - Cannot be used as Index
# value is [0,1,2,3,4]
# It IS a list of INT's, which can be used as indices
# We want to references those ELEMENTS for indices

for i in array_outer:
	# So on first iteration, the value is array_outer[0] = 0
	# Second will be array_outer[1] = 1
	# And so on up until array_outer[4] = 4
	## Each of these are ints, so we can use these for indices

	for j in array_outer:
		# j references each element in the array
		# so j will take on the value of int's
		# so j can be printed as an int OR can be used as an index

		print j
		# Here we just print j, so we get printed strings of ints



#Consider a matrix...as a 2D Array

# R1C1  R1C2  R1C3
# R2C1  R2C2  R2C3
# R3C1  R3C2  R3C3

#We could build this item with nested lists
#[ [R1C1,R1C2,R1C3], [R2C1,R2C2,R2C3], [R3C1,R3C2,R3C3]]
sample = [ ['r1c1', 'r1c2', 'r1c3'], ['r2c1','r2c2','r2c3'], ['r3c1','r3c2','r3c3'] ]

# Notice what the index references
for item in sample:
	print sample[item]




