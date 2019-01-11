'''strings5.py

   Jed Yang, 2016-10-25

   Here are some recursive tasks with strings.
'''

def printReverse(s):
   '''Recursively prints a string in reverse.'''
   if s == '':       # stop recursion from going infinitely deep
      print()
   else:
      printReverse(s[1:])
      print(s[0], end='')
        
printReverse('A man, a plan, a canal, Panama!')

def getReverse(s):
   '''Recursively reverses a string.'''
   if len(s) <= 1:   # strings of length 0 or 1 are their own reverse
      return s
   else:
      return s[-1] + getReverse(s[:-1])

print(getReverse('Not a palindrome.'))

# printReverse and getReverse are very similar.  Compare and contrast.  Can you
# change getReverse to use s[-1] and s[:-1] like printReverse?  [Hint: Yes, but
# you need to change something else, too.]  How about changing printReverse to
# use s[0] and s[1:] like getReverse?  [Hint: Again, yes, but it will be a bit
# problematic with formatting.  Don't worry about that for now and move on.  If
# you have time at the end, think about how to fix it.]

def getAnagrams(s):
   '''Recursively compute a list of anagrams of a string.  From Zelle 13.2.4'''
   if len(s) <= 1:       # What if we use len(s) <= 1 instead?  Why?
      return s     # Why put brackets around s?  What if we don't?
   else:
      ans = []
      for w in getAnagrams(s[1:]):
         for pos in range(len(w) + 1):
            ans.append(w[:pos] + s[0] + w[pos:])
      return ans

print(getAnagrams('Jed'))

# Extra Credit:
#   - Run getAnagrams('aab') to see an arguably incorrect behaviour.
#     Can you fix it?
#   - Can you implement getAnagrams without using recursion?
