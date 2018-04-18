for i in [0,1,2,3]:
	print i

for i in "Hello":
	print i

for i in (0,1,2,3):
	print i

x = {'2':'sup?','apple':6}

for i in x:
	print i
	print x[i]

# range(N) - list of 0 up to N
range(10)

# range(a,b) - list of values a up to b
range(1,15)

## if a > b, then it's an empty list
range(10,0)

# range(a,b,c) - list of values a up to b, but count by c
range(0,10,2)

## Will stop counting once values pass b
range(0,10,3)
range(0,10,99)

# Archetype for range w/ len
range ( len ( [0,1,2,'apple']) )

#while

#