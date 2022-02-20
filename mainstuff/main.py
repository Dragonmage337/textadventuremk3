#Glossary of things you use
"""
///Glossary///

variable - holds a statement to be used again.

input - a built in function that takes user statements and utilizes them in the code.
"""
#imports the time module that can tell the computer to wait before doing the next task.
import time
from commonv import PLAYER
#Start Game function to initiate the story
def StartGame():
    #           Asks for the input of the user
    startgame = input("Start your adventure?    [y/n]           ")
    if startgame == 'y' or 'yes':
        Nickname()

    else:
        print("Too bad.")
        Nickname()

#Intro Scene of the adventure
def SleepRoom():
    Scroll()
    print("WAKE UP YOU LAZY BUM")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("*groan*")
    time.sleep(2)
    print("WAKE UP")
    print("Thump...")


    
#A function to scroll the screen down.
def Scroll():
    # goes to a new line
    print("\n")
    #Tells the computer to wait 1 second
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    

#A function to get the nickname of the character
def Nickname():
    #variable holding input of the user.
    nickname = input("Before we start your adventure what is your name?\n")
    #sets a dictionary key to the user's input
    PLAYER ["playername"] = nickname
    #Prints the gained user input
    print("So your name is", PLAYER ["playername"])
    #Gets user input to confirm
    confirm = input("[y/n]          ")
    #If elif else conditional that continues on in a certain
    # way depending on the user input.
    if confirm == 'y' or 'yes':
        print("Ok, let's continue.")
        SleepRoom()
    elif confirm == 'n' or 'no':
        Nickname()
    else:
        print("I don't understand what that means...")

StartGame()