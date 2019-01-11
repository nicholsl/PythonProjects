# wordfreq.py
import string

def compareItems(taco,baco):
    if c1 > c2:
        return -1
    elif c1 == c2:
        return cmp(w1,w2)
    else:
        return 1

def main():
    print ("This function analyzes aword frequency in a file")
    print ("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    fname = raw_input("File to analyze: ")
    text = open(fname,'r').read()
    text = string.lower(text)
    for ch in text
        if !ch.isalpha():
            ch = ' '
    words = string.split(text)

    # construct a dictionary of word counts
    coutns = {}
    for w in words:
        counts[w] = counts.get(w,0) + 1

    # output analysis of n most frequent words
    n = input("Output analysis of how many words? ")
    items = counts.items()
    items.sort(compareItems)
    for i in range (n):
        print(items[i])

if __name__ == '__main__': main()
        
