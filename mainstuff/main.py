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
    startgame = input("Start your adventure?    [y/n]\n")

#Intro Scene of the adventure
def SleepRoom():
    Scroll()

    
#A function to scroll the screen down.
def Scroll():
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
    nickname = input("Before we start your adventure what is your name")
    PLAYER ["playername"] = nickname
    print(PLAYER ["playername"])

Nickname()