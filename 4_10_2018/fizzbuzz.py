# Version of Fizz Buzz
daNumba = int( raw_input("Pick a number, any number: ") )



def fizzbuzz(divisor):
	if (divisor %3 == 0) and (divisor % 5 == 0):
		print "fizzbuzz"
	elif (divisor % 5 == 0 ):
		print "fizz"
	elif (divisor %3 == 0):
		print "buzz"
	else:
		print "you ain't fizzin or buzzin cuzzin"

while ( daNumba > 0):
	fizzbuzz(daNumba)
	daNumba-=1