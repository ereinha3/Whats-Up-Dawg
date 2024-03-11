from random import randint, choice
from data.event_library import event_lookup_table
from data.afflictions import afflictions_dictionary
from model import Dog, Human, config
import sys
from data.shop import meal_options, walk_options, medications, care_items
import math

def percentCheck(value):
    return randint(1, 100) < value

def affliction_detail_from_set(afflictionSubset: set) -> dict:
    return {key: value for key, value in afflictions_dictionary.items() if key in afflictionSubset}

def update_model_stats(token: dict, human: Human, dog: Dog):
    if ("health" in token):
        dog.health += token["health"]
    if ("happiness" in token):
        dog.happiness += token["happiness"]
    if ("balance" in token):
        human.balance -= token["cost"]
    if ("time" in token):
        human.time -= token["time"]
    if ("afflictions" in token):
        dog.afflictions = dog.afflictions | affliction_detail_from_set(token["afflictions"])
    if ("treatments" in token):
        for affliction_to_treat in token["treatments"]:
            dog.afflictions[affliction_to_treat]["duration"] = 0

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

def handle_event(outcome, dog:Dog, human:Human) -> None:
    update_model_stats(outcome, human, dog)

def next_round(dog:Dog, human:Human, event_cost, event):

    #Update dog age
    summary_paragraph = 'A whole 6 months have passed! The following occured over the period of time:\n\n'
    dog.age += config["months_per_round"] / 12

    #Update walk time
    summary_paragraph += f'You spent {walk_time} hours walking {dog.name}.\n'
    human.time_spent += walk_options[dog.walk_schedule]["time"] * 30 * config["months_per_round"]
        
    #Update meal expenses
    summary_paragraph += f'You spent ${dog.meal_expense} paying for your dogs meals.\n'
    human.balance -= dog.meal_expense

    #Dog suffers from afflictions and may get better
    for affliction_name, affliction_detail in dog.afflictions.items():
        summary_paragraph += f'You have spent ${dog.afflictions[affliction_name]["cost"]} caring for your dogs {affliction_name}\n'.
        update_model_stats(affliction_detail, human, dog)
        if dog.afflictions[name]["duration"] < 1:
            summary_paragraph += f"{dog.name} no longer suffers from {affliction_name}.\n"

    dog.afflictions = {key: value in dog.afflictions.items() if value["duration"] > 0}
    
    #Dog plays with items and wears them out
    for item_name, item_detail in dog.items.items():
        update_model_stats(item_detail, human, dog)
        if (dog.items[item_name]["duration"] -= 1) < 1:
            summary_paragraph += f"{dog.name} completely used their {item_name}.\n"

    #Remove expired items
    dog.items = {key: value in dog.items.items() if value["duration"] > 0}
    
    #Remove used up meds
    for med_name, med_detail in dog.medications.items():
        if (dog.meds[med_name]["duration"] -= 1) < 1:
            summary_paragraph += f"You ran out of {med_name} for {dog.name}.\n"

    #Handle dog death
    if dog.health <= 0:
        summary_paragraph += f"After {dog.age} trips around the sun, {dog.name}'s life has come to an end.\n"
'''
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
'''        
    elif dog.surrendered:
        summary_paragraph += f"Your balance has exceeded the minimum threshold meaning you are no longer able to financially support {dog.name}.\n"
        summary_paragraph += f"{dog.name} has been surrendered to a shelter."
    
    if dog.alive:
        summary_paragraph += f"You spent a total of ${round(start_balance-human.balance+event_cost,2)} on {dog.name} over the past 6 months.\n"
        human.balance += human.revenue
    else:
        summary_paragraph += f"You spent a total of ${round(human.revenue*2*dog.age-human.balance,2)} on {dog.name} over the course of {dog.name}'s life.\n"
    human.balance = round(human.balance, 2)
    return dog, human, summary_paragraph

def check_resistance(dog: Dog, event: dict) -> None:
    return (event["resist"]["check"](dog))
