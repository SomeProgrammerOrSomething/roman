# Functions Real Fast

#def function_name(parameters):
#	[Function Operations]
#	return [None Or Values]

def simple_print(text):
	# This function prints text
	print "text"
	return


simple_print('Hello. This is text')

def reverse(iterable):
	backwards = []

	for i in range(len(iterable)):
		backwards += iterable[len(iterable) - i - 1 ]

	print backwards

reverse('Hello, World')