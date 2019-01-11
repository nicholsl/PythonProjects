''' arithmetic.py

   Jed Yang, 2016-09-13

   Adapted to Python 3 from a program written by Jeff Ondich, 9/11/09

1. Run this program several times with a variety of input values.
Try to predict each time what output the program will produce.

Questions:
-- What does "print" alone on a line do?)
-- What does the operator "/" do?
-- What does the operator "%" do?  (Think about quotients
    and remainders.)
-- What does the operator "**" do?
-- What happens if you enter text that isn't an integer?
   (e.g. "tofu" or "123.456")
-- What does "type(a)" do?

2. In the two places where it says "int(numberText)", change
"int" to "float" (and change "Integer, please" to "Number, please"
while you're at it).  For historical reasons that I'll explain in
class, the term "float" is often used in computer programming when
"real" (as in "real numbers") would be better.

3. Run the modified program again, this time providing a
non-integer for the first prompt.  What happens now?

4. At the bottom of the program, note that we seem to be turning
a string into a real number.  Any ideas why we would use the word
"float" for this purpose?  (No?  Come to class Monday and I'll tell
you all about it.)  In any case, remember how this is done--you may
need it in your homework.
'''

numberText = input('Integer, please: ')
a = int(numberText)

numberText = input('Another integer, please: ')
b = int(numberText)

print()
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '/', b, '=', a / b)
print(a, '%', b, '=', a % b)
print(a, '**', b, '=', a ** b)
print()
print('The type of', a, 'is', type(a))
print('The type of', b, 'is', type(b))

print()
print('============')
print()

numberText = input('Please enter a number with or without a decimal point: ')
x = float(numberText)

print('The square of your number is:', x * x)
print()