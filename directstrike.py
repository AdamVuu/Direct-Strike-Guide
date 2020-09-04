# Interactive Guide for Starcraft Arcade Game Direct Strike

from random import randint

#create a list of race options
race = ['Terran', 'Protoss', 'Zerg']

#assign a random race to the computer
computer = race[randint(0,2)]

t1Units = ['Marine', 'Marauder', 'Reaper']
t2Units = ['Ghost', 'Hellion', 'Hellbat', 'Siege Tank', 'Viking', 'Medivac', 'Banshee', 'Raven', 'Liberator' 'Widow Mine', 'Cyclone', ]
t3Units = ['Thor', 'Battlecruiser']

p1Units = ['Zealot', 'Adept', 'Stalker', 'Sentry']
p2Units = ['Dark Templar', 'High Templar', 'Archon', 'Warp Prism', 'Observer', 'Immortal', 'Disruptor','Phoenix', 'Oracle', 'Void Ray']
p3Units = ['Colossus', 'Carrier', 'Tempest']



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
        print('What will you open the game with?')
        firstchoice = False
        while firstchoice == False:
        #set firstchoice to True
            firstchoice = input('Units, Upgrades, Economy? ')
            if firstchoice == 'Units':
                print('What units would you like to open with?')
                tUnits = input('Marine, Marauder, Reaper? ')
                print('You have decided to open up with a ', tUnits, ".")
                if tUnits != "Marine" == "Marauder" == "Reaper":
                    print("That's not a valid option. Choose another option.")
                    firstchoice == False
            elif firstchoice == 'Upgrades':
                print('What upgrades would you like to open with? ')
                tUpgrades == input('Special Upgrades, Weapon, Armor? ')
                print('You have decided to invest in ', tUpgrades, '.')
                if tUpgrades != "Special Upgrades" == "Weapon" == "Armor":
                    print("That's not a valid option. Choose another option.")
                    firstchoice == False
            elif firstchoice == 'Economy':
                print('You have decided to invest in economy and purchased a gas structure.')
            else:
                print("That's not a valid option. Choose another option.")
                firstchoice == False
        #firstchoice was set to True but we want it to be False so the loop continues
        firstchoice == False 
    elif player == "Protoss":
        print("Your race is ", player,  ".")  
        print("You will be playing against a ", computer, ".")
        print('What will you open the game with?')
        firstchoice = input('Units, Upgrades, Economy? ')
        if firstchoice == 'Units':
            print('What units would you like to open with?')
            pUnits = input('Zealot, Stalker, Sentry? ')
            print('You have decided to open with a', pUnits, '.')
            if pUnits != 'Zealot' == 'Stalker' == 'Sentry':
                print("That's not a valid option. Choose another option.")
                #firstchoice == False
        elif firstchoice == 'Upgrades':
            print('What upgrades would you like to open with?')
            pUpgrades = input('Special, Weapons, Armor? ')
            print('You have decided to open with', pUpgrades, 'upgrades.')
            if pUpgrades != 'Special' == 'Weapons' == 'Armor':
                print("That's not a valid option. Choose another option.")
        elif firstchoice == 'Economy':
            print('You have opened with an economy structure.')
            print('Your income has increased by xx. You can not place another gas structure down for 4 turns.')
    elif player == "Zerg":
        print("Your race is ", player,  ".")  
        print("You will be playing against a ", computer, ".")
        print('What will you open the game with?')
        firstchoice = input('Units, Upgrades, Economy? ')
        if firstchoice == 'Units':
            print('What units would you like to open with?')
            zUnits = input('Zergling, Baneling, Roach, Queen?')
            print('You have decided to open with a', zUnits, '.')
            if zUnits != 'Zergling' == 'Baneling' == 'Roach' == 'Queen':
                print("That's not a valid option. Choose another option.")
                #firstchoice == False
        elif firstchoice == 'Upgrades':
            print('What upgrades would you like to open with?')
            zUpgrades = input('Special, Weapons, Armor? ')
            print('You have decided to open with', zUpgrades, 'upgrades.')
            if zUpgrades != 'Special' == 'Weapons' == 'Armor':
                print("That's not a valid option. Choose another option.")
        elif firstchoice == 'Economy':
            print('You have opened with an economy structure.')
            print('Your income has increased by xx. You can not place another gas structure down for 4 turns.')
    
    else:
        print("That's not a valid race. Pick a race.")
    #player was set to True, but we want it to be False so the loop continues
    #player = False
    #computer = race[randint(0, 2)]