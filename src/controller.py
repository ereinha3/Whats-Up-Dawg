from random import randint, choice
from data.event_library import event_lookup_table
from data.afflictions import afflictions_dictionary
from model import Dog, Human
import sys
from data.shop import meal_options, walk_options, medications, care_items
import math

def percentCheck(value):
    return randint(1, 100) < value

def load_event(dog):
    while 1:
        affliction_probabilities = list(afflictions_dictionary.keys())
        affliction_probabilities.remove(0)
        new_probabilities = []
        end = affliction_probabilities[-1]
        for i in range(len(affliction_probabilities)):
            new_probabilities += [affliction_probabilities[i] for i in range(end)]
            end -= 1
        # 25% chance that the selected affliction occurs, 75% chance a random non-affliction event occurs
        probability_of_non_affliction = [0 for x in range(int((dog.max_age-dog.age)//3))]
        # print(probability_of_non_affliction)
        selection = choice([choice(new_probabilities)]+probability_of_non_affliction)
        name = choice(list(afflictions_dictionary[selection].keys()))
        if name not in dog.afflictions.keys():
            return event_lookup_table[name]

    #return event_lookup_table[list(event_lookup_table)[randint(0, len(event_lookup_table) - 1)]]

def find_affliction_from_event_name(event_name):
    for commonality, value in afflictions_dictionary.items():
        if event_name in value.keys():
            #print(commonality, value[event_name])
            return commonality, value[event_name]
    return None

def next_round(dog:Dog, human:Human):
    summary_paragraph = 'A whole 6 months have passed! The following occured over the period of time:\n\n'
    # take 5% of income for now
    start_balance = human.balance
    human.balance += human.revenue
    
    # Multiply by 180 here to accurately calculate the time over 6 month
    walk_time = walk_options[dog.walk_schedule]["time"] * 180
    human.time_spent += walk_time
    
    # Adding to time summary
    summary_paragraph += f'You spent {walk_time} walking {dog.name} over the last 6 months.\n'
    
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
    
    # TODO: Apply medications to afflictions and get rid of them if applicable
    
    # Apply afflictions
    afflictions_to_remove = []
    for illness in dog.afflictions.keys():
        dog.afflictions[illness][1] -= 1
        if dog.afflictions[illness][1] <= 0:
            afflictions_to_remove.append(illness)
        if event_lookup_table[illness]["resist"]["check"](dog):
            continue
        treatment = dog.afflictions[illness][0]
        affliction = find_affliction_from_event_name(illness)[1]
        if treatment:
            human.balance -= affliction["cure"]["cost"](dog)
            human.time_spent -= affliction["cure"]["work"]
            if illness not in afflictions_to_remove:
                summary_paragraph += f"{dog.name} still suffers from {illness}, but is undergoing treatment.\n"
        else:
            dog.health += affliction["health"]
            dog.happiness += affliction["stress"]
        

    for affliction in afflictions_to_remove:
        summary_paragraph += f"{dog.name} has been cured of {affliction} thanks to rigorous treatment.\n"
        dog.afflictions.pop(affliction)
        
    # Remove timed our durations on items
    items_to_remove = []
    for item in dog.items.keys():
        item = care_items[item]
        dog.happiness += item["happiness"]
        dog.health += item["health"]
        dog.items[item] -= 1
        if dog.items[item] <= 0:  
            items_to_remove.append(dog.items[item["display"]])

    for item in items_to_remove:
        summary_paragraph += f"{dog.name} completely used their {item}.\n"
        del item

    meds_to_remove = []
    for medication in dog.medications.keys():
        med_name = medication
        medication = medications[medication]
        human.balance -= medication["cost"]
        dog.medications[med_name] -= 1
        if dog.medications[med_name] <= 0:
            meds_to_remove.append(med_name)

    for medication in meds_to_remove:
        summary_paragraph += f"You ran out of {medication} for {dog.name}.\n"
        del medication
    
    human.balance = round(human.balance, 2)
    summary_paragraph += f"You spent a total of {start_balance-human.balance} on {dog.name} over the past 6 months.\n"
    return dog, human, summary_paragraph

def check_resistance(dog: Dog, event: dict) -> None:
    return (event["resist"]["check"](dog))
