from random import randint
from Model import Dog, Human
from data.breeds_dict import breeds
from Events import load_event, play_event
import sys

def life_cycle_update(dog: Dog, human: Human, months: int) -> None:
    dog.update_age(months)
    dog.activate_afflictions()
    human.deposit(human.get_revenue() * months - dog.get_expenses() * months)
    human.relax()

#shop menu numbers are mocked
#need research to support specific costs
shop_menu = {
        "treat": {
            "cost": 5,
            "happiness": 2
            },
        "puzzle": {
            "cost": 50,
            "duration": 15,
            "satisfy": 25,
            },
        "plushy": {
            "cost": 15,
            "duration": 5,
            "satisfy": 15
            },
        "nylon_bone": {
            },
        "butcher_bone": {
            },
        "kong": {
            },
        "bed": {
            },
        }

def display_shop_menu(dog: Dog, human: Human) -> None:
    print(f"What would you like to buy for your dog?")
    print(f"1. I'm finished shopping")
    print(f"2. Doggy Treat")
    print(f"3. Plushy Toy")
    print(f"4. Doggy Puzzle")
    print(f"5. Nylon Bone")
    print(f"6. Butcher Bone")
    print(f"7. Kong")
    choice = sys.stdin.readline()
    match choice:
        case "1":
            return
        case _:
            "Shop prices not implemented yet."


def display_walk_menu(dog: Dog, human: Human) -> None:
    print(f"You are currently taking your dog on {dog.get_walk_schedule()}.")

def display_meal_menu(dog: Dog, human: Human) -> None:
    print(f"Meal menu not yet implemented.")

def display_medication_menu(dog: Dog, human: Human) -> None:
    print(f"Medication menu not yet implemented.")

def display_treatment_menu(dog: Dog, human: Human) -> None:
    print(f"Treatment menu not yet implemented.")

def display_lifestyle_actions(dog: Dog, human: Human) -> None:
    print(f"Your dog is {dog.age // 12} years and {dog.age % 12} months old!")
    print(f"Looking back over the last few months, you reflect on whether it is time to make any changes.")
    print(f"1. I think my dog and I are doing as well as we can be. Let's see what the future brings!")
    print(f"2. Check my current financial and time-off status.")
    print(f"3. Take my dog to the vet for a check-up.")
    print(f"4. Make some purchases for my dog.")
    print(f"5. Change my dog's walking schedule.")
    print(f"6. Change my dog's meal plan.")
    print(f"7. Update my dog's medication plan.")
    print(f"8. Surrender your dog to a shelter.")
    print()

    choice = sys.stdin.readline().strip()

    match choice:
        case "1":
            return
        case "2":
            human.print_attributes()
        case "3":
            if (human.pay(50)):
                dog.print_attributes()
                display_treatment_menu(dog, human)
            else:
                print("You cannot afford to take your dog for a checkup.")
        case "4":
            display_shop_menu(dog, human)
        case "5":
            display_walk_menu(dog, human)
        case "6":
            display_meal_menu(dog, human)
        case "7":
            display_medication_menu(dog, human)
        case "8":
            dog.surrender()
            return
        case _:
            print("Please enter a valid menu option.")

    return display_lifestyle_actions(dog, human)

def main() -> None:
    dog = Dog()
    human = Human(3000)
    print("Welcome to the dog game! Your dogs name is: " + dog.get_name())
    while True:
        life_cycle_update(dog, human, 12)
        
        if not (dog.is_alive()):
            print("Your dog has died!")
            break
        
        display_lifestyle_actions(dog, human)

        if dog.is_surrendered():
            print("You have surrendered your dog to a shelter.")
            break

    
        event = load_event()
        play_event(dog, human, event)

if __name__ == "__main__":
    main()
