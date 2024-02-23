from random import randint
from Model import Dog, Human
import sys

def get_event():
	event_table = ["fleas", "burr in paw", "torn nail", "nausea and vomiting"]
	return event_table[randint(0, len(event_table) - 1)]

dog = Dog()
human = Human(2000)
print("Welcome to the dog game! Your dogs name is: " + dog.get_name())
while dog.is_alive():
	dog.update_age(6)
	dog.update_max_health(-5)
	if not (dog.is_alive()):
		print("Your dog has died!")
	print("Here is how your dog is doing:")
	dog.print_attributes()

	print("Here is how you are doing:")
	human.print_attributes()
	print(f"Your dog suffers from: {get_event()}, what do you do?")
	print(f"1. Take your dog to the vet?")
	print(f"2. Do nothing and hope things get better.")
	while True:
		try:
			choice = int(sys.stdin.readline())
		except ValueError:
			print("Please enter a valid number.")
			continue
		if (choice == 1):
			if (human.pay(100)):
				print("You lose $100 but your dog is well!")
			else:
				print("Sorry you can't afford to take your dog to the vet.")
			break
		elif (choice == 2):
			dog.update_health(-5)
			print("Your poor dog looks miserable.")
			break
		else:
			print("Please enter either 1 or 2.")
