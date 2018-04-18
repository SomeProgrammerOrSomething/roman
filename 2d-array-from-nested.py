x = range(3)
# List

y = []
z = []
# Empty List

for item in x:
	y.append( [x[item]] )
# Appends each element of x as a list
print y
print "\n"

for item in x:
	z.append( x )

print z