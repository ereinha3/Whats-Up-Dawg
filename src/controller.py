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
        print(probability_of_non_affliction)
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
        
def handle_event(event:dict, button_number, dog:Dog, human:Human):
    affliction_name = event["name"]
    #print(affliction_name)
    initial_balance = human.balance
    commonality, affliction = find_affliction_from_event_name(affliction_name)
    #print(affliction)
    if str(button_number) == '1': #Human chose to treat
        if commonality != 0: # Is an affliction
            dog.afflictions[affliction_name] = [1, affliction['duration']]
        else:
            human.balance -= affliction["cure"]["cost"](dog)
            human.time_spent -= affliction["cure"]["work"]
    if str(button_number) == '2':
        if commonality != 0:
            dog.afflictions[affliction_name] = [0, math.inf]
        else:
            dog.health += affliction["health"]
            dog.happiness += affliction["stress"]
    human.balance = round(human.balance, 2)
    return dog, human, round(initial_balance-human.balance, 2)


def next_round(dog:Dog, human:Human, event_cost, event):
    summary_paragraph = 'A whole 6 months have passed! The following occured over the period of time:\n\n'
    # take 5% of income for now
    start_balance = human.balance
    
    
    # Multiply by 180 here to accurately calculate the time over 6 month
    walk_time = walk_options[dog.walk_schedule]["time"] * 180
    human.time_spent += walk_time
    
    # Adding to time summary
    summary_paragraph += f'You spent {walk_time} hours walking {dog.name} over the last 6 months.\n'
    
    # Dividing by 4 to get price per 4oz, then multiply by cups eaten per day, then by 180 to find total cost
    meal_cost = round(meal_options[dog.meal_plan]["cost"]/4 * dog.calculate_food_per_day() * 180,2)
    human.balance -= meal_cost
    
    # Add food costs to time summary
    summary_paragraph += f'You spent ${meal_cost} on food for {dog.name} over the last 6 months.\n'
    
    # Add event costs to time summary
    if event_cost > 0:
        summary_paragraph += f'You spent ${event_cost} on resolving {event} for {dog.name} over the last 6 months.\n'
    
    # Half a year
    dog.age += 0.5
    old_max = dog.max_health
    
    
    
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
        item_name = item
        item = care_items[item]
        dog.happiness += item["happiness"]
        dog.health += item["health"]
        dog.items[item_name] -= 1
        if dog.items[item_name] <= 0:  
            items_to_remove.append(item_name)
            # del dog.items[item["display"]]
    for item in items_to_remove:
        summary_paragraph += f"{dog.name} completely used their {item}.\n"
        dog.items.pop(item_name)
        del item

    meds_to_remove = []
    for medication in dog.medications.keys():
        med_name = medication
        medication = medications[medication]
        human.balance -= medication["cost"]
        dog.medications[med_name] -= 1
        if dog.medications[med_name] <= 0:
            meds_to_remove.append(med_name)
            # del dog.medications[medication]
    for medication in meds_to_remove:
        summary_paragraph += f"You ran out of {medication} for {dog.name}.\n"
        dog.medications.pop(medication)
        del medication
        
    # Dog max age has to be multiplied by two to account for the fact that this is a 6 month, not a year-long, round
    dog.max_health -= 100/(dog.max_age*2)
    dog.health = dog.health/old_max * dog.max_health
    
    if dog.health <= 0:
        summary_paragraph += f"After {dog.age} trips around the sun, {dog.name}'s life has come to an end.\n"
        summary_paragraph += "The cause of death was ruled to be: "
        afflictions_list = list(dog.afflictions.keys())
        if len(afflictions_list) != 0:
            if len(afflictions_list)>1:
                for affliction in afflictions_list[:-1]:
                    summary_paragraph += f"{affliction}, "
                summary_paragraph += f"and {afflictions_list[-1]}.\n"
            else:
                summary_paragraph += f"{afflictions_list[0]}.\n"
        else:
            summary_paragraph += "natural causes.\n"
        dog.alive = False
        
    elif human.dog.surrendered:
        summary_paragraph += f"Your balance has exceeded the minimum threshold meaning you are no longer able to financially support {dog.name}.\n"
        summary_paragraph += f"{dog.name} has been surrendered to a shelter."
    
    human.balance = round(human.balance, 2)
    if dog.alive:
        summary_paragraph += f"You spent a total of ${round(start_balance-human.balance+event_cost,2)} on {dog.name} over the past 6 months.\n"
        human.balance += human.revenue
    else:
        summary_paragraph += f"You spent a total of ${round(human.revenue*2*dog.age-human.balance,2)} on {dog.name} over the course of {dog.name}'s life.\n"
    return dog, human, summary_paragraph

def check_resistance(dog: Dog, event: dict) -> None:
    return (event["resist"]["check"](dog))
