'''higher0.py

   Jed Yang, 2016-11-10

   A gentle introduction to higher-order functions.

   You have used the accumulator pattern to process lists with loops.  Here we
   will see another way of doing these, using higher-order functions: functions
   that take other functions as inputs.
'''

################################################################################
### MAP: APPLY A FUNCTION TO EACH ELEMENT IN A LIST ### List of Cubes ##########

# Very frequently we want to apply a function to each item in a list.
# Here's an example using a for loop.
l = range(10)
ans = []
for item in l:
   ans.append(item ** 3)
print(ans)

# This task is so common that there is a function, called map, just for it.
l = range(10)
def cube(x):
   return x ** 3
ans = list(map(cube, l))
print(ans)

# Note that map() takes two arguments, the first of which is a function.

# Even though we are used to thinking of functions as represented by its name
# followed by (), e.g., cube(), note that we are passing cube, not cube(), to
# map.  Why?  [Hint: try
#print(cube)
# to see what cube is.]

print(cube)

print (map(cube, l))

# Why do I write 'list(' in front of 'map('?  What happens if I take that out?



################################################################################
### FILTER: SELECT A SUBLIST ACCORDING TO SOME CRITERION ### Even Numbers ######

# Another common task is to select the list items that satisfy some test.
# Here's an example using a for loop.
l = range(10)
ans = []
for item in l:
   if item % 2 == 0:
      ans.append(item)
print(ans)

# Here's how to do it with the filter function.
l = range(10)
def isEven(n):
   return n % 2 == 0
ans = list(filter(isEven, l))
print(ans)



################################################################################
### REDUCE: COMBINE ELEMENTS IN A LIST USING SOME OPERATION ### Sum of Ints ####

# A third common task is to combine list elements using some operation.
# Here's an example using a for loop.
l = range(10)
total = 0
for item in l:
   total = total + item
print(total)

# Here's how to do it with the reduce function.
l = range(10)
def summation(x, y):
   return x + y
import functools
total = functools.reduce(summation, l)
print(total)

# This calculates, in this order, (...(((0 + 1) + 2) + 3) + ... + 9).

# Remember these examples, we will continue to use them in the next part of the lab.
