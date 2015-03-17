# python is pass-by-ref
a = [1, 2, 3]
b = a
b.append(4)
print a

a = 5
b = 2.0
print a/b, a//b  #this will print 2.5 2

print isinstance(b//1, int)


# Duck typing

# Imports

a = [1, 2, 3]
b = a
c = list(a)  # list(), This will always create a new list
print a is b, a is not c  # True True

a = 2
b = 3
a ** b  # raise a to power of b
a & b  # bitwise and
a and True # && || corresponds to and or


# Data structure

# List is mutable, tuple is not

# complex value
a = 1 + 2j

a = 'python'; a = list(a)  # will convert a to a list of character
a[0] = 'C'             # otherwise couldn't do this

a = 'python'; a[2]; a[:3]

# raw string, take as is
a = r'this\has\no\special\characters'


a = 'first'; b = ' second'
print a + b   # this will piece together the two parts


# Type casting
a = '3.14159'
b = float(a)
b = int(b)


# Dates and times
from datetime import datetime, date, time


# flow control
x = 4
if x > 0:
    print "It's negative"
elif x == 0:
    print "Equal to zero"
else:
    print "Positive"


collection = range(5)
for value in collection:
    # do something
    if value == 4:
        break
    pass

# when doing large number iteration, instead of use range(), use xrange()

a = 2.3
b = 'Non-negative' if a>= 0 else 'Negative'

# Data structure
tup = 3, 4, 5   # immutable
# tuple and list and string can be converted to each other

a = list('abcdefg')
''.join(a)    # this will convert a list to string

# the use of + and * for list, tuple, and string

# for tuple, .count()

# for list, sort, insert, pop, remove...

# slicing
a = range(1,10)
a[1:4]; a[:4]; a[-3]; a[-3:]; a[:-2]

# enumerate
for i, value in enumerate(a):
# i is index, value is the element
    pass


# built-in function
sorted(list('2016169037'))
sorted(set('2016169037'))   # set is also a structure

# dict
d = {'a':'some value', 'b':[1,2,3]}
d['a']
d[4] = 342
'b' in d
del d[4]

# dict.pop,
d.get('a', 'a default value')  # a convenience function


