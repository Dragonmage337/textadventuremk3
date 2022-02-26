"Pokemon Red : The Text Adventure"

"""
///Glossary///
    print - prints a string, or a line of code
    def - defines a function
    input - gets an input from the user
    time.sleep() - tells the computer to wait a certain amount of seconds before running -
    - the next line of code
    if - only runs the code in the statement if a certain condition has been completed
    elif - else if 
    while - while a condition is true or false
    dictionary - holds a large amount of values that can be changed.
    /n - sends the string to a new line

///End of Glossary///
 """
#Imports the time module to tell the computer to wait seconds defined by code
import time
#A dictionary containing multiple values for the pokemon base stats.



#defines a function to print a statement and start another function.
def OakIntro():
    
    print("Oak : Hello there! Welcome to the world of POKEMON! My name is OAK!\n"
    "People call me the POKEMON PROF!\n")
    time.sleep(1)
    print("This world is inhabited by creatures called POKEMON! For some"
            "people, POKEMON are pets. Others use them for fights.\n Myself..."
            "I study POKEMON as a profession.\n")
#runs all of the functions after a 5 second wait.
    time.sleep(5)
    UserName()
    RivalName()
    ChoosePokemon()
    FirstBattle()
#Asks the user for input then stores the input.
def RivalName():
    rivalname = input("Your rival is my grandson...um, what was his name again?\n")
    RIVALNAME ["legs squared"] = rivalname
    time.sleep(1)
    print("Oh, so his name is ",RIVALNAME ["legs squared"])
#Asks the user for input and then stores that input.
def UserName():
    username = input("First,what is your name?\n")
    USERNAME ["legs"] = username
    time.sleep(1)
    print("Oh, so your name is ",USERNAME ["legs"])
#Asks the user what their starter pokemon is
def ChoosePokemon():
    #Assigns a variable to an input, then runs the input.
    #An if/else conditional to confirm the user's choice
    while True:
        starter = input("There are 3 pokemon in front of you. Which do you choose? ")
        #try:
        sPokemon = starter # 'Charmander'
        print(sPokemon)
        RivalPokeman = StarterPokemon[StarterPokemon.index(sPokemon) + 1]
        print(RivalPokeman)
        print("Make sure to raise this pokemon with patience. It is a fiesty pokemon.\n")
        time.sleep(1)
        print(RIVALNAME ["legs squared"]," : Fine, i'll take ")
        print(RivalPokeman)
        print("then.\n")
       # except:
            #print("not a valid pokemon nerd")
        break


#A function that runs the first battle
def FirstBattle():
    print(USERNAME ["legs"],", just as you attempt to leave...")
    print(RIVALNAME ["legs squared"]," : Hey! Let's test our Pokemon!")
    time.sleep(1)
    print("You've been challenged to a battle!")
    time.sleep(1)
    print("To be continued...")
    


#A simple function to start the game
def Start_Game():
    start_game = input("Start Game? [y/n]   ")
    if start_game == 'y' or 'yes':
        OakIntro()
    else:
        print("i dont understand what that means, you nerd")
        Start_Game()
#A loop to keep the game going.
while True:
    Start_Game()
    






 
