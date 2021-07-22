import random

def guessthecolour(x):
    count=1


    while (count<=2):
        print("enter your", count, "guess\n")
        y=input()
        if (y==colourtuple[x]):
            print("YOU GUESSED IT CORRECTLY!!!!\n")
            print("Thank You for playing this game with me\n")
            exit()
        else:
            print("You guessed it wrong\n")
            count=count+1
            if (count>2):
                
                break

            print("Make another guess\n")







colourtuple=("violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red")
print("WELCOME TO GUESS THE COLOR GAME\n")
print("1. The computer will randomly pick a colour from the Rainbow colors.\n")
print("2. You will get two chances to guess it correctly\n")

x=random.randint(0,6)
guessthecolour(x)
print("Seems like you have wasted your guesses\n")
print("The right answer was - ")
print(colourtuple[x])
print("type y or n if you want to restart the game\n")
z=input()
if ((z=='y') or (z=='Y')):
    x=random.randint(0,6)
    guessthecolour(x)
else:
    print("closing the game\n")
    exit()
