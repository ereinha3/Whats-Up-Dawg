from random import randint, choice
from data.event_library import event_lookup_table
from data.afflictions import afflictions_dictionary
from model import Dog, Human
import sys
from data.shop import meal_options, default_walk_options, medications, care_items

def percentCheck(value):
    return randint(1, 100) < value

def load_event():
    affliction_probabilities = list(afflictions_dictionary.keys())
    affliction_probabilities.remove(0)
    new_probabilities = []
    end = affliction_probabilities[-1]
    for i in range(len(affliction_probabilities)):
        new_probabilities += [affliction_probabilities[i] for i in range(end)]
        end -= 1
    # 25% chance that the selected affliction occurs, 75% chance a random non-affliction event occurs
    selection = choice([0, 0, 0, choice(new_probabilities)])
    return event_lookup_table[choice(list(afflictions_dictionary[selection].keys()))]
    #return event_lookup_table[list(event_lookup_table)[randint(0, len(event_lookup_table) - 1)]]

def determine_event_outcome(options: dict, human: Human):
    # for key, value in options.items():
        # print(key + ".", value["intro"])

    choice = sys.stdin.readline().strip() # TODO - Replace with 

    if (choice not in options.keys()):
        # print("Please enter a valid option number.\n")
        return determine_event_outcome(options, human)
    
    selection = options[choice]
    if ("cost" in selection and selection["cost"] > human.get_balance()):
        # print("It is good of you to try but you cannot afford the expense. You'll have to pick another option.")
        return determine_event_outcome({key: value for key, value in options.items() if key != selection}, human)
    if ("work" in selection and selection["work"] > human.get_time()):
        # print("Unfortunately you do not have enough time. You'll have to pick another option.")
        return determine_event_outcome({key: value for key, value in options.items() if key != selection}, human)

    return selection

def next_round(dog:Dog, human:Human):
    # take 5% of income for now
    human.balance += human.revenue
    
    # Multiply by 180 here to accurately calculate the time over 6 month
    human.time_spent += default_walk_options[dog.walk_schedule]["time"] * 180
    
    # Dividing by 4 to get price per 4oz, then multiply by cups eaten per day, then by 180 to find total cost
    human.balance -= meal_options[dog.meal_plan]["cost"]/4 * dog.calculate_food_per_day() * 180
    
    # Half a year
    dog.age += 0.5
    old_max = dog.max_health
    
    # Dog max age has to be multiplied by two to account for the fact that this is a 6 month, not a year-long, round
    dog.max_health -= 100/(dog.max_age*2)
    if dog.max_health <= 0:
        dog.alive = False
    dog.health = dog.health/old_max * dog.max_health
    if dog.health <= 0:
        dog.alive = False
    
    # TODO: Apply medications to afflictions and get rid of them if applicable
    for illness in dog.afflictions
    
    # Apply afflictions
    for illness in dog.afflictions:
        dog.health += afflictions_dictionary[illness]["health"]
        dog.happiness += afflictions_dictionary[illness]["stress"]
        if (dog.medications
        
    # Remove timed our durations on items
    for item in dog.items:
        item = care_items[item]
        dog.happiness += item["happiness"]
        dog.health += item["health"]
        item["duration"] -= 1
        if item["duration"] == 0:
            dog.items.remove(item)
    for medication in dog.medications:
        medication = medications[medication]
        human.balance -= medication["cost"]
        medication["duration"] -= 1
        if medication["duration"] == 0:
            dog.medications.remove(medication)
    
    human.balance = round(human.balance, 2)
    return dog, human

def check_resistance(dog: Dog, human: Human, event: dict) -> None:
    print(event["intro"] + "\n")
    if (event["resist"]["check"](dog)):
        # print(event["resist"]["message"])
        return True
    else:
        return False
    
    outcome = determine_event_outcome(event["options"], human)
    
    # if "cost" in outcome:
    #     human.pay(outcome["cost"])
    # if "work" in outcome:
    #     human.work(outcome["work"])
    # if "harm" in outcome:
    #     dog.update_health(-outcome["harm"])
    # if "stress" in outcome:
    #     dog.update_happiness(-outcome["stress"])
    # if "afflictions" in outcome:
    #     dog.add_afflictions(outcome["afflictions"])
    
    # print(outcome["outro"])


def event_loader(dog: Dog):
    # Event Load Logic Goes Here
    event = load_event()

# def life_cycle_update(dog: Dog, human: Human, months: int) -> None:
#     dog.update_age(months)
#     dog.activate_afflictions()
#     human.deposit(human.get_revenue() * months - dog.get_expenses() * months)
#     human.relax()
#     dog.walk()
#     dog.play()

# def buy(dog: Dog, human: Human, item: dict, item_key: str, add_func):
#     bought = human.pay(item["cost"])
#     if bought:
#         add_func({item_key: item})
#         print("You bought your dog a " + item["display"])
#     else:
#         print("You cannot afford that.")

# def display_shop_menu(dog: Dog, human: Human, menu: dict, add_func) -> None:
#     print(f"What would you like to buy for your dog?\n")
#     print(f"1. Exit Store.")
#     menu_table = list(menu)
    
#     #list shop menu options
#     for i, entry in enumerate(menu_table):
#         print(f"{i + 2}. {menu[entry]['display']} (${menu[entry]['cost']})")
    
#     #gather user input
#     choice = sys.stdin.readline().strip()

#     #convert user input to int
#     try:
#         choice = int(choice)
#     except ValueError:
#         print("Please enter a valid option number.")
#         return display_shop_menu(dog, human, menu, add_func)

#     #Exit store
#     if (choice == 1):
#         return

#     elif (choice > 1 and choice - 1 <= len(menu_table)): # Ignore options outside the menu_table range
#         buy(dog, human, menu[menu_table[choice - 2]], menu_table[choice - 2], add_func) # -1 to compensate for 0 index, -1 to compensate for 1. choice being hardcoded
#     else: 
#         print("Please enter a valid option number.")

#     return display_shop_menu(dog, human, menu, add_func)

# def display_walk_menu(dog: Dog, human: Human) -> None:
#     print(f"You are currently taking your dog on {dog.get_walk_schedule_name()} walks.\n")
#     print(f"1. Keep this schedule.")
#     print(f"2. Begin short walks (30 minutes a day).")
#     print(f"3. Begin medium walks (1 hour a day).")
#     print(f"4. Begin long walks (2 hours a day).\n")
#     choice = sys.stdin.readline().strip()
#     match choice:
#         case "1":
#             return
#         case "2":
#             dog.update_walk_schedule("short")
#         case "3":
#             dog.update_walk_schedule("medium")
#         case "4":
#             dog.update_walk_schedule("long")
#         case _:
#             print("Please enter a valid option number.")
#             return display_walk_menu(dog, human)
            
# def display_meal_menu(dog: Dog, human: Human) -> None:
#     print(f"You are currently feeding your dog {dog.get_meal_plan()['display']}.\n")
#     status1 = "Keep" if dog.get_meal_plan()["display"] == "Walmart's Finest" else "Switch to"
#     status2 = "Keep" if dog.get_meal_plan()["display"] == "Vet Recommended" else "Switch to"
#     print(f"1. {status1} Walmart's Finest")
#     print(f"2. {status2} Vet Recommended")
#     choice = sys.stdin.readline().strip()
#     match choice:
#         case "1": 
#             dog.set_meal_plan("cheap")
#             print("Your dog is eating the cheapest dog food that money can buy. It is much more affordable than vet recommended dog food, but is by all accounts less good for the dog.")
#         case "2":
#             dog.set_meal_plan("vet_recommended")
#             print("Your dog is eating vet recommended dog food, a pricier but healthier option.")
#         case _:
#             print("Please enter a valid option number.")
#             return display_meal_menu(dog, human)

# def display_medication_menu(dog: Dog, human: Human) -> None:
#     print(f"Medication menu not yet implemented.")

# def display_treatment_menu(dog: Dog, human: Human) -> None:
#     print(f"Treatment menu not yet implemented.")

# def display_lifestyle_actions(dog: Dog, human: Human) -> None:
#     print(f"Your dog is {dog.age // 12} years and {dog.age % 12} months old!")
#     print(f"Looking back over the last few months, you reflect on whether it is time to make any changes.\n")
#     print(f"1. I think my dog and I are doing as well as we can be. Let's see what the future brings!")
#     print(f"2. Check my current financial and time-off status.")
#     print(f"3. Take my dog to the vet for a check-up.")
#     print(f"4. Purchase some care items for my dog.")
#     print(f"5. Change my dog's walking schedule.")
#     print(f"6. Change my dog's meal plan.")
#     print(f"7. Update my dog's medication plan.")
#     print(f"8. Surrender your dog to a shelter.")
#     print()

#     choice = sys.stdin.readline().strip()

#     match choice:
#         case "1":
#             return
#         case "2":
#             human.print_attributes()
#         case "3":
#             if (human.pay(50)):
#                 dog.print_attributes()
#                 display_treatment_menu(dog, human)
#             else:
#                 print("You cannot afford to take your dog for a checkup.")
#         case "4":
#             display_shop_menu(dog, human, care_items, dog.add_possessions)
#         case "5":
#             display_walk_menu(dog, human)
#         case "6":
#             display_meal_menu(dog, human)
#         case "7":
#             print("Your dog currently has the following medications {dog.get_medications()}.")
#             print("What medications would you like to purchase for your dog?\n")
#             display_shop_menu(dog, human, medications, dog.add_medication)
#         case "8":
#             dog.surrender()
#             return
#         case _:
#             print("Please enter a valid menu option.")

#     return display_lifestyle_actions(dog, human)

# def main() -> None:
#     dog = Dog()
#     human = Human()
#     print("Welcome to the dog game! What would you like to name your dog?")
#     dog.set_name(sys.stdin.readline().strip())
#     print("Your dogs name is: {dog.get_name()}\n")
#     print("Caring for a dog can require a substantial financial investment. What is your monthly income?")

#     while True:
#         try:
#             income = float(sys.stdin.readline())
#             human.init_income(income)
#             print(f"You have set your income at {income}. It is not recommended to spend more than 5% of your income on a pet. Therefore the amount of money you will have to spend on your dog in a month is 5% of your monthly.")
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     print("How much time do you have during the week to look after your dog?")

#     while True:
#         try:
#             time = float(sys.stdin.readline())
#             human.init_time(time)
#             print(f"You have {time} hours in the week to look after your dog.")
#             break
#         except ValueError:
#             print("Please enter a valid number.")

#     while True:
#         life_cycle_update(dog, human, 6)
        
#         if not (dog.is_alive()):
#             print("Your dog has died!")
#             break
        
#         display_lifestyle_actions(dog, human)

#         if dog.is_surrendered():
#             print("You have surrendered your dog to a shelter.")
#             break

    
#         event = load_event()
#         play_event(dog, human, event)

# if __name__ == "__main__":
#     main()
