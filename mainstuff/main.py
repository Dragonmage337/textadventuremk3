#Glossary of things you use
"""
///Glossary///

variable - holds a statement to be used again.

input - a built in function that takes user statements and utilizes them in the code.
"""
#imports the time module that can tell the computer to wait before doing the next task.
from operator import invert
import time
import random
from commonv import PLAYER
from commonv import INVENTORY
from commonv import TIMESPLAYED
#Start Game function to initiate the story

def StartGame():
    #           Asks for the input of the user
    startgame = input("Start your adventure?    [y/n]           ")
    if startgame == 'y':
        Nickname()
        TIMESPLAYED ["amountplayed"] = TIMESPLAYED ["amountplayed"] + 1
    else:
        print("Too bad.")
        Nickname()
        TIMESPLAYED ["amountplayed"] = TIMESPLAYED ["amountplayed"] + 1

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
    print("You climb out of the bed and stand in the middle of your room.")
    leave = input("Do you leave your home or just sit here and wait?")
    if leave.lower() == 'y' or leave.lower() == 'leave':
        LeaveRoom()
    elif leave.lower() == 'n' or leave.lower() == 'wait' or leave.lower() == 'no':
        print("Ok then.")
        Scroll()
        print("You sat there and waited. Your boss calls you from work and screams '' You're FIRED''")
        time.sleep(1)
        print("But, on the bright side, you found your old NotBible!!!")
        INVENTORY ["NotBible"] == True
        print(INVENTORY ["NotBible"])
        time.sleep(1)
        print("Congratulations! You got fired from your job and became useless to society! Ending 1 out of 4")
        StartGame()
   
def LeaveRoom():
    print("You leave your room and sprint to work as you realize that you are late.")
    Scroll()
    print("But you come to some obstructions in your path.")
    Scroll()
    rando = random.randrange(1,10)
    if rando > 3:
        Obstruction1()
    elif rando < 3:
        Obstruction2
    elif rando == 10:
        Obstruction3()

def Obstruction1():
    print("You have been locked into an unending ad!")
    time.sleep(10)
    while True:
        print("Have you heard of Raid Shadow Legends!?!???!")
        print("Ending 2 out of 4")

def Obstruction2():
    print("You come across an annoying person in the street who won't stop talking.")
    Scroll()
    print("You have sat here for hours...")
    Scroll()
    print("And they just keep on talking...")
    Scroll()
    print("Ending 3 out of 4")
    StartGame()

def Obstruction3():
    print("You come across nothing. Its oddly silent. Weird. You continue onto"
    " work like nothing happened and you don't get fired.")
    time.sleep(1)
    print("Ending 4 out of 4")
    time.sleep(2)
    print("SIKE")
    Obstruction1()


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
    if confirm.lower() == 'y' or confirm.lower() == 'yes':
        print("Ok, let's continue.")
        SleepRoom()
    elif confirm.lower() == 'n' or confirm.lower() == 'no':
        Nickname()
    else:
        print("I don't understand what that means...")

StartGame()