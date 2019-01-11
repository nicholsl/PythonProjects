'''higher1.py

   Jed Yang, 2016-11-10

   We have seen how to use map, filter, and functools.reduce to process lists.
   But these methods do not seem to save a lot of coding, if we have to write a
   helper function each time to use them.  There must be a better way.
'''

# Here is the sum-of-ints example using 'reduce' from higher0.py.
l = range(10)
def summation(x, y):
   return x + y
import functools
total = functools.reduce(summation, l)
print(total)

# Do we really have to write our own addition function?  Python obviously has
# addition, but neither of these lines works.
# functools.reduce(+, range(10))
# functools.reduce('+', range(10))

# Comment the above lines out (since they don't work).

# The function you want is add, in the operator module.
import operator
print( functools.reduce(operator.add, range(10)) )

# You may not know about operator.add.  Also, in general, Python might not have
# a built-in function for your task.  You can use the 'lambda' keyword to make a
# function right when you need it, without giving it a name!
#
#     lambda arg1, arg2, ..., argN: return value calculated from arg1...argN
#
# Here is the reduce example using the lambda keyword.

print( functools.reduce(lambda x, y: x + y, range(10)) )
#                       ^^^^^^^^^^^^^^^^^^ this represent a function that takes
#                                        two inputs, x and y, and returns x + y.

# Write the lambda expression for the even-numbers filter example from
# higher0.py.  I've started it for you.  You just need to change the ??????.

#print( list(filter(lambda n: ???????, range(10))) )

print( list (filter(lambda n: n % 2 == 0, range(10))))

# Adapt our list-of-cubes map example from higher0.py using lambda, in one line.
# I didn't quite start it for you this time.

print( list (map(lambda x: x**3, range(10))))
