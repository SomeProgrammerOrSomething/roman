def answer(choice):
	choosey = raw_input("What is your pill count? Choose wisely... ")
	choosey = int(choosey)

	if choosey == 1:
		print "Your too low"
	elif choosey == 2:
		print "mid"
	elif choosey == 3:
		print "your on 3"

	else:
		print "Pick one two or three"
		answer(None)

answer(None)