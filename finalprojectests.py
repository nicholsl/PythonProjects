import codecs

nonBinaryKWF = codecs.open('myVocabulary.txt', mode ='r', encoding ='utf-8')
wordsToCheck = ['食卓', 'から', 'バナナ', 'が', '消える', 'かも']

moocow=[]

for line in nonBinaryKWF:
    moocow.append(line.strip('\n'))

wordsToAsk = []
found = False
for i in range(len(wordsToCheck)):
    print ("checking",wordsToCheck[i])
    for tear in moocow:
        print("checking",tear,"for",wordsToCheck[i])
        if wordsToCheck[i] in tear:
            found = True
            print ("I found",wordsToCheck[i],"in the file.")
        if not found:
            wordsToAsk.append(wordsToCheck[i])

'''taco = ['moo','taco','cat']
mafia = ['banana', 'foo', 'bar']

print ("The length of taco is,", len(taco))
for i in range(len(taco)):
    print(i)

for i in range(len(taco)):
    print ("we're looking at", taco[i],"in taco")
    for member in mafia:
        print(i, taco[i], member)

for word in wordsToCheck:
    for member in mafia:
        print (word, member)

for word in wordsToCheck:
    print (word)
    if not any(line.rstrip('\n') in word for line in nonBinaryKWF):
        print(word,"is not in file")
    else:
        print ('found it') '''
