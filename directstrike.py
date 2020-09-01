# Interactive Guide for Starcraft Arcade Game Direct Strike

from random import randint

#create a list of race options
race = ['Terran', 'Protoss', 'Zerg']

#assign a random race to the computer
computer = race[randint(0,2)]


#asks for player name
print('What is your name?')
myName = input()

#asks for player race
print('Hi {}, what race will you be playing as? ' .format(myName))

#set player to False
player = False
while player == False:
#set player to True
    player = input('Terran, Protoss, Zerg? ')
    if player == "Terran":
        print("Your race is ", player,  ".")  
        print("You will be playing against a ", computer,  ".")
    elif player == "Protoss":
        print("Your race is ", player,  ".")  
        print("You will be playing against a ", computer, ".")
    elif player == "Zerg":
        print("Your race is ", player,  ".")  
        print("You will be playing against a ", computer, ".")
    else:
        print("That's not a valid race. Pick a race.")