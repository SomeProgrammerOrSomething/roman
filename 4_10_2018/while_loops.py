# While Loops Check Conditions - Usually Uses Booleans
# For Loops are for Iteration

# For Loop Example
for index in range(5):
	print "Hello, it's", index

# Clean Up
print "\n"

# While Loop - Conditions Built into check:
index = 0
while index <= 4:
	print index
	index += 1

# Clean Up
print "\n"

# If & Break - While Loop Example:
index = 0
while True:
	print index
	index += 1
	if index >= 4:
		break

# For Loops w/ Continue
for index in range(5):
	if index == 3:
		#continue
		pass
	print "Hello, it's",index,"again!"


# Menu
while True:
	# Text
	# Text
	# Text
	# if condition
		# break