'''fibonacci.py

   Jed Yang, 2016-10-20

   The n-th Fibonacci number for a nonnegative number n, writen here as fib(n),
   is defined *recursively* as follows:
      fib(0) = 0
      fib(1) = 1
      fib(n) = fib(n-1) + fib(n-2)        if n >= 2
   Note that we had previously defined fib(2) = 1 and did not define fib(0).

   0.  Convince yourself that these two definitions yield the same fib(n).

   Below there are two implementations of fibonacci, one iterative and one
   recursive.  Read and make sure you understand the code.  Then answer other
   questions below or play with the code more.
'''

def fibonacci_iterative(n):
   if n <= 1:
      return n
   prev, cur = 0, 1
   for i in range(2,n+1):
      prev, cur = cur, prev + cur
   return cur

def fibonacci_recursive(n):
   print('Hi, fibonacci_recursive({0}) has been called.'.format(n))

   # The following line allows you to do Question 4 below.  For now, please
   # ignore it.
   fibonacci_recursive.totalCalls = fibonacci_recursive.totalCalls + 1

   if n <= 1:
      return n
   else:
      return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Ignore this line as well.
fibonacci_recursive.totalCalls = 0

def main():
   for i in range(10):
      print('fib({0}) is {1}.'.format(i, fibonacci_iterative(i)))

   for i in range(10):
      print('fib({0}) is {1}.'.format(i, fibonacci_recursive(i)))

# 1. Make sure you understand the iterative AND the recursive procedure.  Why
#    do they give the same answer?

#    Comment out the main().  Go below.
#main()

def large(largeNumber):
   print('Iterative:')
   print(fibonacci_iterative(largeNumber))
   print('Recursive:')
   print(fibonacci_recursive(largeNumber))

# 2. Uncomment the large(100) and see if the we can handle large numbers.

large(30)

# 3. Why is the breaking behaviour of fibonacci_recursive different from the
#    breaking behaviour of factorial_recursive?  In particular, Python is not
#    quickly throwing a RuntimeError of reaching the recursion depth.  If that
#    is not the problem, what is?  Hint: consider using that commented out
#    print() in fibonacci_recursive to help see what is going on.

#    After you sort of understand what's going on, comment out the large(...)
#    that's not working and move on.

# 4. In fibonacci_recursive, there is a mysterious line that I asked you to
#    ignore earlier.  It says:
#
#       fibonacci_recursive.totalCalls = fibonacci_recursive.totalCalls + 1
#
#    You do not need to fully understand why it works, but I want you to know
#    what it does:
#
#    Roughly speaking, we are giving the function fibonacci_recursive an
#    attribute called totalCalls.  It persists between function calls, as if by
#    magic.  The point is that each time we call fibonacci_recursive, we
#    increment by 1 the "totalCalls" variable that's associated with this
#    function.  This allows us to count the number of times fibonacci_recursive
#    is called.
#
#    Uncomment the countCalls() below.
#
#    Can you see a pattern in the number of calls?

def countCalls():
   for i in range(10):
      # set totalCalls to 0 for each loop
      fibonacci_recursive.totalCalls = 0
      # print out the number of calls to fibonacci_recursive it took us to
      # calculate fib(i)
      print('fib({0}) is {1}; totalCalls = {2}'
         .format(i, fibonacci_recursive(i), fibonacci_recursive.totalCalls))

#countCalls()

# 5. Hopefully by now you are convinced that, for factorial, iterative and
#    recursive are both more or less okay, but for fibonacci, iterative is
#    much, much more efficient than recursive.  Can you think of any benefits
#    of recursion over iteration for calculating fibonacci?
