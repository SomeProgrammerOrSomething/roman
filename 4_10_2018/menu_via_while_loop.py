while True:
	# Choice Collection
	choice = int(raw_input( "1 Thing\n2 Thing\n3 Thing\n0 Exit\n\n>>" ))

	if choice not in range(4):
		continue


	if choice == 1:
		print "Thing 1"
	elif choice == 2:
		print "Thing 2"
	elif choice == 3:
		print "Thing 3"

	# Terminate Operations - Must hold value 0 at this point
	else:
		quit()

	# Only Gets to this point of the loop if the value is in rnage(4)
	break
