'''stack.py

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
      return self.items.pop()

   def isEmpty(self):
      '''Check whether the stack is empty.'''
      return (self.items == [])

   def __str__(self):
      '''Return a string representation, for example when print() is called.'''
      return str(self.items)
