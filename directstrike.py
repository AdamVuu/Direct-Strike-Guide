# Interactive Guide for Starcraft Arcade Game Direct Strike

from random import randint

#create a list of race options
race_list = ['Terran', 'Protoss', 'Zerg']

#assign a random race to the computer
computer = race_list[randint(0,2)]

options_list = ['Units', 'Upgrades', 'Economy']

t1Units_list = ['Marine', 'Marauder', 'Reaper']
t2Units_list = ['Ghost', 'Hellion', 'Hellbat', 'Siege Tank', 'Viking', 'Medivac', 'Banshee', 'Raven', 'Liberator' 'Widow Mine', 'Cyclone', ]
t3Units_list = ['Thor', 'Battlecruiser']

p1Units_list = ['Zealot', 'Adept', 'Stalker', 'Sentry']
p2Units_list = ['Dark Templar', 'High Templar', 'Archon', 'Warp Prism', 'Observer', 'Immortal', 'Disruptor','Phoenix', 'Oracle', 'Void Ray']
p3Units_list = ['Colossus', 'Carrier', 'Tempest']

z1Units_list = ['Zergling', 'Baneling', 'Roach', 'Ravager', 'Queen']
z2Units_list = ['Hydralisk', 'Lurker', 'Mutalisk', 'Corruptor', 'Infestor', 'Overseer']
z3Units_list = ['Viper', 'Utralisk', 'Brood Lord']

t1Upgrades_list = ['Infantry Weapons 1', 'Infantry Armor 2', 'Stimpack', 'Concussive Shells']
t2Upgrades_list = ['Infantry Weapons 2', 'Infantry Armor 2', 'Vehicle Weapons 1', 'Vehicle Weapons 2', 'Ship Weapons 1', 'Ship Weapons 2', 'Vehicle/Ship Armor 1,' 'Vehicle/Ship Armor 2', 'Infernal Pre-lighter,' 'Raven Energy', 'Medevac Boosters']
t3Upgrades_list = ['Infantry Weapons 3', 'Infantry Armor 3', 'Vehicle Weapons 3', 'Ship Weapons 3', 'Vehicle/Ship Armor 3']

p1Upgrades_list = ['Ground Weapons 1', 'Ground Armor 1', 'Shields 1', ]
p2Upgrades_list = ['Ground Weapons 2', 'Ground Armor 2', 'Shields 2', 'Air Weapons 1', 'Air Armor 1', 'Air Weapons 2', 'Air Armor 2', 'Charge', 'Resonating Glaives', 'Blink', 'Shadow Step', 'Psionic Storm']
p3Upgrades_list = ['Ground Weapons 3', 'Ground Armor 3', 'Shields 3', 'Air Weapons 3', 'Air Armor 3']

z1Upgrades_list = ['Melee Attacks 1', 'Missile Attacks 1', 'Ground Carapace 1', 'Metabolic Boost', 'Pneumatized Carapace']
z2Upgrades_list =['Melee Attacks 2', 'Missile Attacks 2', 'Ground Carapace 2', 'Flyer Attacks 1', 'Flyer Attacks 2', 'Flyer Carapace 1', 'Flyer Carapace 2']
z3Upgrades_list = ['Melee Attacks 3', 'Missile Attacks 3', 'Ground Carapace 3', 'Flyer Attacks 1', 'Flyer Carapace 3']

#asks for player name
print('What is your name?')
myName = input()

#asks for player race
print('Hi {}, what race will you be playing as? ' .format(myName))

#set player to False
player = False
while player == False:
#set player to True
    player = input(race_list)
    if player == "Terran":
        print("Your race is ", player,  ".")  
        print("You will be playing against a ", computer,  ".")
        print('What will you open the game with?')
        firstchoice = False
        while firstchoice == False:
        #set firstchoice to True
            firstchoice = input(options_list)
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