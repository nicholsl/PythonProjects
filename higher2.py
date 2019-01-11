'''higher2.py

   Jed Yang, 2016-11-10

   You may have seen in some math classes the frequent need of summing
      f(1) + f(2) + ... + f(n),
   where f is some function.  For example, I may want to calculate sum of
   cubes, in which case I will let
      f(x) = x^3.
   Let's see a few different ways of doing this.
'''
import functools

N = 9

################################################################################

way = 'Way 1. Accumulator pattern:'

def sumOfCubes1(n):
   '''Return sum of 1^3 + 2^3 + ... + n^3.'''
   total = 0
   for i in range(n+1):
      total = total + i ** 3
   return total

print(way, sumOfCubes1(N))

################################################################################

way = 'Way 2. Combine two examples from higher0.py:'

# Implement the following using ideas from higher0.py.
def sumOfCubes2(n):
   listOfCubes = list(map('???'))
   total = functools.reduce('???')

#print(way, sumOfCubes2(N))

################################################################################

way = 'Way 3a. Use a summation() higher-order function:'

def summation(start, end, f):
   '''Return f(start) + f(start+1) + f(start+2) + ... + f(end).'''
   total = 0
   for i in range(start, end+1):
      total = total + f(i)
      # See how intuitive the notation is?  We literally just write f(i).
   return total

def cube(x):
   return x ** 3

print(way, summation(1, N, cube))

################################################################################

way = 'Way 3b. Use lambda to avoid defining cube():'
print(way, summation(1, N, lambda x: x ** 3))

################################################################################

way = 'Way 4. Use a one-line summation() implementation:'
def summation2(start, end, f):
   return functools.reduce(lambda x, y: x + y, map(f, range(start, end+1)))

print(way, summation2(1, N, cube))

################################################################################

way = 'Way 5. Use two lambdas to sum in one line, without using anything else:'
print(way,
   functools.reduce(lambda x, y: x + y, map(lambda x: x ** 3, range(N+1))))
