from random import randint, choice, random
from data.events import event_lookup_table, event_library
from data.afflictions import afflictions_library
from data.config import config
from model import Dog, Human
import sys
from data.shop import meal_options, walk_options, medications, care_items
import math

def affliction_detail_from_set(afflictionSubset: set) -> dict:
    '''Given a set of affliction names, return the actual values associated with those afflictions from the data libraries.'''
    return {key: value for key, value in afflictions_library.items() if key in afflictionSubset}

def call_or_get(value, dog):
    '''If the given value is a function, call it and return the value. If it is not a function simply return the value.'''
    if callable(value):
        return value(dog)
    return value

def update_model_stats(token: dict, token_name, human: Human, dog: Dog, show_display=True):
    '''
    This procedure performs an assembly line of checks on stat updates hitten by the token dictionary.
    Dog stats and human stats are updated as appropriate, and if show_display is True the changes are logged.
    '''

    token_name = token_name.replace("_", " ").title()

    if ("health" in token):
        health_value = call_or_get(token["health"], dog)
        dog.health += health_value
        if (health_value < 0 and show_display):
            human.log += f"{dog.name} lost health as a result of {token_name}. Take care!\n"
        elif (health_value > 0 and show_display):
            human.log += f"{dog.name} gained health as a result of {token_name}. Good work!\n"
    
    if ("max_health" in token):
        dog.max_health += call_or_get(token["max_health"], dog)
    
    if ("happiness" in token):
        happiness_value = call_or_get(token["happiness"], dog)
        dog.happiness += call_or_get(token["happiness"], dog)
        if (happiness_value < 0 and show_display):
            human.log += f"{dog.name} lost happiness as a result of {token_name}. Bummer!\n"
        elif(happiness_value > 0 and show_display):
            human.log += f"{dog.name} gained happiness as a result of {token_name}. Good work!\n"
    
    if ("training" in token):
        training_value = call_or_get(token["training"], dog)
        dog.training += training_value
        if (training_value < 0 and show_display):
            human.log += f"{dog.name} is more poorly behaved as a result of {token_name}.\n"
        elif(training_value > 0 and show_display):
            human.log += f"{dog.name} is better behaved as a result of {token_name}.\n"
    
    if ("cost" in token):
        cost = call_or_get(token["cost"], dog)
        human.balance -= cost
        if (show_display):
            human.log += f"You spent ${cost} to resolve {token_name}.\n"
    
    if ("time" in token):
        human.time_spent -= call_or_get(token["time"], dog)
        human.log += f"You spent {token['time']} hours of time on handling {token_name}.\n"
    
    if ("afflictions" in token and len(call_or_get(token["afflictions"], dog)) > 0):
        dog.afflictions = dog.afflictions | affliction_detail_from_set(call_or_get(token["afflictions"], dog))
        human.log += "Your dog has suffered an affliction.\n"
    
    if ("treatments" in token):
        for affliction_to_treat in call_or_get(token["treatments"]):
            dog.afflictions[affliction_to_treat]["duration"] = 0

def load_event(dog):
    '''
    Returns an event dictionary. The event dictionary chosen is selected at random, but algorithmically more likely to be a lower severity event than a higher severity event. Events which have already been chosen will not reload unless they represent an affliction which can be suffered multiple times.
    '''
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
    '''Update Model attributes based on event given and the user option selected.'''
    event_outcome = event["options"][int(decision)]
    update_model_stats(event_outcome, event["name"], human, dog)

    #If not an affliction tag the event so it doesn't get replayed later
    #Event names don't always cleanly map to an affliction name, removed common affliction suffixes for better comparison.
    if event["name"].replace("_medicated", "").replace("_unchecked", "") not in afflictions_library.keys():
        dog.tags.add(event["name"])
    return dog, human

def next_round(dog:Dog, human:Human, event):
    '''Update all attributes in the model to reflect the passing of 6 months. Return a string to be displayed by the view, which summarizes the events.'''

    #Update dog age
    summary_paragraph = 'A whole 6 months have passed! The following occured over the period of time:\n\n'
    dog.age += config["months_per_round"] / 12

    #Walk dog
    human.log += f'You spent {dog.walk_time} hours walking {dog.name}.\n'
    human.time_spent += dog.walk_time
    dog.health += walk_options[dog.walk_schedule]["health"]
    dog.happiness += walk_options[dog.walk_schedule]["happiness"]
        
    #Feed dog
    human.log += f'You spent ${dog.meal_expense} paying for your dogs meals.\n'
    human.balance -= dog.meal_expense
    dog.health += meal_options[dog.meal_plan]["health"]
    dog.happiness += meal_options[dog.meal_plan]["happiness"]
    
    #Dog plays with items and wears them out
    for item_name, item_detail in dog.items.items():
        update_model_stats(item_detail, item_name, human, dog, False) #There are too many items to show all updates.
        dog.items[item_name]["duration"] -= 1.
        if (dog.items[item_name]["duration"]) < 1:
            human.log += f"{dog.name} completely used their {item_name}.\n"

    #Remove expired items
    dog.items = {key: value for key, value in dog.items.items() if value["duration"] > 0}
    
    #Remove used up meds
    for med_name, med_detail in dog.medications.items():
        dog.medications[med_name]["duration"] -= 1
        if (med_detail["treatment"] in dog.afflictions.keys()):
            dog.afflictions[med_detail["treatment"]]["duration"] = 0
            human.log += f"You have treated {dog.name} of {med_detail['treatment']}.\n"
        if (dog.medications[med_name]["duration"]) < 1:
            human.log += f"You ran out of {med_name} for {dog.name}.\n"

    dog.medications = {key: value for key, value in dog.medications.items() if value["duration"] > 0}
    
    #Dog suffers from afflictions and may get better
    for affliction_name, affliction_detail in dog.afflictions.items():
        dog.afflictions[affliction_name]["duration"] -= 1
        update_model_stats(affliction_detail, affliction_name, human, dog)
        if dog.afflictions[affliction_name]["duration"] < 1:
            human.log += f"{dog.name} no longer suffers from {affliction_name}.\n"

    dog.afflictions = {key: value for key, value in dog.afflictions.items() if value["duration"] > 0}

    #Handle dog death or surrender
    if not dog.alive:
        human.log += f"After {dog.age} trips around the sun, {dog.name}'s life has come to an end.\n"
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
    elif dog.surrendered:
        human.log += f"Your balance has exceeded the minimum threshold meaning you are no longer able to financially support {dog.name}.\n"
        human.log += f"{dog.name} has been surrendered to a shelter."

    #Normal output
    if dog.alive:
        human.log += f"You spent a total of ${human.round_expenses} on {dog.name} over the past 6 months.\n"
        human.log += f"You earned ${human.revenue} of disposable income for your doggy fund over the past 6 months.\n"
        human.log += f"After expenses and revenue, your balance has changed by ${round(human.revenue - human.round_expenses, 2)}.\n"
        human.balance += human.revenue
    else:
        human.log += f"You spent a total of ${human.total_expenses} and {human.time_spent} hours on {dog.name} over the course of {dog.name}'s life.\n"
    summary_paragraph += human.log
    human.round_expenses = 0 #reset for next round
    human.log = str() #reset for next round
    return dog, human, summary_paragraph

def check_resistance(dog: Dog, event: dict) -> bool:
    '''Calls the resistance function specified within an event detail, and returns the value.'''
    return (event["resist"]["check"](dog))

