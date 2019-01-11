'''stack1.py

   Jed Yang, 2016-11-06

   Reverse a list using stacks.
'''

from stack import Stack

s = Stack()
s.push(23)
print(s)

s.push(42)
print(s)

s.push(99)
print(s)

print('============')
t = Stack()
print('s:', s)
print('t:', t)
print()

t.push(s.pop())
print('s:', s)
print('t:', t)
print()

t.push(s.pop())
print('s:', s)
print('t:', t)
print()

t.push(s.pop())
print('s:', s)
print('t:', t)
print()

# Wow, the order has been reversed.  Use this idea to write a function that
# returns a list in reverse.  I've started it for you:

def reverseList(myList):
   '''Return a new list that contain myList elements in reverse.'''
   answer = []
   s = Stack()
   t = Stack() # do I really need a second stack?
   for item in myList:
      s.push(item)
   for item in myList:
      t.push(s.pop())
   # The items of myList have been pushed onto the stack.
   # To convince yourself, you can try
   print(s)
   print(t)
   # and see.  But now what?
   return answer

print(reverseList([1, 2, 3, 4]))
