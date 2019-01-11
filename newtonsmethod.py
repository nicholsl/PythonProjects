#newtonsmethod.py

#guesses the square root of a number using newtons method and refines
#the guess a number of times specified by the user

def newtonsmethod(x , numberOfTimesToGuess):
    #initial guess (arbitrary)
    guess = x/2
    for attempt in range(numberOfTimesToGuess):
        guess = (guess + (x/guess))/2
    return guess

def main():
    x=float(input('What number would you like the square root of?'))
    numberOfTimesToGuess = int(input('How many times would you like to improve your guess?'))
    guess = newtonsmethod(x , numberOfTimesToGuess)
    print('Our guess for the square root of', x,'was',guess,'.')
    print('The actual square root of',x,'is',(x**(1/2)),'. Our guess was off by', abs(guess-(x**(1/2))))

if __name__ == "__main__":
    main()
