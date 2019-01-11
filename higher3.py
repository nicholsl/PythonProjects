'''higher3.py

   Jed Yang, 2016-11-10

   So far, we have used functions as *arguments* to other (higher-order)
   functions.  We can also use functions as *return values*.
'''

def powerOfFactory(n):
   '''Input: an integer n
      Return: one-parameter function f, with the following properties:
      -  Input: an integer x.
      -  Return: n^x (n raised to the x-th power).
   '''
   # We define a new function here, crazy, eh?
   def myNewFunc(x):
      return n ** x
   # And return this function:
   return myNewFunc

# Suppose I am interested in calculating powers of 2.  I can do this:

powerOf2 = powerOfFactory(2)

print(powerOf2(8))
print()

for i in range(10):
   print(powerOf2(i))
print()

# I can also use the 'map' idea to apply 'powerOf2' to a range of numbers.
print(list(map(powerOf2, range(10))))
print()

# Perhaps now I want to try other powers.
print(list(map(powerOfFactory(3), range(10))))
print(list(map(powerOfFactory(4), range(10))))
print(list(map(powerOfFactory(5), range(10))))
print()
# See how convenient that is?  I have a function that is like a factory,
# cranking out all sorts of functions.

# Implement the following function.  It is possible to write it in one line if
# you use the lambda keyword.  Otherwise, perhaps three or four lines.
def isDivisibleBy(n):
   def f(m):
      return m % n == 0
   return f
   '''Input: an integer n
      Return: one-parameter function f, with the following properties:
      -  Input: an integer m.
      -  Return: a Boolean indicating whether m is divisible by n.
   '''
   pass

def test():
   isDivisibleBy7 = isDivisibleBy(7)
   print('should be True:', isDivisibleBy7(14))
   print('should be False:', isDivisibleBy7(15))
   print('should be True:', isDivisibleBy(9)(18))
   print('should be \n[True, False, False, True, False, False, True, False, False, True]:')
   print(list(map(isDivisibleBy(3), range(10))))

test()

# Conceptually, we turned a two-parameter function f(x, y) into a one-parameter
# function g(x) that returns a function so g(x)(y) gives the same result as
# f(x, y).  This transformation is known as currying.

# We can make a higher-order function do currying for us, like so:

def curry(f):
   '''Input: two-parameter function f
      Return: one-parameter function g, with the following properties:
      -  Input: x
      -  Return: one-parameter function h, with the following properties:
         -  Input: y
         -  Return: f(x, y)
   '''
   def g(x):
      def h(y):
         return f(x, y)
      return h
   return g

# Since curry() is a function that takes a function and returns a higher-order
# function (which returns a function), one might say curry() is a higher-order
# higher-order function?

powerOf = curry(lambda x, y: x ** y)
print( powerOf(2)(5) )

# We can also go in the reverse direction.

def uncurry(g):
   '''Input: one-parameter function g that returns a one-parameter function
      Return: two-parameter function f, with the following properties:
      -  Input: x, y
      -  Return: g(x)(y)
   '''
   def f(x, y):
      return g(x)(y)
   return f

original = uncurry(powerOf)
print( original(2, 5) )

# Extra Credit: Use lambda to implement curry() and uncurry() in one line each.
