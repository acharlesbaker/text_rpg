"""
A simple choose your own adventure style RPG. Players will be able to choose from
3 different classes, assign points to their stats at level up and battle monsters. 
"""

import time
import os
import sys

'''
Defining a couple classes that will be used to build objects used throughout the game, such as player and locations.
'''
class Player():
	def __init__(self,p_name='Bobert'):
		self.player_name = p_name.title()
		self.job = ''
		self.level = 1
class Room():
	def __init__(self,loc_desc,exits,loot):
		self.loc_desc = loc_desc
		self.exits = exits
		self.loot = loot
'''
Building all the neccesary functions to be used in the game.
'''
def clear():
    # for windows 
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(str):
	for char in str:
		print(char, end='') 
		sys.stdout.flush()
		time.sleep(0.05) 
	#print(str)

def get_job():
	print_slow('\n\nYou may choose between three classes. They are: \n- Fighter - Strong in body but not in mind \n- Mage - Strong in mind but not in body \n- Thief - Neither strong in body or mind \n\n')
	player.job = input('Class:')
	player.job = player.job.title()
	if player.job not in ['Fighter', 'Mage', 'Thief']:
		invalid_job = "I'm sorry, {job} is not a valid class. Please try again.".format(job=player.job)
		print_slow(invalid_job)
		time.sleep(2)
		clear()
		get_job()
		#for char in invalid_job:
		#	print(char, end='')
		#	time.sleep(.02)
	elif player.job == 'Fighter':
		fighter_job = "\nExcellent choice. While you won't be solving any theoretical physics equations, you won't have any problem bringing physics into the equation."
		player.equipment = {'Armor': 'Chainmail', 'Weapon': 'Longsword'}
		player.inv = ['Weak Health Potion', '10 gp']
		player.health = 15
		player.strength = 10
		player.mind = 5
		player.stealth = 0
		print_slow(fighter_job)
	elif player.job == 'Mage':
		mage_job = "\nExcellent choice. While you won't be a physical threat to anyone, they say the pen is mightier than the sword. That's what they say, anyway."
		player.equipment = {'Armor': 'Thin Cloak', 'Weapon': 'Magic'}
		player.inv = ['Spellbook', 'Tome of Healing']
		player.health = 5
		player.strength = 5
		player.mind = 15
		player.stealth = 5
		print_slow(mage_job)
	elif player.job == 'Thief':
		mage_job = "\nInteresting choice. Not one I would of made, but if your morals are suspect then perhaps a life of crime will suit you."
		player.equipment = {'Armor': 'Tacticool Stealth Ninja Suit', 'Weapon': 'Ninja Stars'}
		player.inv = ['Weak Stealth Potion', "Mom's Chicken Dinner"]
		player.health = 10
		player.strength = 5
		player.mind = 5
		player.stealth = 10
		print_slow(mage_job)
	#player_inv = Inventory(player.job)
	time.sleep(2)

def get_inv():
	print("Equiped Armor: {armor}\nEquipped Weapon: {weapon}\nBag Contents: {bag}".format(armor=player.equipment['Armor'],weapon=player.equipment['Weapon'],bag=player.inv))

def get_stat():
	print("\nPlayer Name: {name}\nClass: {job}\nHealth: {health}\nStrength: {strength}\nMind: {mind}\nStealth: {stealth}".format(name=player.player_name, job=player.job, health=player.health, strength=player.strength, mind=player.mind, stealth=player.stealth))

def look():
	print(current_location.loc_desc)

def get_command():
	command_list = {'inv':get_inv, 'stat':get_stat, 'look':look}
	command = input('\n:')
	try:
		command_list[command]( )
	except:
		print_slow("I'm sorry {name}, {uput} is not a valid command. Were you paying attention during the tutorial?".format(name=player.player_name,uput=command))
		get_command()
	time.sleep(5)
	clear()
	if tut_act == True:
		pass
	else:
		get_command()

clear()

abyss = Room("You are in a deep, dark abyss. You appear to be floating in nothingness, standing on nothing with nothing around you and nothing above you. If you didn't know any better, you'd say you were dreaming.", None, None)

'''
Begin tutorial.
'''
tut_act = True
current_location = abyss

hello_str = '\nHello adventurer, I am Adev, and I will lead you on your path to greatness. \nBefore we begin, what is your name?'
print_slow(hello_str)

player = Player(input('\nPlayer Name: '))
time.sleep(1)
clear()

i_see_str = '\nI see, so your name is {name}.\n'.format(name=player.player_name)

print_slow(i_see_str)

time.sleep(1)
clear()

dest_str='\n{name}, it is time for you to choose which path your destiny will take.'.format(name=player.player_name)

print_slow(dest_str)

get_job()
clear()

okay_sofar = '\nOkay, so far we know your name is {name} and your class is {job}.'.format(name=player.player_name, job=player.job)

print_slow(okay_sofar)

lets_take_a_look = "\n\nLet's take a look at what you've got in your bag.\n\nWhat's that? Nothing you say?\n\nTake another look.\n\n\nYou can check your inventory at any time by typing 'inv' into the prompt."
print_slow(lets_take_a_look)

get_command()

other_commands = "\nThere are other commands available to you. Another valuable command is the 'stat' command, which pulls up your current player profile information. Try it now."
print_slow(other_commands)

get_command()

as_can_see = "\nAs you can see, {name}, there are some extremely powerful commands at your disposal. Now, let's take a look at where you are. Try the 'look' command.".format(name=player.player_name)
print_slow(as_can_see)

get_command()

print_slow("Time to wake up...")

time.sleep(4)
tut_act = False
current_location = Room("You are in a dark, barren cell. There is nothing to find here. There appears to be only one exit, and that is to the north.", ['n'], None)
get_command()


#get_job()
#input('prompt:')

#test_input = input('wtf')
#excel_str = '\nExcellent. You have chosen wisely, {name}'.format