# These tools are simple, direct conersions to other datatypes

# Numerical Conversions
## Must use 

# Play with Int
y_int = 1
y_float = 1.0
y_int_str = '1'
y_float_str = '1.0'
y_list = [1,2]
y_tuple = (1,2)
y_dict = {1:2}

# Converst to Int
print int(y_float)
# Converts to float
print int(y_int_str)
print int(y_float_str)
## Argument must be string or Number
# These will return TypeError
# print int(y_list)
# print int(y_tuple)
# print int(y_dict)

# Converts to float
print float(y_int)
# print float(y_float)
## y_float is already a float
print float(y_int_str)
print float(y_float_str)

## Argument be string or Number
# These will return TypeError
# print float(y_list)
# print float(y_tuple)
# print float(y_dict)

###
# Converts to String
print str(y_int)
print str(y_float)
print str(y_int_str)
print str(y_float_str)
print str(y_list)
print str(y_tuple)
print str(y_dict)


# Cannot convert List

## TypeError - Must use Iterables
# print list(y_int)
# print list(y_float)

print list(y_int_str)
print list(y_float_str)
print list(y_list)
print list(y_tuple)
print list(y_dict)

# Convert to Tuple

## TypeError - Must use Iterables
# print tuple(y_int)
# print tuple(y_float)

print tuple(y_int_str)
print tuple(y_float_str)
print tuple(y_list)
print tuple(y_tuple)
print tuple(y_dict)


# Converts to Dictionary
## Will need key-value
## Will make left expression into string key
## Will make right expression into value
x = dict(example=1)
z = dict(one=1,two=2,three=3)
print x
print type(x)

print z
print type(z)