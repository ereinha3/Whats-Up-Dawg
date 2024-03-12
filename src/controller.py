from random import randint, choice, random
from data.events import event_lookup_table, event_library
from data.afflictions import afflictions_library
from model import Dog, Human, config
import sys
from data.shop import meal_options, walk_options, medications, care_items
import math

def percentCheck(value):
    return randint(1, 100) < value

def affliction_detail_from_set(afflictionSubset: set) -> dict:
    return {key: value for key, value in afflictions_library.items() if key in afflictionSubset}

def call_or_get(value, dog):
    if callable(value):
        return value(dog)
    return value

def update_model_stats(token: dict, token_name, human: Human, dog: Dog):

    print(f"Updating model based on {token_name}")
    print(token)

    if ("health" in token):
        health_value = call_or_get(token["health"], dog)
        dog.health += health_value
        if (health_value < 0):
            human.log += f"{dog.name} lost health as a result of {token_name}. Take care!\n"
        else:
            human.log += f"{dog.name} gained health as a result of {token_name}. Good work!\n"
    if ("max_health" in token):
        dog.max_health += call_or_get(token["max_health"], dog)
    if ("happiness" in token):
        happiness_value = call_or_get(token["happiness"], dog)
        dog.happiness += call_or_get(token["happiness"], dog)
        if (happiness_value < 0):
            human.log += f"{dog.name} lost happiness as a result of {token_name}. Bummer!\n"
        else:
            human.log += f"{dog.name} gained happiness as a result of {token_name}. Good work!\n"
    if ("training" in token):
        training_value = call_or_get(token["training"], dog)
        dog.training += training_value
        if (training_value < 0):
            human.log += f"{dog.name} is more poorly behaved as a result of {token_name}\n"
        else:
            human.log += f"{dog.name} is better behaved as a result of {token_name}\n"
    if ("cost" in token):
        cost = call_or_get(token["cost"], dog)
        human.balance -= cost
        human.log += f"You spent ${cost} to resolve {token_name}\n"
    if ("time" in token):
        human.time_spent -= call_or_get(token["time"], dog)
    if ("afflictions" in token):
        dog.afflictions = dog.afflictions | affliction_detail_from_set(call_or_get(token["afflictions"], dog))
        human.log += "Your dog has suffered an affliction.\n"
    if ("treatments" in token):
        for affliction_to_treat in call_or_get(token["treatments"]):
            dog.afflictions[affliction_to_treat]["duration"] = 0

def load_event(dog):
    while 1:
        event_probabilities = list(event_lookup_table)
        event_probabilities.remove(0)
        new_probabilities = []
        end = event_probabilities[-1]
        for i in range(len(event_probabilities)):
            new_probabilities += [event_probabilities[i] for i in range(end)]
            end -= 1
        probability_of_non_affliction = [0 for x in range(int((dog.max_age-dog.age)//3))]
        selection = choice([choice(new_probabilities)]+probability_of_non_affliction)
        name = choice(list(event_lookup_table[selection]))

        #Don't give the dog cancer twice at once
        if name in dog.afflictions.keys():
            continue

        #Don't give a user the same random event twice
        elif name in dog.tags:
            continue
        return event_library[name]

def handle_event(event, decision, dog:Dog, human:Human) -> None:
    event_outcome = event["options"][int(decision)]
    update_model_stats(event_outcome, event["name"], human, dog)

    #If not an affliction tag the event so it doesn't get replayed later
    if event["name"] not in afflictions_library.keys():
        dog.tags.add(event["name"])
    return dog, human

def next_round(dog:Dog, human:Human, event):

    #Update dog age
    summary_paragraph = 'A whole 6 months have passed! The following occured over the period of time:\n\n'
    dog.age += config["months_per_round"] / 12

    #Update walk time
    human.log += f'You spent {dog.walk_time} hours walking {dog.name}.\n'
    human.time_spent += dog.walk_time
        
    #Update meal expenses
    human.log += f'You spent ${dog.meal_expense} paying for your dogs meals.\n'
    human.balance -= dog.meal_expense

    #Dog suffers from afflictions and may get better
    for affliction_name, affliction_detail in dog.afflictions.items():
        update_model_stats(affliction_detail, affliction_name, human, dog)
        if dog.afflictions[name]["duration"] < 1:
            human.log += f"{dog.name} no longer suffers from {affliction_name}.\n"

    dog.afflictions = {key: value for key, value in dog.afflictions.items() if value["duration"] > 0}
    
    #Dog plays with items and wears them out
    for item_name, item_detail in dog.items.items():
        print(item_name, item_detail)
        update_model_stats(item_detail, item_name, human, dog)
        dog.items[item_name]["duration"] -= 1.
        if (dog.items[item_name]["duration"]) < 1:
            human.log += f"{dog.name} completely used their {item_name}.\n"

    #Remove expired items
    dog.items = {key: value for key, value in dog.items.items() if value["duration"] > 0}
    
    #Remove used up meds
    for med_name, med_detail in dog.medications.items():
        dog.medications[med_name]["duration"] -= 1
        if (dog.medications[med_name]["duration"]) < 1:
            human.log += f"You ran out of {med_name} for {dog.name}.\n"

    dog.medications = {key: value for key, value in dog.medications.items() if value["duration"] > 0}

    #Handle dog death
    if dog.health <= 0:
        human.log += f"After {dog.age} trips around the sun, {dog.name}'s life has come to an end.\n"
    elif dog.surrendered:
        human.log += f"Your balance has exceeded the minimum threshold meaning you are no longer able to financially support {dog.name}.\n"
        human.log += f"{dog.name} has been surrendered to a shelter."
    
    if dog.alive:
        human.log += f"You spent a total of ${human.round_expenses} on {dog.name} over the past 6 months.\n"
        human.log += f"You earned ${human.revenue} of disposable income for your doggy fund over the past 6 months.\n"
        human.balance += human.revenue
    else:
        human.log += f"You spent a total of ${human.total_expenses} on {dog.name} over the course of {dog.name}'s life.\n"
    summary_paragraph += human.log
    human.round_expenses = 0 #reset for next round
    human.log = str() #reset for next round
    return dog, human, summary_paragraph

def check_resistance(dog: Dog, event: dict) -> None:
    return (event["resist"]["check"](dog))

'''
        human.log += "The cause of death was ruled to be: "
        afflictions_list = list(dog.afflictions.keys())
        if len(afflictions_list) != 0:
            if len(afflictions_list)>1:
                for affliction in afflictions_list[:-1]:
                    human.log += f"{affliction}, "
                human.log += f"and {afflictions_list[-1]}.\n"
            else:
                human.log += f"{afflictions_list[0]}.\n"
        else:
            human.log += "natural causes.\n"
        dog.alive = False
'''        
