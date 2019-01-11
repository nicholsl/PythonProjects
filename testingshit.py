'''def getdata():
    username = input('what is your username?')
    password = input('what is your password?')
    return username, password

def unlocked():
    print("type 'lock' to lock your information.")
    print("Type 'show me' to see your username and password.")
    unlockresponse = input()
    return unlockresponse

def locked():
    print("It's locked!")
    lockresponse = input('tell me your username and password, separated by a comma')
    return lockresponse
    

def main():
    username, password=getdata()
    unlockresponse = unlocked()
    while unlockresponse != 'lock':
        if unlockresponse == 'show me':
            print(username, password)
            unlocked()
    lockresponse = locked()
    while lockresponse!= (username,',',password):
        print('still locked')
    unlocked()
main()'''

name = input('What is your Username: ')
password = input('What is your Password: ')
print ("To lock your computer type lock.")
command = None
input1 = None
input2 = None
while command != "lock":
    command = input("What is your command: ")
while input1 !=name:
    input1 = input("What is your username: ")
while input2 != password:
    input2 = input("What is your password: ")
print ("Welcome back to you system!")


    
    
