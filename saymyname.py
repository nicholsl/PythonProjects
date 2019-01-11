#saymyname.py
guess = str()
for guess in range(3):
    guess = (input("What's my name?")).lower()
    print(guess)
    if guess == 'liz':
        print("That's it!")
        break
    else:
        print("Try again!")
