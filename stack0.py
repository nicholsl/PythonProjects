'''stack0.py

   Jed Yang, 2016-11-06

   A standard implementation of a stack data structure.
'''

class Stack:
   def __init__(self):
      '''Initialize a new empty stack.'''
      self.items = []

   def push(self, item):
      '''Add a new item to the stack.'''
      self.items.append(item)

   def pop(self):
      '''Remove and return from the stack the item that was last added.'''
      if self.isEmpty:
          print("that's empty!")
      else:
          return self.items.pop()

   def isEmpty(self):
      '''Check whether the stack is empty.'''
      return (self.items == [])


   def __str__(self):
      '''Return a string representation, for example when print() is called.'''
      return 'Stack: ' + str(self.items)

s = Stack()
s.push(23)
print(s)
# 1.  When an object is printed, Python looks for __str__() method to make the
#     object into a string.  What happens if I did not provide a __str__()
#     method?  Comment the code for __str__() above and see.

s.push(42)
print(s)

a = s.pop()
print(a)
print(s)

print(s.pop())
print(s.pop())
print(s.pop())



# 2.  What happens if you try to do s.pop() a few too many times in a row?
#     Can you modify pop() method to guard against this?
#     Hint: call self.isEmpty() first.
#s.pop()
#s.pop()
#s.pop()
#s.pop()
#s.pop()

# 3.  Actually, most implementations of Stack do not guard against pop() when
#     empty.  It is the user of Stack (i.e., you and me) who is responsible to
#     check before pop()'ing.  Now that you understand the basics of stacks,
#     download stack.py, which contains the same* Stack implementation, and
#     continue with stack1.py, stack2.py, etc.
#
#     * I removed the "Stack: " prefix in __str__().
