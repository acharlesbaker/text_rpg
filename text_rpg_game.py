"""
A simple choose your own adventure style RPG. Players will be able to choose from
3 different classes, assign points to their stats at level up and battle monsters. 
"""
import time
import os
import sys



class Player():
	def __init__(self,p_name='Bobert'):
		self.player_name = p_name
		self.job = ''
		self.level = 1

#class Inventory():
#	def __init__(self,job):
#		if job == 'Fighter':
#			self.equipment = {'Armor': 'Chainmail', 'Weapon': 'Longsword'}
#			self.inv = ['Weak Health Potion', '10 gp']
#		elif job == 'Mage':
#			self.equipment = {'Armor': 'Thin Cloak', 'Weapon': 'Magic'}
#			self.inv = ['Spellbook', 'Tome of Healing']
#		elif job == 'Thief':
#			self.equipment = {'Armor': 'Tacticool Stealth Ninja Suit', 'Weapon': 'Ninja Stars'}
#			self.inv = ['Weak Stealth Potion', "Mom's Chicken Dinner"]

def clear():
    # for windows 
    os.system('cls' if os.name == 'nt' else 'clear')

def print_slow(str):
	#for char in str:
		#print(char, end='') 
	    #sys.stdout.flush() 
	    #time.sleep(0.05) 
	print(str)

def get_job():
	print_slow('\n\nYou may choose between three classes. They are: \nFighter - Strong in body but not in mind \nMage - Strong in mind but not in body \nThief - Neither strong in body or mind \n\n')
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
		print_slow(fighter_job)
	elif player.job == 'Mage':
		mage_job = "\nExcellent choice. While you won't be a physical threat to anyone, they say the pen is mightier than the sword. That's what they say, anyway."
		player.equipment = {'Armor': 'Thin Cloak', 'Weapon': 'Magic'}
		player.inv = ['Spellbook', 'Tome of Healing']
		print_slow(mage_job)
	elif player.job == 'Thief':
		mage_job = "\nInteresting choice. Not one I would of made, but if your morals are suspect then perhaps a life of crime will suit you."
		player.equipment = {'Armor': 'Tacticool Stealth Ninja Suit', 'Weapon': 'Ninja Stars'}
		player.inv = ['Weak Stealth Potion', "Mom's Chicken Dinner"]
		print_slow(mage_job)
	#player_inv = Inventory(player.job)
	time.sleep(2)

def get_inv():
	#return "Equiped Armor: {armor}\nEquipped Weapon: {weapon}\nBag Contents: {bag}".format(armor=player.equipment['Armor'],weapon=player.equipment['Weapon'],bag=player.inv)
	print("Equiped Armor: {armor}\nEquipped Weapon: {weapon}\nBag Contents: {bag}".format(armor=player.equipment['Armor'],weapon=player.equipment['Weapon'],bag=player.inv))

def get_command():
	command = 'not_a_command'
	#command_list = {'inv':print(get_inv())}
	command = input('')
	for key in command_list.keys():
		if command == key:
			#command_list[command]
			pass
		elif command == 'inv':
			get_inv()
		else:
			print_slow("I'm sorry {name}, {uput} is not a valid command. Were you paying attention during the tutorial?".format(name=player.player_name,uput=command))
			get_command()

clear()

hello_str = 'Hello adventurer, I am Adev, and I will lead you on your path to greatness. \nBefore we begin, what is your name?'

print_slow(hello_str)

player = Player(input('\nPlayer Name: '))
time.sleep(1)
clear()

i_see_str = 'I see, so your name is {name}.\n'.format(name=player.player_name)

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

time.sleep(1)
get_command()
time.sleep(1)
#get_job()
#input('prompt:')

#test_input = input('wtf')
#excel_str = '\nExcellent. You have chosen wisely, {name}'.format