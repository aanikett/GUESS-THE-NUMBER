# welcome to the "Guess the Number", a python based game
import random

def guessthenumber(y):
    count=1;
    while (count<=5):
        print("Enter your", count, "guess\n")
        x=int(input())
        if (x==y):
            print("YOU'VE GUESSED THE RIGHT NUMBER!!!!\n")
            print("THE RIGHT NUMBER WAS", y, "!!!!\n")
            exit()
        elif (y>x):
            if (y-x<10):
                print("You're close!! Guess a bit higher!\n")
                count=count+1
            else:
                print("Your're guessing very low!")
                count=count+1
        elif (y<x):
            if (x-y>10):
                print("You're close!! Guess a bit lower!\n")
                count=count+1
            else:
                print("Your're guessing very high!")
                count=count+1
        else:
            count=count+1





print("Welcome to the Guess the Number game - a game based on python\n")
print("Rules:\n")
print("1. The system will select a number between 1 and 100\n")
print("2. You have to guess the number\n")
print("3. You only have five guesses to guess the right number\n")
print("IF YOU'RE READY, PRESS Y TO ENTER THE GAME OR ANY OTHER KEY TO EXIT THE GAME\n")
ch=input()
if ((ch == 'Y') or (ch == 'y')):
    print("THE GAME IS STARTING NOWW!!\n")
    print("THE SYSTEM IS GUESSING THE NUMBER!!\n")
    y=random.randint(1,100)
    guessthenumber(y)
else:
    exit()
print("SEEMS LIKE YOU'RE OUT OF GUESSES!!\n")
print("BETTER LUCK NEXT TIME!!\n")
print("THE RIGHT NUMBER WAS", y, "!!!!\n")
