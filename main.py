from classes import *
def main():
	player1 = Player()
	player2 = Computer()
	print(f"Hello {player1.name}")
	print(f"My name is {player2.name}. I am going to destroy you!")
	start = True
	while start == True:
		
		player1.get_attack(player2)
		print(f"{player2.name} has {player2.health} left")		
		player2.computer_turn(player1)
		print(f"Your health is {player1.health}")
		if player2.health <= 0:
			print(f"{player2.name} is defeated!")
			print("You win!")
			start = False
		elif player1.health <= 0:
			print(f"{player1.name} is defeaed!")
			print("Game over!")
			start = False

main()
