import random as rd

guessNo = rd.randint(1,100)
userGuessNo = int(input("Enter Guess no :- "))
counter = 1

while userGuessNo != guessNo:
    if userGuessNo > guessNo:
        print("Guess higher, think again")
    elif userGuessNo < guessNo:
        print("Guess lower, think again")
    userGuessNo = int(input("Enter Guess no :- "))
    counter += 1
    
print("Sahi Jawab")
print("you took",counter,"attempts")