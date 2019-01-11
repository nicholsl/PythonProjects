from tinysegmenter import *
import codecs
import re
import csv

def analyze():
    sentence = input(u"What would you like to analyze?")
    segmenter = TinySegmenter ()
    tokenized = segmenter.tokenize(sentence)
    justWords = []
    for character in tokenized:
        if character.isalpha():
            justWords.append(character)
    print(justWords)
    
    return justWords

def isKnown():
    # set removes duplicates in justWords
    justWords = set(analyze())

    #make a list for iteration
    wordsToCheck = list(justWords)
    
    #open file of currently known words for writing (binary format)
    knownWordsfile = open('myVocabulary.txt','ab+')
    
    # open file of currently known words so it can be read like a string
    nonBinaryKWF = codecs.open('myVocabulary.txt', mode ='r', encoding ='utf-8')
    
    # check words against file, appends words not in file to wordsToAsk
    wordsToAsk = []
    '''for i in range(len(wordsToCheck)):
        print ("checking",wordsToCheck[i])
        found = False
        for line in nonBinaryKWF:
            print("checking",line,"for",wordsToCheck[i])
            if wordsToCheck[i] in line:
                found = True
                print ("I found",wordsToCheck[i],"in the file.")
            if not found:
                wordsToAsk.append(wordsToCheck[i])'''

    for line in nonBinaryKWF:
        found = False
        for i in range(len(wordsToCheck)):
            if wordsToCheck[i] in line:
                found = True
                print ("I found",wordsToCheck[i],"in the file.")
            if not found:
                wordsToAsk.append(wordsToCheck[i])

    # create a list of unknown words to run through the dictionary
    unknownWords = []
    for word in wordsToAsk:
        print(word)
        known = input("Do you know this word? Y or N    ")
        print()
        if known == 'Y':
            knownWordsfile.write(word.encode('utf-8') + '\n'.encode('utf-8'))
        elif known == 'N':
            unknownWords.append(word)
    return unknownWords

def todaysFlashcardFilename():
    #choose how to save flashcards
    todaysFileName = input("What would you like to call this flashcard file? \n")

    return todaysFileName

def makeFlashcards():

    #loads the dictionary
    print("Please wait while the dictionary loads")
    taco = checkDictionary()

    #creates file for flashcards
    todaysFileName = todaysFlashcardFilename()
    todaysFlashcards = open(todaysFileName,'ab+')

    #opens file to document new flashcards
    currentlyExistingFlashcards = open('myFlashcards.txt','ab+')

    #opens same file to read in non-binary format to check for existing flashcards
    nonBinaryCEF = codecs.open('myFlashcards.txt', mode ='r', encoding ='utf-8')

    #calls the analyze function, checks to see if words are known, loads unknown words
    unknownWords = isKnown()

    # creates a list to hold dictionary results
    readingsAndDefinitions = []
    # holds words for which dictionary had trouble for use in later searches
    notFound = []

    # searches the dictionary for unknown words
    for word in unknownWords:
        try:
            print (word, taco[word])
            #add value to a list for use outside of dictionary
            readingsAndDefinitions.append((taco[word]))
        except UnicodeEncodeError:
            print (word, ';_;')
        except KeyError:
            print(word, 'is not in the dictionary!')
            notFound.append(word)

    # make note of unfound words
    if len(notFound)!= 0:
        print ("The following words were not found.")
        print(notFound)
    else: print('all words were found')
    
    # check the flashcards file for the presence of the word
    
    for i in range(len(unknownWords)):
        found = False
        for line in currentlyExistingFlashcards:
            if unknownWords[i] in line:
                found = True
                print ("You already have a flashcard for", unknownWords[i],"in the file.")
        if not found:
            # make a flashcard
            todaysFlashcards.write(unknownWords[i].encode('utf-8')+';'.encode('utf-8')+readingsAndDefinitions[i].encode('utf-8')+'\n'.encode('utf-8'))
            # document that it has been made
            currentlyExistingFlashcards.write(unknownWords[i].encode('utf-8') + '\n'.encode('utf-8'))

    print ('Flashcards were made')

def checkDictionary():
    jimbreen = codecs.open('JMdict_e 2', mode='r',encoding = "utf-8")
    theDictionary = jimbreen.readlines()

    newEntryPattern = re.compile('<entry>')
    entryClosePattern = re.compile('\/entry>')
    
    kanjiPattern = re.compile('<keb>(.+)<\/keb>\n')
    readingPattern = re.compile('<reb>(.+)<\/reb>\n')
    definitionPattern = re.compile('<gloss>(.+)<\/gloss>\n')

    taco = {}
    foundEntry = False
    k = 0
    for line in theDictionary:
        
        if re.match(newEntryPattern,line):

            foundEntry = True

            entry = ''
            readings = []
            definitions = []


            hasKey = False
            hasReadings = False
            hasDefinition = False
            allDefinitionsRead = False
            
        if re.match(entryClosePattern,line):
            foundEntry = False

        if foundEntry:

            if re.match(kanjiPattern,line):

                hasKey = True
                entry = (kanjiPattern.search(line)).group(1)
                
            if re.match(readingPattern,line):

                hasReadings = True
                readings.append((readingPattern.search(line)).group(1))
                
            if re.match(definitionPattern,line):

                if not hasKey and not hasReadings:
                    print('this entry doesnt have a key or readings')
                    foundEntry = False

                hasDefinition = True
                definitions.append((definitionPattern.search(line)).group(1))

            if re.match(r'<\/sense>',line):

                allDefinitionsRead = True

            if hasKey and hasReadings and hasDefinition and allDefinitionsRead:
                taco[entry] = (','.join(readings+definitions))
                foundEntry = False

            elif hasReadings and hasDefinition and allDefinitionsRead:
                taco[readings[0]] = (','.join(readings+definitions))
                foundEntry = False

    jimbreen.close()
    return taco




#def assistiveSearch():

            

#checks jimbreen for entry; once found
#returns entry from <entry> to </entry>
        
makeFlashcards()

from tinysegmenter import *

segmenter = TinySegmenter ()


#result = segmenter.tokenize(u'政府・与党は、地方に本社機能を移した企業への減税を２０１８年度まで維持する方針を固めた。安倍政権が地方創生の一環で１５年度に導入した「地方拠点強化税制」で、１７年度から減税額が縮小される予定だった。年末にまとめる与党の税制改正大綱に盛り込まれる見通しだ。')

#for word in result:
    #print(word)
