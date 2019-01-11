'''factorial.py

   Jed Yang, 2016-10-20

   The factorial of a nonnegative number n, often writen as n!, is defined to
   be n * (n-1) * (n-2) * ... * 2 * 1.  We also define, 0! = 1, but do not
   define (for now) the factorial of negative or non-integer numbers.

   Below there are two implementations of factorial, one iterative and one
   recursive.  Read and make sure you understand the code.  Then answer other
   questions below or play with the code more.
'''

import sys

def factorial_iterative(n):
   product = 1
   for i in range(2,n+1):
      product = product * i
   return product

def factorial_recursive(n):
   if n <= 1:
      return 1
   else:
      return n * factorial_recursive(n-1)

def main():
   for i in range(10):
      print('The factorial of {0} is {1}.'.format(i, factorial_iterative(i)))

   for i in range(10):
      print('The factorial of {0} is {1}.'.format(i, factorial_recursive(i)))

# 1. Make sure you understand the iterative AND the recursive procedure.  Why
#    do they give the same answer?

#    Comment out the main().  Go below.
#main()

def large(largeNumber):
   print('Iterative:')
   print(factorial_iterative(largeNumber))
   sys.setrecursionlimit(largeNumber+7)
   print('Recursive:')
   print(factorial_recursive(largeNumber))

# 2. Uncomment the large(100) and see if the we can handle large numbers.

large(2000)

# 3. Try bigger large numbers in a systematic way to observe the behaviour of
#    the functions and find a breaking point where things no longer works.
#    Does the iterative or the recursive one stop working first?  Why?

# 4. What if you uncomment the sys.setrecursionlimit() line above?

# 5. Continue with Question 3.
