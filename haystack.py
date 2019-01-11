haystack = 'abcdefg'
index = None
needle = 'c'
for char in range(len(haystack)):
	if char == needle:
		index = haystack[char]
		
print (index)