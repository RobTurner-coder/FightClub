import random
class Player:
# initialises player class
	def __init__(self):
		self.name = input("What is your name >>  ")
		self.health = 100
		self.attack = 10
		self.ice = 20
		self.healing = 30

	def get_attack(self, target):#gets user input for attack
		user_input = input("What would you like to do? 1 = ATTACK | 2 = ICE | 3 = HEAL >> ")
		if user_input == "1":#basic attack
			self.basic_attack(target)
			return self.attack
		elif user_input == "2":#ice attack
			self.ice_attack(target)
			return self.ice
		elif user_input == "3":
			self.heal()

	def basic_attack(self, target):
			target.health -= self.attack
			print(f"{self.name} attacked {target.name} with a basic attack for {self.attack} damage")
			
	
	def ice_attack(self, target):
		target.health -= self.ice
		print(f"{self.name} attacked {target.name} with an ice attack for {self.ice} damage")

	def heal(self):
		heal_amount = self.healing
		self.health = min(self.health + heal_amount, 100)
		print(f"You healed yourself for {self.healing} hit points! You now have {self.health} hit points")

	

class Computer:
	def __init__(self):
		self.name = "Gilgamesh"
		self.health = 100
		self.attack = 10
		self.ice = 20
		self.mega_flare = 50

	def computer_turn(self, target):
		attack_list = [self.basic_attack, self.ice_attack, self.mega_flare_attack]
		random_attack = random.choice(attack_list)
		random_attack(target)
		

	def basic_attack(self, target):
		target.health -= self.attack
		print(f"{self.name} attacks you with a basic attack doing {self.attack} damage!")
	
	def ice_attack(self, target):
		target.health -= self.ice
		print(f"{self.name} attacks you with ice for {self.ice} damage")

	def mega_flare_attack(self, target):
		target.health -= self.mega_flare
		print(f"{self.name} attacks you with MEGA FLARE for {self.mega_flare} damage")
