import sys

sys.setdefaultencoding('utf8')

def statelist():
    file = open('State list.txt')
    taco = []
    for line in file:
 #       line.decode('utf-8')
        ('['+line+']').append(taco)

statelist()
