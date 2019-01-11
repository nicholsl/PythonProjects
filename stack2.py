'''stack2.py

   Jed Yang, 2016-11-06

   Check for balanced brackets using stacks.
'''

from stack import Stack

goodExpr = '((1+2)*3+(4*5)+6-7)*(8*9)'
badExpr1 = '(((1+2)*3'
badExpr2 = '(1))'
badExpr3 = '(1))((2)'
# - goodExpr has balanced parentheses.  It has the same number of ( as ).
# - badExpr1 has too few closing )
# - badExpr2 has too many closing )
# But just because ( and ) appear the same number of times, the expression
# might still not be correct.
# - badExpr3 has three of ( and ) each, but too many ) early on.
#
# We can use a stack to keep track of the ones we've seen:

def balancedParen(expr):
   '''Check whether an expression has balanced parentheses.'''
   s = Stack()
   for ch in expr:
      if ch == '(':
         s.push(ch)
      elif ch == ')':
         if s.isEmpty():
            print('Too many ) encountered so far.')
            return False
         else:
            s.pop()
   if s.isEmpty():
      return True
   else:
      print('Too few ) overall.')
      return False

balancedParen(goodExpr)

balancedParen(badExpr1)

balancedParen(badExpr2)

balancedParen(badExpr3)

# Try using balancedParen(...) to test goodExpr, badExpr1, 2, and 3 to make sure it works.

# Ok, was a stack necessary?  It seems like we are just pushing and popping '('
# to see how many we have at any time.  I can totally do this without a stack,
# right?

# Compare the following with the code above, test it, make sure it works.

def balancedParenWithoutStack(expr):
   '''Check whether an expression has balanced parentheses;
      no need for stacks!
   '''
   openParenCount = 0
   for ch in expr:
      if ch == '(':
         openParenCount = openParenCount + 1
      elif ch == ')':
         if openParenCount == 0:
            print('Too many ) encountered so far.')
            return False
         else:
            openParenCount = openParenCount - 1
   if openParenCount == 0:
      return True
   else:
      print('Too few ) overall.')
      return False

# So what's the point of using stacks?  Well... what about these expressions?

goodExpr2 = '{[()]}'
goodExpr3 = '{[(1+2)*3+(4*5)+6-7]*(8*9)}'
badExpr4 = '[(])'

# The good ones are *properly nested* but badExpr4 is not.  Indeed, even though
# ( and ) are fine and [ and ] are fine, they come in the wrong order.  I am
# not sure how to modify balancedParenWithoutStack() to test for this--tracking
# the counts of each type of brackets encountered so far would not be enough.
# But if we push them onto a stack, we can make sure brackets are matching.

# Below is the code of balancedParen().  I've edited the 4th line so it pushes
# no only ( but also [ and { onto the stack.  Continue the edits to test
# whether the closing brackets ), ], and } come in the correct order.

def balancedBracket(expr):
   '''Check whether an expression has balanced parentheses.'''
   s = Stack()
   for ch in expr:
      if ch == '(' or ch == '[' or ch == '{': # pushes all three types
         s.push(ch)
      elif ch == ')':
         if s.isEmpty():
            print('Too many ) encountered so far.')
            return False
         else:
            s.pop()
   if s.isEmpty():
      return True
   else:
      print('Too few ) overall.')
      return False
